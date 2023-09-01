import os
import sys

# Add the parent directory (project root) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-1, -1) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 5) == -5
    assert calculator.multiply(0, 100) == 0

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(10, 2) == 5
