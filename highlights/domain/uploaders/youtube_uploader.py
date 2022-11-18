"""basic uploader to Youtube using Google API
"""
import pickle
from copy import copy
from pathlib import Path
from typing import List

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery, http
from google.auth.transport.requests import Request
from pydantic import BaseModel

from highlights.domain.common import VideoMetaInfo
from highlights.exceptions import NotAutomated


class Uploader:
    """Basic uploader
    """
    REQUEST_BODY = {
        'snippet': {
            'categoryId': 17,
            'title': '',
            'description': '',
            'tags': ['NBA', 'NBA highlights', 'Highlights', 'NBAdviser']
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    class Config(BaseModel):
        api_version: str = 'v3'
        api_name: str = 'youtube'
        cred_file: str = 'cred.pickle'
        production: bool = True
        scopes: List[str] = ['https://www.googleapis.com/auth/youtube.upload']
        client_secrets_file: str = ''

    def __init__(self, logger, uploader_config):
        self.logger = logger
        self.config = uploader_config
        self.request_body = copy(self.REQUEST_BODY)

    def execute(self, video_path: str, meta_info: VideoMetaInfo):
        """Perform upload
        """
        youtube_api = self._get_youtube_api()
        self.request_body['snippet']['title'] = meta_info.title
        self.request_body['snippet']['description'] = meta_info.description
        self.request_body['snippet']['tags'].extend(meta_info.tags)

        media_file = http.MediaFileUpload(video_path)
        response = youtube_api.videos().insert(part='snippet, status',
                                               body=self.request_body,
                                               media_body=media_file).execute()
        self.logger.debug(response)

    def _get_youtube_api(self):
        """get instance of youtube api wrapper
        """
        credentials = self._obtain_credentials()
        try:
            youtube_api = discovery.build(self.config.api_name,
                                          self.config.api_version,
                                          credentials=credentials)
            return youtube_api
        except Exception as err:
            self.logger(f"Error connecting to Youtube API\n Error: {err}")

    def _obtain_credentials(self) -> Credentials:
        """Perform load of credentials from pickle file and check if valid

        Raises error if in production and we need to redirect to browser for
        login
        """
        if Path(self.config.cred_file).exists():
            with open(self.config.cred_file, "rb") as file:
                cred = pickle.load(file)
        else:
            return self._login_action()

        if cred.expired and cred.refresh_token:
            # refresh token
            self.logger.info('Try to refresh an expired token')
            cred.refresh(Request())
            with open(self.config.cred_file, "wb") as file:
                pickle.dump(cred, file)
        return cred

    def _login_action(self) -> Credentials:
        """perform manual login action if possible

        Raises NotAutomated if browser is unavailable
        """
        if not self.config.production:
            self.logger.warning("Start Google manual login action")
            flow = InstalledAppFlow.from_client_secrets_file(
                self.config.client_secrets_file, self.config.scopes
            )
            cred = flow.run_local_server()
            with open(self.config.cred_file, "wb") as file:
                pickle.dump(cred, file)
            return cred
        else:
            raise NotAutomated("Abort login action")
