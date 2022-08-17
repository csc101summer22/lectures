import unittest
import maximum_v1 as v1
import maximum_v2 as v2


class TestMaximum(unittest.TestCase):
    def test01(self):
        lst = [2, -1, 9, 8, 5, -3, 0, 8]
        self.assertEqual(v1.max_element(lst), 9)
        self.assertEqual(v2.max_element(lst), 9)

    def test02(self):
        lst = [2, -1, 7, 8, 5, -3, 0, 8]
        self.assertEqual(v1.max_element(lst), 8)
        self.assertEqual(v2.max_element(lst), 8)

    # NOTE: The above tests are definitely not enough tests -- they do not have
    #       100% coverage, indicating that they don't even test every line of
    #       code, let alone every possible edge case.

    def test03(self):
        lst = []
        self.assertEqual(v1.max_element(lst), None)
        self.assertEqual(v2.max_element(lst), None)


if __name__ == "__main__":
    unittest.main()
