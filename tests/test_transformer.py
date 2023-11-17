import pytest
from gau.transformer import flat


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            {'a': 1, 'b': {'c': 2, 'd': [3, 4]}},
            {'a': 1, 'b.c': 2, 'b.d.0': 3, 'b.d.1': 4}
        ),
        (
            [{'a': 1}, {'b': 2}],
            {'0.a': 1, '1.b': 2}
        ),
        # Add more test cases here
    ]
)
def test_flat(data, expected):
    assert flat(data) == expected
