import unittest
import logging
from module_12_ import Runner

logging.basicConfig(level=logging.INFO, filename='runner_tests.log',filemode='w', encoding='utf-8',
    format='%(asctime)s - %(levelname)s: %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r_w = Runner("RunnerTest", -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
        else:
            r_w.walk()
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            r_r = Runner(12345)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            r_r.run()
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()