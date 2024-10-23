#!/bin/python3

from functools import partial


def computeRing(rows: int, cols: int, r: int, c: int) -> int:
    return min(r, c, rows - 1 - r, cols - 1 - c)


def goLeft(rotation: int, c: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, c - ring)
    c -= shift
    rotation -= shift
    return c, rotation


def goRight(rotation: int, c: int, cols: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, cols - 1 - ring - c)
    c += shift
    rotation -= shift
    return c, rotation


def goUp(rotation: int, r: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, r - ring)
    r -= shift
    rotation -= shift
    return r, rotation


def goDown(rotation: int, r: int, rows: int, ring: int) -> tuple[int, int]:
    shift = min(rotation, rows - 1 - ring - r)
    r += shift
    rotation -= shift
    return r, rotation


def computeNewSingleMapping(
    rows: int, cols: int, rotation: int, r: int, c: int
) -> tuple[int, int]:
    ring = computeRing(rows, cols, r, c)
    while rotation > 0:
        if r == ring:
            if c == ring:
                r, rotation = goDown(rotation=rotation, r=r, rows=rows, ring=ring)
            else:
                c, rotation = goLeft(rotation=rotation, c=c, ring=ring)
        elif r == rows - 1 - ring:
            if c == cols - 1 - ring:
                r, rotation = goUp(rotation=rotation, r=r, ring=ring)
            else:
                c, rotation = goRight(rotation=rotation, c=c, cols=cols, ring=ring)
        elif c == ring:
            r, rotation = goDown(rotation=rotation, r=r, rows=rows, ring=ring)
        elif c == cols - 1 - ring:
            r, rotation = goUp(rotation=rotation, r=r, ring=ring)
        else:
            raise ValueError(f"Unexpected coords for {ring=}: {r=}, {c=}")

    assert rotation == 0, rotation
    return r, c


# new to old
def computeNewMappings(
    rows: int, cols: int, rotation: int
) -> dict[tuple[int, int], tuple[int, int]]:
    compute_mapping = partial(
        computeNewSingleMapping, rows=rows, cols=cols, rotation=rotation
    )
    return {compute_mapping(r=r, c=c): (r, c) for r in range(rows) for c in range(cols)}


def matrixRotation(matrix: list[int], rotation: int):
    if not matrix:
        return

    rows = len(matrix)
    if not rows:
        return

    cols = len(matrix[0])
    if not cols:
        return

    new_position = computeNewMappings(rows, cols, rotation)

    def get_new_value(r: int, c: int) -> int:
        rn, cn = new_position[(r, c)]
        return matrix[rn][cn]

    for r in range(rows):
        print(" ".join(str(get_new_value(r, c)) for c in range(cols)))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
