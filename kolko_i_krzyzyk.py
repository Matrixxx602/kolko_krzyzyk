## Pseodokod

# Wyświetla instrukcję gry
# Wybiera kto pierwszy zaczyna
# Tworzy plansze do gry
# Pokazuje plansze
# Pętla while, dotąd aż ktoś nie wygral albo zremisował
#   Jeśli ruch jest po stronie gracza
#       Odczytuje ruch gracza
#       Nanosi ruch na plansze
#   Jeśli jest inaczej
#       Wyznacza ruch komputera
#       Nanosi ruch na plansze
#   Pokazuje plansze
#   Zmienia gracza

def display_instruct():
    print('''
Witaj w grze "Kółko i krzyżyk". Twoim zadaniem jest umieszczenie trzech takich samych
symboli w jednej lini. Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

                      0 | 1 | 2
                      ---------
                      3 | 4 | 5
                      ---------
                      6 | 7 | 8

Przygotuj się do gry. \n
    ''')

def ask_yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


