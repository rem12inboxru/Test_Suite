import unittest
import TestRunner
import TestRunner2

superTest = unittest.TestSuite()
superTest.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRunner.RunnerTest))
superTest.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRunner2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(superTest)