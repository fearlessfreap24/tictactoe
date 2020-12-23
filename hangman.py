from words import words
import random
import string
import re


def getWord():
    word = random.choice(words)
    badChars = r'[^A-Za-z]'
    while re.findall(badChars, word) or len(word) < 5:
        word = random.choice(words)
    
    return word.upper()


def createDashReplacementWord(word, usedLetter):
    dashedString = str()
    for i in word:
        if i in usedLetter:
            dashedString += i + " "
        else:
            dashedString += '-' + " "
    return dashedString


def hangman():
    word = getWord()
    usedLetter = set()
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    lives = 0

    while len(wordLetters) > 0 and lives < 6:
        dashedReplacedWord = createDashReplacementWord(word, usedLetter)
        print(f"\nYour word to guess = {dashedReplacedWord}") 
        userLetter = input("Guess a letter: ").upper()
        if userLetter in alphabet - wordLetters and userLetter not in usedLetter:
            print(f'Your letter "{userLetter}" is incorrect please try again.')
            lives += 1
        elif userLetter in usedLetter:
            print(f"You have already used \"{userLetter}\". Please try again")
        else:
            wordLetters.remove(userLetter)

        usedLetter.add(userLetter)
        print(f'You have used the following letters: {str(sorted(usedLetter))} and have {6-lives} lives remaining')

    if lives == 6:
        print(f"\nYou have failed to solve the word \"{word}\"")
    else:
        print(f"\nCongratulations!!! You have solved the word \"{word}\"")

if __name__ == "__main__":
    hangman()