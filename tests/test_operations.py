# tests/test_operations.py
"""
Unit tests for operations such as exponentiation, square root, absolute value, and cube.
"""

import pytest
from app.operations import exponentiation, square_root, absolute_value, cube


def test_exponentiation_positive():
    """Test positive cases for exponentiation."""
    assert exponentiation(2, 3) == 8
    assert exponentiation(5, 0) == 1
    assert exponentiation(10, 1) == 10

def test_exponentiation_negative():
    """Test negative cases for exponentiation."""
    assert exponentiation(2, -2) == 0.25
    assert exponentiation(-2, 3) == -8

def test_square_root_positive():
    """Test positive cases for square root."""
    assert square_root(16) == 4
    assert square_root(25) == 5
    assert square_root(0) == 0

def test_square_root_negative():
    """Test negative cases for square root."""
    with pytest.raises(ValueError, match="Square root of negative number is not allowed."):
        square_root(-16)

def test_absolute_value():
    """Test cases for absolute value."""
    assert absolute_value(5) == 5
    assert absolute_value(-5) == 5
    assert absolute_value(0) == 0

def test_cube():
    """Test cases for cube."""
    assert cube(3) == 27
    assert cube(-2) == -8
    assert cube(0) == 0
