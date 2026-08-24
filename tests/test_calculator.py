import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_with_floats(self):
        assert add(2.5, 3.5) == 6.0

    def test_add_with_mixed_types(self):
        assert add(2, 3.5) == 5.5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_with_floats(self):
        assert subtract(5.5, 2.5) == 3.0

    def test_subtract_with_mixed_types(self):
        assert subtract(5, 2.5) == 2.5

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(4, 5) == 20

    def test_multiply_with_floats(self):
        assert multiply(2.5, 4.0) == 10.0

    def test_multiply_with_mixed_types(self):
        assert multiply(2, 3.5) == 7.0

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-4, -5) == 20


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_with_floats(self):
        assert divide(10.0, 2.0) == 5.0

    def test_divide_with_mixed_types(self):
        assert divide(10, 2.5) == 4.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5.0

    def test_divide_with_fractional_result(self):
        result = divide(5, 2)
        assert abs(result - 2.5) < 1e-9
