"""Common data structures and functions used throughout the project
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


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
    name: str
    game: Game
    stats: Stats
