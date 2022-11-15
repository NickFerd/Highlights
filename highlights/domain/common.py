"""Common data structures and functions used throughout the project
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List


@dataclass
class Game:
    """Info about particular game
    """
    game_id: str
    home_team: str
    away_team: str
    date: datetime.date
    # maybe need to add scores


@dataclass
class Stats:
    """Info about player stats
    """
    points: int
    assists: int
    rebounds: int
    other: Optional[dict] = None


@dataclass
class Player:
    """Encapsulates info about a player in particular game
    """
    player_id: int
    team_id: int
    name: str
    game: Game
    stats: Stats

    @property
    def game_id(self):
        return self.game.game_id


@dataclass
class Link:
    highlight_id: int
    url: str
    description: str = ''


@dataclass
class VideoMetaInfo:
    """meta info about created video (title, description, tags)
    """
    title: str
    description: str
    tags: List[str] = field(default_factory=list)
