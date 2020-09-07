def guess_game():

    import random
    random = random.randint(1, 5)

    difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    if difficulty == 0 or difficulty == 6 or difficulty > 6:
        print("No Such Options")

    print("The Computer's number was: ", random)

    if random == difficulty:
        print("Congratulations, you have WON the game")
        print("Your score is: ", difficulty)
        from Scores import score_guess
        score_guess()
        file = open('C:\Temp\GuessScore.txt', 'a')
        file.write(str(difficulty))
        file.write('\n')
        file.close()
        total = sum(int(line) for line in open('C:\Temp\GuessScore.txt', 'r'))
        print("Your total score is: ", total)
        exit()
    else:
        print("You have LOST, please try again")
        guess_game()


guess_game()



