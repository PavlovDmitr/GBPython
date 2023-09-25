import pytest
from triangle import triangle


def test_one_triangle_exist():
    assert triangle(a= 1, b = 1, c = 1) == 'equilateral', 'test 1 fail'

def test_two_triangle_exist():
    assert triangle(a= 1, b = 1, c = 2) == 'isosceles', 'test 2 fail'

def test_three_triangle_exist():
    assert triangle(a= 4, b = 5, c = 3) == 'versatile', 'test 3 fail'


if __name__ == '__main__':
    pytest.main()