import unittest
from runner_and_tournament import Runner, Tournament
from pprint import pprint

class TournamentTest(unittest.TestCase):
    def setUp(self):
        """
        Бегун по имени Усэйн, со скоростью 10.
        Бегун по имени Андрей, со скоростью 9.
        Бегун по имени Ник, со скоростью 3.
        """
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    def tearDown(self):
        pprint(self.all_results)

    def test_tournament_1(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    def test_tournament_2(self):
        self.tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

    def test_tournament_3(self):
        self.tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[len(self.all_results)] == "Ник")

