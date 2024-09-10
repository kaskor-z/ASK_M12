import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        # cls.is_frozen = True
        cls.all_results = []

    def setUp(self):
        """
        Бегун по имени Усэйн, со скоростью 10.
        Бегун по имени Андрей, со скоростью 9.
        Бегун по имени Ник, со скоростью 3.
        """
        # self.is_frozen = True
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)
        self.search_name = "Ник"

    @classmethod
    def tearDownClass(cls):
        for i, result in enumerate(cls.all_results, 1):
            print(f'Тест №{i}. {result}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        result = tournament.start()
        self.assertTrue(result[len(result)] == self.search_name)
        TournamentTest.all_results.append(result)

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        result = tournament.start()
        self.assertTrue(result[len(result)] == self.search_name)
        self.all_results.append(result)

    @unittest.skipIf(True, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament.start()
        self.assertTrue(result[len(result)] == self.search_name)
        self.all_results.append(result)

