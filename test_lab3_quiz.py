import unittest
from lab3_quiz import join_strings, squares_comprehension, sum_of_digits


class TestStringMethods(unittest.TestCase):

    # Zadanie 1: Łączenie ciągów znaków
    def test_join_strings(self):
        self.assertEqual(join_strings(['informatyka', 'test', 'łączenie'], ' - '), 'informatyka - test - łączenie')
        self.assertEqual(join_strings(['one', 'two', 'three'], ','), 'one,two,three')
        self.assertEqual(join_strings([], ','), '')  # testowanie przypadku z pustą listą

    # Zadanie 2: Comprehensions
    def test_squares(self):
        self.assertEqual(squares_comprehension(4), [0, 1, 4, 9, 16])
        self.assertEqual(squares_comprehension(0), [0])  # testowanie przypadku z zerem
        # Sprawdzenie, czy użyto list comprehension
        import inspect
        lines = inspect.getsource(squares_comprehension).split('\n')
        self.assertTrue(any('[' in line and 'for' in line in line for line in lines))

    # Zadanie 3: Rekurencja
    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits(12345), 15)
        self.assertEqual(sum_of_digits(9876), 30)
        self.assertEqual(sum_of_digits(0), 0)  # testowanie przypadku z zerem
        self.assertEqual(sum_of_digits(101010), 3)  # testowanie przypadku z powtarzającymi się liczbami


if __name__ == '__main__':
    unittest.main()
