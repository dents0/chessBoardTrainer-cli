"""
A chess board trainer
---------------------
This program represents a set of exercises which aim to help to memorize the 
chess board.

Author: Deniss Tsokarev
Date: February 21, 2020
Link: https://github.com/dents0/chessBoardTrainer-cli.git

"""


from random import choice


# Board squares
squares = [
            [letter + str(num) for num in [1, 2, 3, 4, 5, 6, 7, 8]]
            for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
          ]
# Square colors row by row
colors = [['black', 'white', 'black', 'white', 'black', 'white', 'black', 'white'] if num%2!=0 else ['white', 'black', 'white', 'black', 'white', 'black', 'white', 'black'] for num in range(1,9)]
# Square:Color pairs
square_colors = dict(zip([item for sublist in squares for item in sublist], [item for sublist in colors for item in sublist]))
# Board diagonals
diagonals = [
                'g1-h2',
                'f1-g2-h3',
                'e1-f2-g3-h4',
                'd1-e2-f3-g4-h5',
                'c1-d2-e3-f4-g5-h6',
                'b1-c2-d3-e4-f5-g6-h7',
                'a1-b2-c3-d4-e5-f6-g7-h8',
                'a2-b3-c4-d5-e6-f7-g8',
                'a3-b4-c5-d6-e7-f8',
                'a4-b5-c6-d7-e8',
                'a5-b6-c7-d8',
                'a6-b7-c8',
                'a7-b8',
                
                'a2-b1',
                'a3-b2-c1',
                'a4-b3-c2-d1',
                'a5-b4-c3-d2-e1',
                'a6-b5-c4-d3-e2-f1',
                'a7-b6-c5-d4-e3-f2-g1',
                'a8-b7-c6-d5-e4-f3-g2-h1',
                'b8-c7-d6-e5-f4-g3-h2',
                'c8-d7-e6-f5-g4-h3',
                'd8-e7-f6-g5-h4',
                'e8-f7-g6-h5',
                'f8-g7-h6',
                'g8-h7'
            ]
# Square diagonals
square_diagonals = {}
for square in [item for sublist in squares for item in sublist]:
    square_diagonals[square] = [item for item in diagonals if square in item]
# Game score
score = 0
max_score = 0


def generate_square():
    """
    Selects a random square
    """
    return choice([item for item in square_colors.keys()])


def color_test(square, color):
    """
    Checks if the correct color of a square has been passed
    """
    if color.lower() == 'b':
        color = 'black'
    if color.lower() == 'w':
        color = 'white'
    return square_colors[square] == color.lower()


def test_colors():
    """
    Tests the knowledge of the square colors
    """
    global score, max_score
    square = generate_square()
    print("\nWhat is the COLOR of '{}' square? (white/black)".format(square))
    answer = input("Your answer: ")
    if color_test(square, answer) == True:
        score += 5
        print("Correct!") 
        again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
    else:
        print("Wrong! The right answer is '{}'.".format(square_colors[square]))
        again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
        max_score = score
        score = 0
    if again == 'y' or again == 'yes':
        return test_colors()
    else:
        return practice_board()



def diagonals_test_short():
    """
    Test the knowledge of the diagonals
    """
    global score, max_score
    square = generate_square()
    if len(square_diagonals[square]) == 1:
        correct = [square_diagonals[square][0].split('-')[0] + square_diagonals[square][0].split('-')[-1], square_diagonals[square][0].split('-')[-1] + square_diagonals[square][0].split('-')[0]]
        print("\nName the diagonal crossing '{}' square".format(square))
        print("(e.g. x1y8...)")
        answer = input("Your answer: ").lower()
        if answer in correct:
            score += 10
            print("Correct!") 
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
        else:
            print("Wrong! The correct answer is '{}'.".format(correct[0]))
            again = input("Score: {}\nPlay again? (y/n): ".format(score))
            max_score = score
            score = 0
    else:
        correct = [
                      square_diagonals[square][0].split('-')[0] + square_diagonals[square][0].split('-')[-1], square_diagonals[square][0].split('-')[-1] + square_diagonals[square][0].split('-')[0],
                      square_diagonals[square][1].split('-')[0] + square_diagonals[square][1].split('-')[-1], square_diagonals[square][1].split('-')[-1] + square_diagonals[square][1].split('-')[0]
                  ]
        print("\nName the diagonals crossing '{}' square".format(square))
        print("(e.g. x1y8...)")
        answer_1 = input("diagonal-1: ").lower()
        answer_2 = input("diagonal-2: ").lower()
        if answer_1 in correct and answer_2 in correct and answer_1 != answer_2:
            score += 10
            print("Correct!")
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()  
        else:
            print("Wrong! The right answer is: '{}', '{}'.".format(correct[0], correct[1]))
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
            max_score = score
            score = 0
        if again == 'y' or again == 'yes':
            return diagonals_test_short()
        else:
            return practice_board()


def diagonals_test_long():
    """
    Tests the knowledge of the diagonal squares
    """
    global score, max_score
    square = generate_square()
    if len(square_diagonals[square]) == 1:
        print("\nName all squares of the diagonal crossing '{}' square".format(square))
        print("(keep the following syntax: square1-square2-square3...)")
        answer = input("Your answer: ").lower()
        if set(answer.split('-')) == set(square_diagonals[square][0].split('-')):
            score += 12
            print("Correct!")
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
        else:
            print("Wrong! The correct answer is '{}'.".format(square_diagonals[square][0]))
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
            max_score = score
            score = 0
    else:
        print("\nName all squares of the diagonals crossing '{}' square".format(square))
        print("(keep the following syntax: square1-square2-square3...)")
        answer_1 = input("diagonal-1: ").lower()
        answer_2 = input("diagonal-2: ").lower()
        if (set(answer_1.split('-')) in [set(square_diagonals[square][0].split('-')), set(square_diagonals[square][1].split('-'))] and set(answer_2.split('-')) in [set(square_diagonals[square][0].split('-')), set(square_diagonals[square][1].split('-'))]) and set(answer_1.split('-')) != set(answer_2.split('-')):
            score += 12
            print("Correct!")
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()  
        else:
            print("Wrong! The right answer is: '{}', '{}'.".format(square_diagonals[square][0], square_diagonals[square][1]))
            again = input("Score: {}\nPlay again? (y/n): ".format(score)).lower()
            max_score = score
            score = 0
        if again == 'y' or again == 'yes':
            return diagonals_test_long()
        else:
            return practice_board()


def practice_board():
    """
    Provides a menu with practice options
    """
    global score, max_score
    print("\n\n\n\nIMPROVE YOUR KNOWLEDGE OF THE CHESS BOARD")
    print("Select a practice mode:")
    print("1. Square's Color")
    print("2. Name Diagonals")
    print("3. Diagonal's Squares")
    print("4. Exit")
    opt = input("Your choice: ")
    if opt == '1':
        print()
        return test_colors()
    elif opt == '2':
        print()
        return diagonals_test_short()
    elif opt == '3':
        print()
        return diagonals_test_long()
    elif opt == '4':
        if score > 0:
            max_score = score
        print("\nYour max score is {}\nGoodbye!".format(max_score))
        return
    else:
        print("Invalid format. Try again.")
        return practice_board()


practice_board()
