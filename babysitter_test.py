import unittest
import babysitter


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        pass

    def test__calculate_returns_zero_if_no_time_is_worked(self):
        total = babysitter.calculate(12, 12, 12)
        self.assertEquals(total, 0, "Calculate did not return 0 when no time was worked.")

    def test__calculate_returns_sixty_four_for_working_midnight_to_four(self):
        total = babysitter.calculate(12, 12, 4)
        self.assertEquals(total, 64, "Working midnight to 4am should be $64.")

    def test__calculate_returns_sixteen_for_working_1_to_2(self):
        total = babysitter.calculate(1, 2, 2)
        self.assertEquals(total, 16, "Working 1am to 2am should be $16.")

    def test__calculate_returns_twelve_for_working_nine_to_ten_with_bedtime_at_ten(self):
        total = babysitter.calculate(9, 10, 10)
        self.assertEquals(total, 12, "Working one hour with kid awake should be $12.")

    def test__calculate_returns_sixteen_for_working_ten_to_midnight_with_bedtime_at_ten(self):
        total = babysitter.calculate(10, 10, 12)
        self.assertEquals(total, 16, "Working two hours before midnight should be $16.")

    def test__calculate_returns_124_for_working_five_to_four_with_bedtime_at_six(self):
        total = babysitter.calculate(5, 6, 4)
        self.assertEquals(total, 124, "Working five to four with bedtime at six should be $124.")

    def test__calculate_returns_sixtyfour_for_working_midnight_to_four_with_two_bedtime(self):
        total = babysitter.calculate(12, 2, 4)
        self.assertEquals(total, 64, "Working midnight to four with bedtime at two should be $64.")

    def test__calculate_returns_fiftysix_for_working_10_to_two_with_one_bedtime(self):
        total = babysitter.calculate(10, 1, 2)
        self.assertEquals(total, 56, "Working ten to two with bedtime at one should be $56.")

    def test__calculate_returns_sixtyfour_for_working_10_to_two_with_eleven_bedtime(self):
        total = babysitter.calculate(10, 11, 2)
        self.assertEquals(total, 52, "Working ten to two with bedtime at eleven should be $52.")

if __name__ == "__main__":
    unittest.main()
