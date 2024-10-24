from .rotation import matrix_rotation, compute_ring_size
import pytest

# Most of these test cases come from https://www.hackerrank.com/challenges/matrix-rotation-algo/problem


def test_compute_ring_size_one_cell_matrix():
    assert compute_ring_size(rows_count=1, cols_count=1, ring=0) == 1


def test_compute_ring_size_one_element_matrix():
    assert compute_ring_size(rows_count=1, cols_count=2, ring=0) == 2


def test_4_4_matrix():
    # Given
    matrix = [[4 * i + j + 1 for j in range(4)] for i in range(4)]

    # When
    output = []
    matrix_rotation(matrix=matrix, rotation=2, output_sink=output.append)

    # Then
    assert output == ["3 4 8 12", "2 11 10 16", "1 7 6 15", "5 9 13 14"]


def test_5_4_matrix():
    # Given
    matrix = [
        [1, 2, 3, 4],
        [7, 8, 9, 10],
        [13, 14, 15, 16],
        [19, 20, 21, 22],
        [25, 26, 27, 28],
    ]

    # When
    output = []
    matrix_rotation(matrix=matrix, rotation=7, output_sink=output.append)

    # Then
    assert output == [
        "28 27 26 25",
        "22 9 15 19",
        "16 8 21 13",
        "10 14 20 7",
        "4 3 2 1",
    ]


def test_zero_rotation():
    # Given
    matrix = [[4 * i + j + 1 for j in range(4)] for i in range(4)]

    # When
    output = []
    matrix_rotation(matrix=matrix, rotation=0, output_sink=output.append)

    # Then
    matrix_str = [list(map(str, row)) for row in matrix]
    assert output == [" ".join(row) for row in matrix_str]


def test_none_matrix():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=None, rotation=10)


def test_none_rotation():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=[[1]], rotation=None)


def test_negative_rotation():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=None, rotation=-1)


def test_empty_matrix():
    # Given
    matrix = [[]]

    # When
    output = []
    matrix_rotation(matrix=matrix, rotation=5, output_sink=output.append)

    # Then
    assert not output


def test_one_element_matrix():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=[[1]], rotation=2)


def test_one_row_matrix():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=[[1, 2]], rotation=2)


def test_one_col_matrix():
    with pytest.raises(ValueError):
        matrix_rotation(matrix=[[1], [2]], rotation=2)
