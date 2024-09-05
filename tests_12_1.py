import unittest
import runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.Bob_ = runner.Runner("Bob")
        for _ in range(10): self.Bob_.walk()
        self.assertEqual(self.Bob_.distance, 50)

    def test_run(self):
        self.Alex_ = runner.Runner("Alex")
        for _ in range(10): self.Alex_.run()
        self.assertEqual(self.Alex_.distance, 100)

    def test_challenge(self):
        self.Karl_, self.Ivan_ = runner.Runner("Karl"), runner.Runner("Ivan")
        for _ in range(10): self.Karl_.walk(); self.Ivan_.run()
        self.assertNotEqual(self.Karl_.distance, self.Ivan_.distance)


if __name__ == "__main__":
    unittest.main()