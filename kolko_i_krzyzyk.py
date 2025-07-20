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
        computer = X
        human = O
    return computer, human

# Funkcja tworzy nową pustą plansze do gry.
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

# Funkcja wyświetla plansze do gry.
def display_board(board):
    print("\n\t\t", board[0], "|", board[1], "|", board[2])
    print("\t\t---------")
    print("\n\t\t", board[3], "|", board[4], "|", board[5])
    print("\t\t---------")
    print("\n\t\t", board[6], "|", board[7], "|", board[8], "\n")

# Funkcja zwraca listę dozwolonych ruchów w turze.
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

# Funkcja zwraca wyngrany żeton (X lub O), remis (TIE) lub nic (None), aby określić wynik gry.
def winner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        
    if EMPTY not in board:
        return TIE

    return None

# Funkcja zwraca numer pola, w którym gracz chce umieścić żeton.
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twoj ruch? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte. Wybierz inne.\n")
    print("Dobrze...")
    return move

# Funkcja zwraca numer pola, w którym komputer umieści swój ruch.
def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer...", end=" ")

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
        
# Funkcja zmienia gracza po wykonaniu ruchu.
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
    
# Funkcja zwraca wynik końcowy gry.
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(f"{the_winner} jest zwyciężcą!\n")
    else:
        print("REMIS!\n")

    if the_winner == computer:
        print("Komputer wygrał!")
    elif the_winner == human:
        print("Wygrałeś! Gratulacje!")
    else:
        print("Miałeś mnóstwo szcześcia, niełatwo jest zremisować, a co dopiero wygrać z komputerem!")

# Funkcja głowna, która steruje całą grą.
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)



# Rozpoczęcie gry
main()
input("\n\nAby zakończyć grę, naciśnij klawisz ENTER.")