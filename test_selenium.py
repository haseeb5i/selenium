import unittest


def setUpModule():
    # will run once for this module, at the begining
    # which includes one or many classes for tests
    print("setUpModule")


def tearDownModule():
    # will run once for this module, at the end
    # which includes one or many classes for tests
    print("tearDownModule")


class SeleniumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # this runs only once for this class in the begining
        print("setting up the testing environment\n")

    @classmethod
    def tearDownClass(cls):
        # this runs only once for this class at the end
        print("\nclosing up the testing environment")

    @classmethod
    def setUp(self):
        # this runs once before every test mehod
        print("setting up login for the test")

    @classmethod
    def tearDown(self):
        # this runs after for ever test mehtod
        print("logging out after test\n")

    def test_search(self):
        print("Running serach test")
        # unit test assertions defines the criteria of passing or failing the test
        # by using different assertions, we can define different check cases with different messages
        num = 1
        # assert that num is equl to one to pass the test
        # there is a whole list of assertions to check
        # some importnat assertions are, usually first assert_op second order
        # assertEqual and assertNotEqual
        # assertTrue and assertFalse
        # assertIsNone and assertIsNotNone
        # assertIn and assertNotIn
        # assertGreater, assertGreaterEqual, assertLess, assertLessEqual
        self.assertEqual(num, 1, "number not equal to 1")

    def test_advanced_search(self):
        print("Running advanced serach test")

    @unittest.SkipTest
    def test_login(self):
        # these decoractore allow us to skip specific tests
        # @unittest.skip("skip message")
        # @unittest.skipIf(a==0, "a is not zero err message")
        print("Running login test")


class ExtraTests(unittest.TestCase):

    def test_extra(self):
        print("running an extra test method")


if __name__ == '__main__':
    # we can organise our test cases in test suites by loading them seperately
    # tc1 = unittest.TestLoader().loadTestsFromTestCase(SeleniumTests)
    # tc2 = unittest.TestLoader().loadTestsFromTestCase(ExtraTests)
    # a test suite is a list of different test cases
    # master_suite = unittest.TestSuite([tc1, tc2])
    # now run these tests using different log levels
    # unittest.TextTestRunner(verbosity=2).run(master_suite)
    unittest.main()
