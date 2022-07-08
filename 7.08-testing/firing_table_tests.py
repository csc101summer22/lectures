# Tests trajectories of cannonballs.

# Unit tests can be written in Python using the unittest module:
import unittest
import firing_table

# For now, just treat this as necessary boilerplate:
class TestFiringTable(unittest.TestCase):
    # Each test case is a function whose name starts with "test" and whose
    #  lone parameter is "self":
    def test01_time_of_flight(self):
        time = firing_table.time_of_flight(50)
        # Each test case should include at least one "assertion"; note that,
        #  by default, floats will be checked to the seventh decimal place:
        self.assertAlmostEqual(time, 3.1927543)

    def test02_time_of_flight(self):
        time = firing_table.time_of_flight(0)
        self.assertAlmostEqual(time, 0)


if __name__ == "__main__":
    unittest.main()
