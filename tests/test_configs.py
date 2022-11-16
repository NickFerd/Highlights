"""tests for configs
"""
import os
from unittest.mock import patch

from highlights.config import BasicFlowConfig


@patch.dict(os.environ, {"MERGER__RETRY_ON_ERROR": "4"})
def test_basic_flow_config():
    assert BasicFlowConfig().dict() == {
        'highlighter': {
            'sleep_between_nba_api_seconds': 1
        },
        'log': {
            'filename': '/var/log/highlights/log.txt',
            'level': 'INFO',
            'rotation': '1 week'
        },
        'merger': {
            'delete_assets': True,
            'retry_on_error': 4,
            'root_assets_folder': ''
        },
        'uploader': {
            'api_name': 'youtube',
            'api_version': 'v3',
            'client_secrets_file': '',
            'cred_file': 'cred.pickle',
            'production': True,
            'scopes': ['https://www.googleapis.com/auth/youtube.upload']
        },
        'min_value_stats': 6,
        "max_number_videos": 4,
        'video_description': '#nba #nbahighlights\n'
                             'Most impressive performances of the game day - '
                             'NBAdviser Highlights'
    }
