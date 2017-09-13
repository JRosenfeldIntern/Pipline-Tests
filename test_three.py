import unittest


class TestThree(unittest.TestCase):
    def test_greater(self):
        self.assertGreater(5, 4)

    def test_less(self):
        self.assertLess(4, 5)

    def test_less_equal(self):
        self.assertLessEqual(3, 3)

    def test_not_equal(self):
        self.assertNotEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
