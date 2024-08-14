import unittest

import Runner
from unittest import TestCase


class RunnerTest(TestCase):
    @unittest.skipIf(False, 'Тест исполняется')
    def test_walk(self):
        self.sport = Runner.Runner('Ed')
        for i in range(10):
            self.sport.walk()
        self.assertEqual(self.sport.distance, 50)

    def test_run(self):
        self.sport = Runner.Runner('Jon')
        for i in range(10):
            self.sport.run()
        self.assertEqual(self.sport.distance, 100)

    def test_challenge(self):
        self.sport1 = Runner.Runner('Max')
        self.sport2 = Runner.Runner('Vic')
        for i in range(10):
            self.sport1.run()
            self.sport2.walk()
        self.assertNotEqual(self.sport1.distance, self.sport2.distance)



if __name__ == 'main':
    TestCase.main()
