"""Common data structures and functions used throughout the project
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, List


class GameStatusEnum(Enum):
    """Possible game statuses"""
    LIVE = 2
    FINAL = 3


@dataclass
class Team:
    """Info about a team"""
    team_id: int
    full_name: str
    tricode: str = ''  # Optional


@dataclass
class Game:
    """Info about particular game
    """
    game_id: str
    home_team: Team
    away_team: Team
    date: datetime.date
    status: int  # think of change
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
    def game_id(self) -> str:
        return self.game.game_id

    @property
    def teams_playing_tricodes(self) -> str:
        """names of teams playing"""
        return f"{self.game.away_team.tricode} vs " \
               f"{self.game.home_team.tricode}"

    @property
    def game_date(self) -> str:
        """Man-readable representation of game date
        Example: Nov 14"""
        fmt = '%b'
        return f"{datetime.strftime(self.game.date, fmt)} {self.game.date.day}"

    def get_stats(self, min_include: int):
        """return string representation of stats

        :parameter min_include - applies to rebounds and assists,
        min value from which to include stat in output
        """
        assists = '' if self.stats.assists < min_include \
            else f' {self.stats.assists} asts'
        rebounds = '' if self.stats.rebounds < min_include \
            else f" {self.stats.rebounds} rebs"
        return f"{self.stats.points} pts{assists}{rebounds}"


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
