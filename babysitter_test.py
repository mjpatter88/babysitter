import unittest


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        pass

    def test__calculate_returns_zero_if_no_time_is_worked(self):
        total = babysitter.calculate(12, 12)
        self.assertEquals(total, 0, "Calculate did not return 0 when no time was worked.")




if __name__ == "__main__":
    unittest.main()
