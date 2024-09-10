import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        self.Bob_ = runner.Runner("Bob")
        for _ in range(10): self.Bob_.walk()
        self.assertEqual(self.Bob_.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        self.Alex_ = runner.Runner("Alex")
        for _ in range(10): self.Alex_.run()
        self.assertEqual(self.Alex_.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.Karl_, self.Ivan_ = runner.Runner("Karl"), runner.Runner("Ivan")
        for _ in range(10): self.Karl_.walk(); self.Ivan_.run()
        self.assertNotEqual(self.Karl_.distance, self.Ivan_.distance)


if __name__ == "__main__":
    unittest.main()