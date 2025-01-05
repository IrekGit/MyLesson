import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r_w = Runner("nameRunnerWalk")
        for i in range(10):
            r_w.walk()
        self.assertEqual(r_w.distance, 50)

    def test_run(self):
        r_r = Runner("nameRunnerRun")
        for j in range(10):
            r_r.run()
        self.assertEqual(r_r.distance, 100)

    def test_challenge(self):
        r_r = Runner("nameRunner1")
        r_w = Runner("nameRunner2")
        for k in range(10):
            r_r.run()
            r_w.walk()
        self.assertNotEqual(r_r.distance, r_w.distance)


if __name__ == '__main__':
    unittest.main()