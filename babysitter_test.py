import unittest


class TestBabysitter(unittest.TestCase):
    def setUp(self):
        pass

    def test__first_failing_test(self):
        self.assertEquals(True, False, "first test")




if __name__ == "__main__":
    unittest.main()
