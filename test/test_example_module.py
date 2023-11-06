"""Test ``example_module.py``."""

import pytest

from reglsq import example_module

ADD_FIXTURES = [
    ((3, 2), 5),
    ((4.5, 1.5), 6.0)
]


@pytest.mark.parametrize("test_input,expected", ADD_FIXTURES)
def test_add(test_input, expected):
    """Test add for integers and floats."""
    result = example_module.add(*test_input)

    assert result == expected
