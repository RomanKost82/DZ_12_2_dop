import unittest
from utils.arrs import get, my_slice


class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, 'test'), 2)
        self.assertEqual(get([1, 2, 3], 0, 'test'), 1)
        self.assertEqual(get([], 0, 'test'), 'test')
        self.assertEqual(get([1, 2, 3], -1, 'tests'), 'tests')
        self.assertEqual(get([1, 2, 3], 5, 'tests'), 'tests')

    def test_my_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4], end=-2), [1, 2])
        self.assertEqual(my_slice([1, 2, 3, 4], 2, 1), [])
        self.assertEqual(my_slice([1, 2, 3, 4], end=6), [1, 2, 3, 4])
        self.assertEqual(my_slice([], 1, 3), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -10, 10), [1, 2, 3, 4])


# if __name__ == '__main__':
#     unittest.main()
