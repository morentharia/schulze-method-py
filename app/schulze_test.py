import pytest

from schulze import schulze_method

@pytest.mark.parametrize("test_input,expected", [
    (
        [
            {"count": 40, "ballot": [["X"], ["c", "b", "e"]]},
            {"count": 20, "ballot": [["c"], ["b", "e"], ["X"]]},
            {"count": 20, "ballot": [["b"], ["c", "e"], ["X"]]},
            {"count": 20, "ballot": [["e"], ["c", "b"], ["X"]]},
        ],
        [['b', 'c', 'e'], ['X']],
    ),
    (
        [
            {"count": 50, "ballot": [["X"], ["c", "b", "e"]]},
            {"count": 20, "ballot": [["c"], ["b", "e"], ["X"]]},
            {"count": 20, "ballot": [["b"], ["c", "e"], ["X"]]},
            {"count": 10, "ballot": [["e"], ["c", "b"], ["X"]]},
        ],
        [['X', 'b', 'c', 'e']],
    ),
    (
        [
            {"count": 50, "ballot": [["X"], ["c", "b", "e"]]},
            {"count": 20, "ballot": [["c", "b", "e"], ["X"]]},
            {"count": 20, "ballot": [["b", "c", "e"], ["X"]]},
            {"count": 10, "ballot": [["e", "c", "b"], ["X"]]},
        ],
        [['X', 'b', 'c', 'e']],
    ),
    (
        [
            {"count": 49, "ballot": [["X"], ["c", "b", "e"]]},
            {"count": 21, "ballot": [["c"], ["b", "e"], ["X"]]},
            {"count": 19, "ballot": [["b"], ["c", "e"], ["X"]]},
            {"count": 10, "ballot": [["e"], ["c", "b"], ["X"]]},
        ],
        [['c'], ['b'], ['e'], ['X']],
    ),

    # Example from: https://en.wikipedia.org/wiki/Schulze_method
    (
        [
            {"count": 5, "ballot": [["a"], ["c"], ["b"], ["e"], ["d"]]},
            {"count": 5, "ballot": [["a"], ["d"], ["e"], ["c"], ["b"]]},
            {"count": 8, "ballot": [["b"], ["e"], ["d"], ["a"], ["c"]]},
            {"count": 3, "ballot": [["c"], ["a"], ["b"], ["e"], ["d"]]},
            {"count": 7, "ballot": [["c"], ["a"], ["e"], ["b"], ["d"]]},
            {"count": 2, "ballot": [["c"], ["b"], ["a"], ["d"], ["e"]]},
            {"count": 7, "ballot": [["d"], ["c"], ["e"], ["b"], ["a"]]},
            {"count": 8, "ballot": [["e"], ["b"], ["a"], ["d"], ["c"]]},
        ],
        [['e'], ['a'], ['c'], ['b'], ['d']],
    ),
    (
        # Example from: http://condorcet.ericgorr.net/
        [
            {"count": 12, "ballot": [[0], [3], [2], [1]]},
            {"count": 3, "ballot": [[1], [0], [2], [3]]},
            {"count": 25, "ballot": [[1], [2], [0], [3]]},
            {"count": 21, "ballot": [[2], [1], [0], [3]]},
            {"count": 12, "ballot": [[3], [0], [1], [2]]},
            {"count": 21, "ballot": [[3], [0], [2], [1]]},
            {"count": 6, "ballot": [[3], [1], [0], [2]]},
        ],
        [[1, 2], [0], [3]],
    ),
    (
        [
            {"count": 280, "ballot": [[0], [2], [3], [1]]},
            {"count": 301, "ballot": [[1], [0], [2], [3]]},
            {"count": 303, "ballot": [[2], [1], [3], [0]]},
            {"count": 356, "ballot": [[3], [0], [1], [2]]},
        ],
        [[1], [0], [2], [3]],
    ),

])


def test_schulze_method(test_input, expected):
    assert schulze_method(test_input) == expected
