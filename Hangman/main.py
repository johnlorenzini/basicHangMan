import time
import urllib.request
from bs4 import BeautifulSoup
import requests
import random


def spacing():
    for i in range(0, 50):
        print()


def formatWord():
    wordSite = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(wordSite)
    words = response.content.splitlines()
    genRand = random.randint(0, 10000)
    word = str(words[genRand])
    return word[2:len(word) - 1]


def getHint(word):
    definition = urllib.request.urlopen("https://www.vocabulary.com/dictionary/" + word)
    soup = BeautifulSoup(definition, 'html.parser')
    results = soup.find(id="page")
    elements = results.find("div", class_="definition")
    try:
        test = elements.text
    except AttributeError:
        spacing()
        print("Generated word has no available definition! Generating new word.")
        time.sleep(2)
        return ''
    ind = 0
    while test[ind:ind + 1] != " ":
        test = test[ind + 1:]
    hint = test.strip()
    if word.lower() in hint:
        spacing()
        print("Secret word found in hint! Anonymizing...")
        time.sleep(1)
        words = hint.split()
        numAsterisk = '*' * len(word)
        index = 0
        for i in words:
            if i == word.lower():
                words[index] = numAsterisk
            index += 1
        return " ".join(words)
    else:
        return hint


def guesserWin(solved):
    spacing()
    print("-=-=-=-=-=-=-   Correct! The Secret Word Was:   -=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-          " + solved + "           -=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-        " + name1 + " Wins!        -=-=-=-=-=-=-")
    time.sleep(5)


if __name__ == '__main__':
    spacing()
    print('-=-=-=-=-=-  Guesser Setup  -=-=-=-=-=-')
    print()
    name1 = input('Guesser Name: ')
    tries = int(input("Hello " + name1 + ", how many tries will it take to guess the word: "))
    spacing()

    print("-=-=-=-=-=-  WordMaker Setup  -=-=-=-=-=-")
    print()
    makerChoice = input("Would you like to choose a word, or use a randomly generated one instead? \n(C = Choose, "
                        "R = Random): \n").upper()

    if makerChoice == 'R':
        secret = ''
        findHint = ''
        name2 = "The Robot"
        while findHint == '':
            secret = formatWord().upper()
            findHint = getHint(secret)
        usedHint = False
        spacing()
        print("Word Generated. \n\nAs you've chosen a random word, you may choose to sacrifice half \nof your guesses "
              "to "
              "view the word's definition.")
        time.sleep(5)
    else:
        name2 = input('WordMaker Name: ')
        secret = input('Alright ' + name2 + ", what's the secret word: ").upper()

    spacing()
    print("Let's play hangman!")
    time.sleep(1.5)
    spacing()
    wordGuessed = ''
    for i in range(0, len(secret)):
        if secret[i] == " ":
            wordGuessed += " "
        else:
            wordGuessed += "_"

    lettersGuessed = ''
    while tries > 0:
        print()
        print("SECRET WORD --->  " + wordGuessed + "  <--- SECRET WORD")
        print()
        print("You have " + str(tries) + " tries remaining.")
        print()
        print("Letters Guessed: " + lettersGuessed.upper())
        print()
        if makerChoice == 'R' and usedHint is False:
            guess = input(
                'Enter any letter to guess.\nEnter "solve" to try to solve the puzzle.'
                '\nEnter "hint" to sacrifice 1/2 of your wishes to see the definition.\nEnter "quit" to quit.\n').upper()
        else:
            guess = input('Enter any letter to guess.\nEnter "solve" to try to solve the puzzle.\nEnter "quit" to '
                          'quit.\n').upper()
        if guess == 'QUIT':
            tries = 0
            break
        elif guess == 'HINT' and usedHint is False:
            spacing()
            print("You have 10 seconds to view the definition of " + wordGuessed + ": ")
            print()
            print(findHint)
            time.sleep(10)
            usedHint = True
            tries = int(tries / 2)
        elif guess == 'HINT' and usedHint is True:
            spacing()
            print("You've already used your hint!!")
            time.sleep(2)
        elif guess == 'SOLVE':
            spacing()
            print("You've chosen to SOLVE the puzzle. Input guess below: ")
            solve = input()
            if solve.upper() == secret.upper():
                tries = 0
                guesserWin(secret)
                break
            else:
                tries -= 1
                print()
                print("Incorrect! Tries Remaining: ", tries)
                time.sleep(2)
        elif len(guess) > 1:
            spacing()
            print("You can only guess one letter per try!")
            time.sleep(2)
        else:
            if guess in lettersGuessed:
                print()
                print('You have already guessed this word.')
                time.sleep(2)
            elif guess not in secret:
                lettersGuessed += guess
                tries -= 1
                if tries == 0:
                    spacing()
                    print()
                    print("-=-=-=-=-=-=-   Incorrect! The Secret Word Was:   -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-           " + secret + "           -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-         " + name2 + " Wins!         -=-=-=-=-=-=-")
                    time.sleep(5)
                else:
                    print()
                    print("Incorrect! Tries Remaining: ", tries)
                    time.sleep(2)
            elif guess in secret:
                lettersGuessed += guess
                instances = 0
                for index in range(0, len(secret)):
                    if secret[index:index + 1] == guess:
                        wordGuessed = wordGuessed[:index] + guess + wordGuessed[index + 1:]
                        instances += 1
                print()
                print("Correct!\n" + str(instances) + " Letter(s) Found!")
                time.sleep(2)
                if wordGuessed == secret:
                    tries = 0
                    guesserWin(secret)
                    break
        spacing()
