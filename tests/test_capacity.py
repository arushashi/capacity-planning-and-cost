import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import capacity as c  # noqa: E402


class CapacityTests(unittest.TestCase):
    def test_basic(self):
        # usable per instance = 150 * 0.7 = 105; 1200/105 = 11.43 -> 12; +1 redundancy = 13
        self.assertEqual(c.instances_needed(1200, 150, 0.3, 1), 13)

    def test_no_headroom_no_redundancy(self):
        self.assertEqual(c.instances_needed(300, 100, 0.0, 0), 3)

    def test_zero_load(self):
        self.assertEqual(c.instances_needed(0, 100, 0.3, 1), 1)

    def test_forecast_growth(self):
        points = list(c.forecast(100, 0.10, 2))
        self.assertAlmostEqual(points[2][1], 121.0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            c.instances_needed(100, 0)
        with self.assertRaises(ValueError):
            c.instances_needed(100, 10, headroom=1)


if __name__ == "__main__":
    unittest.main()
