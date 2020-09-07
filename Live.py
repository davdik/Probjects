def welcome():
    name = input("Please Enter Your Name: ")
    print("Hello", name, "and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")


welcome()


def load_game():
    game = int(input("Please choose a game by typing 1 or 2: "))
    if game == 0 or game == 3 or game > 3:
        print("No such option, please try again")
        load_game()
    elif game == 1:
        print("Guess Game - guess a number and see if you chose like the computer")
        from GuessGame import random
        random()
    elif game == 2:
        print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        from MemoryGame import memory_game
        memory_game()


load_game()

