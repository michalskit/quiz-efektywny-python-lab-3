# Zadanie 1
# Napisz funkcję join_strings, która przyjmuje listę 
# ciągów znaków i łączy je w jeden ciąg, dodając 
# między nimi podany separator. Funkcja powinna 
# przyjmować dwa argumenty: listę ciągów znaków i ciąg 
# znaków będący separatorem, a zwracać jeden ciąg znaków.

def join_strings(string_list, separator):
    pass

# Przykład użycia:
# print(join_strings(['informatyka', 'test', 'łączenie'], ' - '))
# Powinno zwrócić: 'informatyka - test - łączenie'

# Zadanie 2
# Zmień poniższą funkcję na jej wersję wykorzystującą 
# list comprehension. Funkcja powinna generować i 
# zwracać listę kwadratów liczb od 0 do n.

def squares(n):
    """Zwraca listę kwadratów liczb od 0 do n"""
    result = []
    for i in range(n+1):
        result.append(i*i)
    return result

# Wersja z list comprehension:
def squares_comprehension(n):
    pass

# Zadanie 3
# Napisz funkcję rekurencyjną, która oblicza sumę 
# cyfr danej liczby całkowitej. Funkcja powinna 
# przyjmować jeden argument - liczbę całkowitą - 
# i zwracać sumę jej cyfr.

def sum_of_digits(n):
    pass

# Przykład użycia:
# print(sum_of_digits(12345))
# Powinno zwrócić: 15


