def memory_game():

    difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    if difficulty == 0 or difficulty == 6 or difficulty > 6:
        print("No Such Options")

    elif difficulty == 1:
        import random
        level1 = random.sample(range(1, 101), 1)
        import time
        time.sleep(0.7)
        import os
        os.system('cls')
        print(level1)
        n = 1
        print(100 * "\n")
        print("Enter 1 digit and press ENTER")
        print(3 * "\n")
        amount1 = list(map(int, input().split()[:n]))
        print(amount1)
        if level1 == amount1:
            print("Congratulations, you have WON the game")
            print("Your score is: ", difficulty)
            from Scores import score_memory
            score_memory()
            file = open('C:\Temp\MemoryScore.txt', 'a')
            file.write(str(difficulty))
            file.write('\n')
            file.close()
            total = sum(int(line) for line in open('C:\Temp\MemoryScore.txt', 'r'))
            print("Your total score is: ", total)
            exit()
        else:
            print("You have LOST, please try again")
            memory_game()

    elif difficulty == 2:
        import random
        level2 = random.sample(range(1, 101), 2)
        print(level2)
        import time
        time.sleep(0.7)
        import os
        os.system('cls')
        n = 2
        print(100 * "\n")
        print("Enter 2 digits separated by SPACE and press ENTER")
        print(3 * "\n")
        amount2 = list(map(int, input().split()[:n]))
        print(amount2)
        if level2 == amount2:
            print("Congratulations, you have WON the game")
            print("Your score is: ", difficulty)
            from Scores import score_memory
            score_memory()
            file = open('C:\Temp\MemoryScore.txt', 'a')
            file.write(str(difficulty))
            file.write('\n')
            file.close()
            total = sum(int(line) for line in open('C:\Temp\MemoryScore.txt', 'r'))
            print("Your total score is: ", total)
            exit()
        else:
            print("You have LOST, please try again")
            memory_game()

    elif difficulty == 3:
        import random
        level3 = random.sample(range(1, 101), 3)
        print(level3)
        import time
        time.sleep(0.7)
        import os
        os.system('cls')
        n = 3
        print(100 * "\n")
        print("Enter 3 digits separated by SPACE and press ENTER")
        print(3 * "\n")
        amount3 = list(map(int, input().split()[:n]))
        print(amount3)
        if level3 == amount3:
            print("Congratulations, you have WON the game")
            print("Your score is: ", difficulty)
            from Scores import score_memory
            score_memory()
            file = open('C:\Temp\MemoryScore.txt', 'a')
            file.write(str(difficulty))
            file.write('\n')
            file.close()
            total = sum(int(line) for line in open('C:\Temp\MemoryScore.txt', 'r'))
            print("Your total score is: ", total)
            exit()
        else:
            print("You have LOST, please try again")
            memory_game()

    elif difficulty == 4:
        import random
        level4 = random.sample(range(1, 101), 4)
        print(level4)
        import time
        time.sleep(0.7)
        import os
        os.system('cls')
        n = 4
        print(100 * "\n")
        print("Enter 4 digits separated by SPACE and press ENTER")
        print(3 * "\n")
        amount4 = list(map(int, input().split()[:n]))
        print(amount4)
        if level4 == amount4:
            print("Congratulations, you have WON the game")
            print("Your score is: ", difficulty)
            from Scores import score_memory
            score_memory()
            file = open('C:\Temp\MemoryScore.txt', 'a')
            file.write(str(difficulty))
            file.write('\n')
            file.close()
            total = sum(int(line) for line in open('C:\Temp\MemoryScore.txt', 'r'))
            print("Your total score is: ", total)
            exit()
        else:
            print("You have LOST, please try again")
            memory_game()

    elif difficulty == 5:
        import random
        level5 = random.sample(range(1, 101), 5)
        print(level5)
        import time
        time.sleep(0.7)
        import os
        os.system('cls')
        n = 5
        print(100 * "\n")
        print("Enter 5 digits separated by SPACE and press ENTER")
        print(3 * "\n")
        amount5 = list(map(int, input().split()[:n]))
        print(amount5)
        if level5 == amount5:
            print("Congratulations, you have WON the game")
            print("Your score is: ", difficulty)
            from Scores import score_memory
            score_memory()
            file = open('C:\Temp\MemoryScore.txt', 'a')
            file.write(str(difficulty))
            file.write('\n')
            file.close()
            total = sum(int(line) for line in open('C:\Temp\MemoryScore.txt', 'r'))
            print("Your total score is: ", total)
            exit()
        else:
            print("You have LOST, please try again")
            memory_game()


memory_game()

