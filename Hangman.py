import random

word_list = ["dog","rabbit","monkey","horse","chicken","snake","dragon","rat","goat","tiger","pig","ox"]
n = random.randint(0, len(word_list))
rand_word = word_list[n]

def hangman(word):
    wrong = 0
    stages = ["",
             "________          ",
             "         |        ",
             "         O        ",
             "        /|\       ",
             "        / \       ",
             "                  ",
            ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a Letter "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "__" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[:wrong]))
        print("You Lose! It was {}.".format(word))
        
hangman(rand_word)