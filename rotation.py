#!/bin/python3


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


def computeOldPosition(
    rows: int, cols: int, rotation: int, r: int, c: int
) -> tuple[int, int]:
    ring = computeRing(rows, cols, r, c)
    while rotation > 0:
        if r == ring:
            if c == cols - 1 - ring:
                r, rotation = goDown(rotation=rotation, r=r, rows=rows, ring=ring)
            else:
                c, rotation = goRight(rotation=rotation, c=c, cols=cols, ring=ring)
        elif r == rows - 1 - ring:
            if c == ring:
                r, rotation = goUp(rotation=rotation, r=r, ring=ring)
            else:
                c, rotation = goLeft(rotation=rotation, c=c, ring=ring)
        elif c == ring:
            r, rotation = goUp(rotation=rotation, r=r, ring=ring)
        elif c == cols - 1 - ring:
            r, rotation = goDown(rotation=rotation, r=r, rows=rows, ring=ring)
        else:
            raise ValueError(f"Unexpected coords for {ring=}: {r=}, {c=}")

    assert rotation == 0, rotation
    return r, c


def matrixRotation(matrix: list[int], rotation: int):
    if not matrix:
        return

    rows = len(matrix)
    if not rows:
        return

    cols = len(matrix[0])
    if not cols:
        return

    def get_new_value(r: int, c: int) -> int:
        old_r, old_c = computeOldPosition(
            rows=rows, cols=cols, rotation=rotation, r=r, c=c
        )
        return matrix[old_r][old_c]

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
