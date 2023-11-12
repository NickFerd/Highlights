"""Script adapted to work from CLI
"""

import click

from highlights.scripts.manual_basic_flow_highlights import setup


@click.command()
@click.option("--game_id", type=str)
@click.option("--player_name", type=str, default=None)
@click.option("--player_id", type=int, default=None)
def main(game_id: str, player_name: str, player_id: int):
    """CLI script"""
    setup(player_name, game_id, player_id)


if __name__ == '__main__':
    main()
