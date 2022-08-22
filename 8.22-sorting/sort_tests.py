import unittest
import random
import sort


class TestSort(unittest.TestCase):
    # def test01(self):
    #     lst = [2, -1, 9, 8, 5, -3, 0, 8]
    #     lst = sort.sort(lst)
    #     self.assertEqual(lst, [-3, -1, 0, 2, 5, 8, 8, 9])

    # def test02(self):
    #     lst = []
    #     lst = sort.sort(lst)
    #     self.assertEqual(lst, [])

    # def test03(self):
    #     lst = [1]
    #     lst = sort.sort(lst)
    #     self.assertEqual(lst, [1])

    # def test04(self):
    #     lst = [-3, -1, 0, 2, 5, 8, 8, 9]
    #     lst = sort.sort(lst)
    #     self.assertEqual(lst, [-3, -1, 0, 2, 5, 8, 8, 9])

    def test05(self):
        lst = [random.randint(-5000, 5000) for i in range(25000)]

        # lst = sort.sort(lst)
        lst.sort()

        for i in range(len(lst) - 1):
            self.assertTrue(lst[i] <= lst[i + 1])


if __name__ == "__main__":
    unittest.main()
