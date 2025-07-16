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

# Stałe
X = "X"
O = "O"
EMPTY = " "
TIE = "REMIS"
NUM_SQUARES = 9

# Funkcja wyświetla instrukcje gry.
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

# Funkcja zadaje pytanie, na które można odpowiedzieć "t"(tak) lub "n"(nie).
def ask_yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

# Funkcja prosi o podanie liczby z pewnego zakresu.
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

# Funkcja pyta gracza czy chce zaczynać pierwszy i przypisuje wybór żetonu (X albo O).
def pieces():
    go_first = ask_yes_no("Czy chcesz pierwszy zacząć gre? (t/n): ")
    if go_first == "t":
        print("Pierwszy ruch należy do Ciebie...")
        human = X
        computer = O
    else:
        print("Pierwszy rozpoczyna komputer...")
        human = O
        computer = X
    return human, computer

# Funkcja tworzy nową pustą plansze do gry.
# new_board()