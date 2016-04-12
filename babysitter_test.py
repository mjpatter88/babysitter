import unittest
import babysitter


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        pass

    def test__calculate_returns_zero_if_no_time_is_worked(self):
        total = babysitter.calculate(12, 12)
        self.assertEquals(total, 0, "Calculate did not return 0 when no time was worked.")

    def test__calculate_returns_sixty_four_for_working_midnight_to_four(self):
        total = babysitter.calculate(12, 4)
        self.assertEquals(total, 64, "Working midnight to 4am should be $64.")

if __name__ == "__main__":
    unittest.main()
