import unittest
from module_12_1_ import RunnerTest
from module_12_2_ import TournamentTest


wow_suite = unittest.TestSuite()
wow_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
wow_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(wow_suite)