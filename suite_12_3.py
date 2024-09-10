import unittest
import tests_12_3_1, tests_12_3_2

tournament_ST = unittest.TestSuite()
tournament_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.RunnerTest))
tournament_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournament_ST)
