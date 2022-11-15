"""Basic implementation of class that downloads assets and merges them into
one video
"""
from pathlib import Path
from typing import List
import uuid
import urllib3
import shutil

from pydantic import BaseModel

from highlights.domain.common import Link

from moviepy.editor import VideoFileClip, concatenate_videoclips

from highlights.exceptions import Abort


class BasicMerger:
    """Basic synchronous implementation of merger"""

    class Config(BaseModel):
        delete_assets: bool = True
        root_assets_folder: str = ''
        retry_on_error: int = 3

    def __init__(self, logger, merger_config):
        self.logger = logger
        self.config = merger_config

    def execute(self, links: List[Link]) -> str:
        """Entry point into merger
        For assets we create folder with unique name and delete after finish.

        Returns absolute path to the created video.
        """
        # generate unique uuid to store assets in folder with this name
        process_id = uuid.uuid4()
        self.logger.info(f"Start {self.__class__.__name__}. "
                         f"Total number of links received: {len(links)}. "
                         f"Process_id={process_id}")

        files_to_merge = []

        files_path = self._get_files_path(folder_name=process_id)
        for link in links:
            filename = self._get_filename(files_folder=files_path,
                                          file_name=f"{link.highlight_id}.mp4")
            self._download_asset(url=link.url, filename=filename)
            files_to_merge.append(filename)

        final_video = self._merge_video(files_to_merge=files_to_merge,
                                        name=f"{process_id}_final.mp4")
        self.logger.info(f"Successfully created video, name={final_video}")
        if self.config.delete_assets:
            self._cleanup(folder_name=files_path)
        return final_video

    def _get_files_path(self, folder_name) -> Path:
        """Create folder to store video assets and return path object"""
        assets_path = Path(self.config.root_assets_folder).joinpath(
            Path(f"{folder_name}")
        )
        if not assets_path.exists():
            assets_path.mkdir()
        return assets_path

    @staticmethod
    def _get_filename(files_folder: Path,
                      file_name: str) -> str:
        """Return file name"""
        file_object = files_folder.joinpath(Path(file_name))
        return str(file_object.resolve())

    @staticmethod
    def _cleanup(folder_name: Path):
        """Delete folder with assets after finish"""
        shutil.rmtree(path=folder_name)

    def _download_asset(self, url: str, filename: str):
        """Download video asset
        """
        http_manager = urllib3.PoolManager()
        tries_count = 0
        while tries_count < self.config.retry_on_error:
            try:
                response = http_manager.request("GET", url=url)
                with open(filename, "wb") as file:
                    file.write(response.data)
                break
            except Exception as err:
                self.logger.error(f"Error downloading this url: {url}\n"
                                  f"Error: {err}")
                tries_count += 1
        else:
            raise Abort("Failed to download needed video assets.")

    def _merge_video(self, files_to_merge: List[str], name: str) -> str:
        """Concatenate video clips into one video
        Return absolute path to created video
        """
        name = self._get_filename(files_folder=self._get_files_path(
            folder_name="final"), file_name=name)
        try:
            final_video = concatenate_videoclips(
                [VideoFileClip(clip) for clip in files_to_merge]
            )
            final_video.to_videofile(name)
        except Exception as err:
            self.logger.critical(f"Failed to merge video with name={name}\n"
                                 f"Error: {err}")
            raise Abort("Failed to merge video")

        return name
