import unittest

import NewRunner
from unittest import TestCase


class TournamentTest(TestCase):
    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.sport1 = NewRunner.Runner('Усэйн', 10)
        self.sport2 = NewRunner.Runner('Андрей', 9)
        self.sport3 = NewRunner.Runner('Ник', 3)

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @classmethod
    def tearDownClass(self):
        print(self.all_results)


    def test_start1(self):
        self.etap1 = NewRunner.Tournament(90, self.sport1, self.sport3)
        self.a = self.etap1.start()
        for key in self.a:
            self.all_results[key] = self.a[key].name
        self.tearDownClass()
        self.assertTrue(self.a[max(self.a)] == "Ник")

    def test_start2(self):
        self.etap2 = NewRunner.Tournament(90, self.sport2, self.sport3)
        self.b = self.etap2.start()
        for key in self.b:
            self.all_results[key] = self.b[key].name
        self.tearDownClass()
        self.assertTrue(self.b[max(self.b)] == 'Ник')

    def test_start3(self):
        self.etap3 = NewRunner.Tournament(90, self.sport1, self.sport2, self.sport3)
        self.c = self.etap3.start()
        for key in self.c:
            self.all_results[key] = self.c[key].name
        self.assertTrue(self.c[max(self.c)] == 'Ник')


if __name__ == 'main':
    TestCase.main()
