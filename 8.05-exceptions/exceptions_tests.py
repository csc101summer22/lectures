import unittest
import exceptions


class TestExceptions(unittest.TestCase):
    def test01_foo(self):
        # Unittests can be set up to expect specific exceptions -- if the
        #  exception is raised, then the test passes:
        with self.assertRaises(Exception):
            exceptions.foo()

    def test02_bar(self):
        # ...if no exception is raised, then the test fails; if a different
        #  exception is raised, then it is left unhandled:
        with self.assertRaises(ValueError):
            exceptions.bar()


if __name__ == "__main__":
    unittest.main()
