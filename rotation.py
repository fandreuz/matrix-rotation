#!/bin/python3


def computeRing(rows_count: int, cols_count: int, row: int, col: int) -> int:
    return min(row, col, rows_count - 1 - row, cols_count - 1 - col)


def computeRingSize(rows_count: int, cols_count: int, ring: int) -> int:
    return (rows_count - 2 * ring) * 2 + (cols_count - 2 * ring - 2) * 2


def goLeft(rotation: int, col: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, col - ring)
    col -= shift
    rotation -= shift
    return col, rotation


def goRight(rotation: int, col: int, cols_count: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, cols_count - 1 - ring - col)
    col += shift
    rotation -= shift
    return col, rotation


def goUp(rotation: int, row: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, row - ring)
    row -= shift
    rotation -= shift
    return row, rotation


def goDown(rotation: int, row: int, rows_count: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, rows_count - 1 - ring - row)
    row += shift
    rotation -= shift
    return row, rotation


def computeOldPosition(
    rows_count: int, cols_count: int, rotation: int, row: int, col: int
) -> tuple[int, int]:
    ring = computeRing(rows_count, cols_count, row, col)
    ring_size = computeRingSize(rows_count, cols_count, ring)
    rotation = rotation % ring_size
    while rotation > 0:
        if row == ring:
            if col == cols_count - 1 - ring:
                row, rotation = goDown(
                    rotation=rotation, row=row, rows_count=rows_count, ring=ring
                )
            else:
                col, rotation = goRight(
                    rotation=rotation, col=col, cols_count=cols_count, ring=ring
                )
        elif row == rows_count - 1 - ring:
            if col == ring:
                row, rotation = goUp(rotation=rotation, row=row, ring=ring)
            else:
                col, rotation = goLeft(rotation=rotation, col=col, ring=ring)
        elif col == ring:
            row, rotation = goUp(rotation=rotation, row=row, ring=ring)
        elif col == cols_count - 1 - ring:
            row, rotation = goDown(
                rotation=rotation, row=row, rows_count=rows_count, ring=ring
            )
        else:
            raise ValueError(f"Unexpected coords for {ring=}: {row=}, {col=}")

    assert rotation == 0, rotation
    return row, col


def matrixRotation(matrix: list[int], rotation: int):
    if not matrix:
        return

    rows_count = len(matrix)
    if not rows_count:
        return

    cols_count = len(matrix[0])
    if not cols_count:
        return

    def get_new_value(row: int, col: int) -> int:
        old_row, old_col = computeOldPosition(
            rows_count=rows_count,
            cols_count=cols_count,
            rotation=rotation,
            row=row,
            col=col,
        )
        return matrix[old_row][old_col]

    for row in range(rows_count):
        print(" ".join(str(get_new_value(row, col)) for col in range(cols_count)))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
