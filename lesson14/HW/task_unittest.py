# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.

import unittest
from triangle import triangle

class TestTriangleExist(unittest.TestCase):
    def test1_triangle_exist(self):
        self.assertEqual(triangle(a= 1, b = 1, c = 1), 'equilateral')
        pass

    def test2_triangle_exist(self):
        self.assertEqual(triangle(a= 1, b = 1, c = 2), 'isosceles')
        pass

    def test3_triangle_exist(self):
        self.assertEqual(triangle(a= 4, b = 5, c = 3), 'versatile')
        pass

if __name__ == '__main__':
    unittest.main()
    

