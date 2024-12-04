import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        first = Runner('Alex')
        for i in range(10):
            first.walk()
        self.assertEqual(first.distance, 50)

    def test_run(self):
        second = Runner('Anna')
        for i in range(10):
            second.run()
        self.assertEqual(second.distance, 100)

    def test_challenge(self):
        third = Runner('Ben')
        forth = Runner('Scarlet')
        for i in range(10):
            third.walk()
            forth.run()
        self.assertNotEqual(third.distance, forth.distance)


if __name__ == '__main__':
    unittest.main()