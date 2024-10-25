#!/bin/python3

from typing import Callable


def compute_ring(rows_count: int, cols_count: int, row: int, col: int) -> int:
    """
    Compute the matrix ring (i.e. distance from the border) of the given
    `row`/`col` pair.
    """
    return min(row, col, rows_count - 1 - row, cols_count - 1 - col)


def compute_ring_size(rows_count: int, cols_count: int, ring: int) -> int:
    """
    Compute the size of the given ring in terms of matrix cells.
    """
    if rows_count == 1:
        return cols_count
    if cols_count == 1:
        return rows_count
    return (rows_count - 2 * ring) * 2 + (cols_count - 2 * ring - 2) * 2


def go_left(rotation: int, col: int, ring: int) -> tuple[int, int]:
    """
    Update `col` and `rotation` after going left as much as possible.
    """
    shift = min(rotation, col - ring)
    col -= shift
    rotation -= shift
    return col, rotation


def go_right(rotation: int, col: int, cols_count: int, ring: int) -> tuple[int, int]:
    """
    Update `col` and `rotation` after going right as much as possible.
    """
    shift = min(rotation, cols_count - 1 - ring - col)
    col += shift
    rotation -= shift
    return col, rotation


def go_up(rotation: int, row: int, ring: int) -> tuple[int, int]:
    """
    Update `row` and `rotation` after going up as much as possible.
    """
    shift = min(rotation, row - ring)
    row -= shift
    rotation -= shift
    return row, rotation


def go_down(rotation: int, row: int, rows_count: int, ring: int) -> tuple[int, int]:
    """
    Update `row` and `rotation` after going down as much as possible.
    """
    shift = min(rotation, rows_count - 1 - ring - row)
    row += shift
    rotation -= shift
    return row, rotation


def compute_old_position(
    rows_count: int, cols_count: int, rotation: int, row: int, col: int
) -> tuple[int, int]:
    """
    Compute the old position of the given `row`/`col` pair before an
    anti-clockwise rotation. This is achieved by rotating clockwise the pair.
    """
    ring = compute_ring(rows_count, cols_count, row, col)
    ring_size = compute_ring_size(rows_count, cols_count, ring)
    # A rotation which is an exact multiple of ring_size has no effect on the
    # matrix
    rotation = rotation % ring_size

    # Until there's still some budget for rotation:
    # - choose a direction
    # - follow the direction as much as possible
    # - update row/col and rotation
    while rotation > 0:
        if row == ring:
            if col == cols_count - 1 - ring:
                row, rotation = go_down(
                    rotation=rotation, row=row, rows_count=rows_count, ring=ring
                )
            else:
                col, rotation = go_right(
                    rotation=rotation, col=col, cols_count=cols_count, ring=ring
                )
        elif row == rows_count - 1 - ring:
            if col == ring:
                row, rotation = go_up(rotation=rotation, row=row, ring=ring)
            else:
                col, rotation = go_left(rotation=rotation, col=col, ring=ring)
        elif col == ring:
            row, rotation = go_up(rotation=rotation, row=row, ring=ring)
        elif col == cols_count - 1 - ring:
            row, rotation = go_down(
                rotation=rotation, row=row, rows_count=rows_count, ring=ring
            )
        else:
            raise ValueError(f"Unexpected coordinates for {ring=}: {row=}, {col=}")

    assert rotation == 0, rotation
    return row, col


def matrix_rotation(
    matrix: list[list[int]], rotation: int, output_sink: Callable[[str], None] = print
):
    if matrix is None:
        raise ValueError("'matrix' cannot be None")
    if rotation is None or rotation < 0:
        raise ValueError(f"'rotation' cannot be {rotation}")

    rows_count = len(matrix)
    if not rows_count:
        return

    cols_count = len(matrix[0])
    if not cols_count:
        return

    if min(rows_count, cols_count) % 2 != 0:
        raise ValueError(f"Unexpected matrix size: {rows_count}x{cols_count}")

    def get_new_value(row: int, col: int) -> int:
        """
        Get a value from the new matrix (after anti-clockwise rotation) at the
        position `row`/`col`.
        """

        old_row, old_col = compute_old_position(
            rows_count=rows_count,
            cols_count=cols_count,
            rotation=rotation,
            row=row,
            col=col,
        )
        return matrix[old_row][old_col]

    for row in range(rows_count):
        output_sink(" ".join(str(get_new_value(row, col)) for col in range(cols_count)))


# Hackerrank-generated section
if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrix_rotation(matrix, r)
