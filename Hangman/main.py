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
    return test.strip()


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
            secret = formatWord()
            findHint = getHint(secret)
        usedHint = False
        spacing()
        print("Word Generated. \n\nAs you've chosen a random word, you may choose to sacrifice half \nof your guesses "
              "to "
              "view the word's definition.")
        time.sleep(5)
    else:
        name2 = input('WordMaker Name: ')
        secret = input('Alright ' + name2 + ", what's the secret word: ").lower()

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
        print(wordGuessed)
        print()
        print("You have " + str(tries) + " remaining.")
        print()
        print("Letters Guessed: " + lettersGuessed.upper())
        print()
        if makerChoice == 'R' and usedHint is False:
            guess = input(
                'Guess (type "quit" to exit, or "hint" to view \nthe definition for 50% of your tries): ').lower()
        else:
            guess = input('Guess (type "quit" to exit): ').lower()
        if guess == 'quit':
            tries = 0
            break
        elif guess == 'hint' and usedHint is False:
            spacing()
            print("You have 10 seconds to view the definition of " + wordGuessed + ": ")
            print()
            print(findHint)
            time.sleep(10)
            usedHint = True
            tries /= 2
        elif guess == 'hint' and usedHint is True:
            spacing()
            print("You've already used your hint!!")
            time.sleep(2)
        else:
            if guess not in secret:
                tries -= 1
                if tries == 0:
                    spacing()
                    print()
                    print("-=-=-=-=-=-=-   Incorrect! The Secret Word Was:   -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-           " + secret + "           -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-         " + name2 + " Wins!         -=-=-=-=-=-=-")
                    time.sleep(5)
                else:
                    print("Incorrect! Tries Remaining: ", tries)
                    time.sleep(2)
            elif guess in lettersGuessed:
                print('You have already guessed this word.')
                time.sleep(1)
            elif guess in secret:
                lettersGuessed += guess
                instances = 0
                for index in range(0, len(secret)):
                    if secret[index:index + 1] == guess:
                        wordGuessed = wordGuessed[:index] + guess + wordGuessed[index + 1:]
                        instances += 1
                print("Correct!", instances, "Letter(s) Found!")
                time.sleep(2)
                if wordGuessed == secret:
                    tries = 0
                    spacing()
                    print("-=-=-=-=-=-=-   Correct! The Secret Word Was:   -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-          " + secret + "           -=-=-=-=-=-=-")
                    print("-=-=-=-=-=-=-        " + name1 + " Wins!        -=-=-=-=-=-=-")
                    time.sleep(5)
                    break
        spacing()
