"""Sample script for testing video merge on server
"""
import os
import time
import urllib

from moviepy.editor import VideoFileClip, concatenate_videoclips
from nba_api.stats.endpoints import VideoDetails
from nba_api.stats.endpoints.videoeventsasset import VideoEventsAsset


def create_video_highlights_for_player(player_id: int = 1628368,
                                       team_id: int = 1610612758,
                                       game_id: str = '0022200036'):
    path = 'assets'
    video_details_for_player = VideoDetails(team_id=team_id,
                                            player_id=player_id,
                                            game_id_nullable=game_id,
                                            ).get_dict()
    player_highlights = video_details_for_player['resultSets']['playlist']
    filenames = []
    print("Start downloading video clips...")
    start_time = time.time()
    for highlight_info in player_highlights:
        print(f"downloading event_id={highlight_info['ei']}")
        video_data = VideoEventsAsset(
            game_id=game_id, game_event_id=highlight_info['ei'],
            # only for development
        ).get_dict()

        links = video_data['resultSets']['Meta']['videoUrls']
        if links:
            # choose best quality
            video_link = links[0]['lurl']
            filename = f"{game_id}_{player_id}_{highlight_info['ei']}.mp4"
            filename = os.path.join(path, filename)
            if not os.path.isfile(filename):
                try:
                    urllib.request.urlretrieve(video_link, filename)
                    filenames.append(filename)
                except Exception as err:
                    print(f'cant download event_id={highlight_info["ei"]}')
                    print(err)
                time.sleep(2)

    print(f"Downloading took {time.time() - start_time}")
    print("Start merging video")

    # merging highlights into one video
    clips = [VideoFileClip(file_name) for file_name in filenames]
    final_video = concatenate_videoclips(clips)
    final_video.to_videofile(f"{game_id}_{player_id}_final.mp4")


if __name__ == '__main__':
    create_video_highlights_for_player()
