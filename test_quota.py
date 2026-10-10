import unittest
from quota import remaining_quota


class QuotaTests(unittest.TestCase):
    def test_zero_quota(self):
        self.assertEqual(remaining_quota(0, 0), 0)

    def test_unspecified_quota(self):
        self.assertEqual(remaining_quota(None, 0), 8)

    def test_positive_quota(self):
        self.assertEqual(remaining_quota(5, 2), 3)


if __name__ == "__main__":
    unittest.main()
