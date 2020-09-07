def score_guess():
    import os
    if not os.path.exists('C:\Temp\GuessScore.txt'):
        with open('C:\Temp\GuessScore.txt', 'w'): pass


score_guess()


def score_memory():
    import os
    if not os.path.exists('C:\Temp\MemoryScore.txt'):
        with open('C:\Temp\MemoryScore.txt', 'w'): pass


score_memory()
