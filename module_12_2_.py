import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        #self.runner_irek = Runner("Ирек", speed=11)
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for test_num, results in sorted(cls.all_results.items()):
            print(f'Результаты забега № {test_num}:')
            for place_, name_ in results.items():
                print(f' {place_} место - {name_}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[1] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[2] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[3] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    '''
    def test_irek_usain_andrey_and_nick(self):
        tournament = Tournament(100, self.runner_irek, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results[4] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")
    '''
if __name__ == "__main__":
    unittest.main()