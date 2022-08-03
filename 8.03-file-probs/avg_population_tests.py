import unittest
import os
import avg_population


class TestAveragePopulation(unittest.TestCase):
    def test01_parse_row(self):
        pops = {"West": [5, 1]}
        avg_population.parse_row("California,West,39538223", pops)
        self.assertEqual(pops, {"West": [39538228, 2]})

    def test02_parse_row(self):
        pops = {"East": [5, 1]}
        avg_population.parse_row("California,West,39538223", pops)
        self.assertEqual(pops, {"East": [5, 1], "West": [39538223, 1]})

    def test03_read_file(self):
        # NOTE: Files persist after programs terminate. Tests of functions that
        #       operate on files need to make sure they create fresh copies of
        #       their test files, otherwise earlier tests could potentially
        #       affect the running of later tests.
        with open("test.csv", "w") as csv:
            csv.write("State,Region,Population\n")
            csv.write("California,West,39538223\n")
            csv.write("Hawaii,West,1455271\n")

        pops = avg_population.read_file("test.csv")
        self.assertEqual(pops, {"West": [40993494, 2]})

        os.remove("test.csv")


if __name__ == "__main__":
    unittest.main()
