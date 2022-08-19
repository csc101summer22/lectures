import unittest
import random
import maximum_v1 as v1
import maximum_v2 as v2


class TestMaximum(unittest.TestCase):
    # def test01(self):
    #     lst = [2, -1, 9, 8, 5, -3, 0, 8]
    #     self.assertEqual(v1.max_element(lst), 9)
    #     self.assertEqual(v2.max_element(lst), 9)

    # def test02(self):
    #     lst = [2, -1, 7, 8, 5, -3, 0, 8]
    #     self.assertEqual(v1.max_element(lst), 8)
    #     self.assertEqual(v2.max_element(lst), 8)

    # def test03(self):
    #     lst = []
    #     self.assertEqual(v1.max_element(lst), None)
    #     self.assertEqual(v2.max_element(lst), None)

    # NOTE: The above tests assume that we know all the possible cases. If we
    #       randomly generate inputs instead, it is possible that we might
    #       stumble upon some unforeseen case.

    def test04(self):
        lst = [random.randint(-1000, 1000) for i in range(1000)]
        e1 = v1.max_element(lst)
        e2 = v2.max_element(lst)

        # NOTE: Since the inputs were randomly generated, we don't know
        #       exactly what a correct output will be, but we do know what
        #       must be true of any correct output.

        for element in lst:
            self.assertTrue(e1 >= element)
            self.assertTrue(e2 >= element)

    def test05(self):
        lst = [i for i in range(20000)]
        # self.assertEqual(v1.max_element(lst), 19999)
        self.assertEqual(v2.max_element(lst), 19999)


if __name__ == "__main__":
    unittest.main()
