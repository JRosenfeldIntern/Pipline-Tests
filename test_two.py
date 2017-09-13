import unittest


class Josh(object):
    def __init__(self):
        self.employed = False
        self.student = True
        self.rich = False
        self.lucky = True


class TestTwo(unittest.TestCase):
    def test_employed(self):
        josh = Josh()
        self.assertTrue(josh.employed)

    def test_student(self):
        josh = Josh()
        self.assertIs(josh.student, True)

    def test_rich(self):
        josh = Josh()
        self.assertIs(josh.rich, False)

    def test_lucky(self):
        josh = Josh()
        self.assertIs(josh.lucky, True)

if __name__ == '__main__':
    unittest.main()


