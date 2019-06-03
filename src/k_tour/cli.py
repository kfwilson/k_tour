import click

from k_tour import Board
from knights_tour import is_valid_tour


@click.command()
@click.argument('tour-type')
@click.option('--board-size', '-s', default=8, help="The size of the board to tour. Defaults to 8.")
def tour(tour_type, board_size):
    """Build a square chessboard of given ``board_size`` (defaults to 8x8) and
    runs a tour of the given type on it.

    TOUR_TYPE may be 'naive', 'random', 'smart', or 'compare' (which will run
    both naive and smart).

    If ``board_size`` is 8, will check validity of tour path via the oracle from
    ``knights_tour``.

`   """
    b = Board(int(board_size))
    if tour_type == 'compare':
        tours = ['naive', 'smart']
    else:
        tours = [tour_type]
    for t in tours:
        route = b.tour(t)
        if b.board_size == 8:
            is_valid_tour([int(p) for p in route])