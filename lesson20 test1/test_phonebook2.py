import unittest


class testPhonebook2(unittest.TestCase):

    def test_first_name_add_f(self):
        exspected_name = 'Oleg' #???????
        self.assertEqual(exspected_name, 'Oleg')