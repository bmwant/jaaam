import unittest

from bf import BrainFuck


class TestStringMethods(unittest.TestCase):

    def test_find_matching_closing_bracket(self):
        interpreter = BrainFuck('[--[-]--]')
        cursor = interpreter._find_matching(']', cursor=0)
        self.assertEqual(cursor, 8)

    def test_find_matching_open_bracket(self):
        interpreter = BrainFuck('[--[-]--]')
        cursor = interpreter._find_matching('[', cursor=5)
        self.assertEqual(cursor, 3)

    def test_fail_when_no_matching_closing_bracket(self):
        interpreter = BrainFuck('[--[---]')
        with self.assertRaises(ValueError):
            cursor = interpreter._find_matching(']', cursor=0)

    def test_fail_when_no_matching_open_bracket(self):
        interpreter = BrainFuck('[-]---][---]')
        with self.assertRaises(ValueError):
            cursor = interpreter._find_matching(']', cursor=6)


if __name__ == '__main__':
    unittest.main()
