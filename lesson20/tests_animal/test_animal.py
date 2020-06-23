import unittest
from lesson20.animal import Animal


class testAnimal(unittest.TestCase):

    def test_name_str(self):
        expected_nikname = 'Lord'
        test_dog = Animal('Pekingese', expected_nikname, 5)
        actual_animal = test_dog.getNikname()
        self.assertEqual(actual_animal, expected_nikname)

    def test_breed(self):
        expected_breed = 'Pekingese'
        test_dog = Animal(expected_breed, 'Lord', 5)
        actual_animal = test_dog.getBreed()
        self.assertEqual(actual_animal, expected_breed)

    def test_age_int(self):
        expected_age = 5
        test_dog = Animal('Pekingese', 'Lord', expected_age)
        actual_animal = test_dog.getAge()
        self.assertEqual(actual_animal, expected_age)

    def test_str_age_int(self):
        expected_age = 5
        test_dog = Animal('Pekingese', 'Lord', str(expected_age))
        actual_animal = test_dog.getAge()
        self.assertEqual(actual_animal, expected_age)

    def test_age_raise(self):
        with self.assertRaises(ValueError) as context:
            test_dog = Animal('Pekingese', 'Lord', 'expected_age')
        self.assertEqual('age must be int', context.exception)


if __name__ == '__main__':
    unittest.main()
