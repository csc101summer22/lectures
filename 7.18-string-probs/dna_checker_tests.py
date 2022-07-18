# Tests checking DNA strands.

import unittest
import dna_checker

class TestDNAChecker(unittest.TestCase):
    def test01_check_base(self):
        match = dna_checker.check_bases("A", "T")
        self.assertTrue(match)

    def test02_check_base(self):
        match = dna_checker.check_bases("C", "G")
        self.assertTrue(match)

    def test03_check_base(self):
        match = dna_checker.check_bases("A", "G")
        self.assertFalse(match)

    def test04_check_strands(self):
        match = dna_checker.check_strands("TACGCTTA", "ATGCGAAT")
        self.assertTrue(match)

    def test05_check_strands(self):
        match = dna_checker.check_strands("TACGCTTA", "ATGCAAAT")
        self.assertFalse(match)


if __name__ == "__main__":
    unittest.main()
