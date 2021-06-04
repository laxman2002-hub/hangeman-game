from secret import secret_word
from images import IMAGES

def is_word_guessed(secret_word, letters_guessed):
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word

def get_available_letters(letters_guessed):
    letters_left = "abcdefghijklmnopqrstuvwxyz"
    for c in letters_guessed:
        letters_left = letters_left.replace(c,"")
    return letters_left

def hangman(secret_word):

    print("~~~~~~~~~~ * Welcome to the game, Hangman! * ~~~~~~~~~~~\n\n")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')
    img = 0
    hint = 1
    letters_guessed = []
    while img!=8:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters),"  hint =",hint," Lives =",8-img)

        guess = input("Please guess a letter: ")

        if guess == "hint" and hint!=0:
            hint -= 1
            for c in secret_word:
                if c not in letters_guessed:
                    letters_guessed.append(c)
                    print(" word :",get_guessed_word(secret_word, letters_guessed) )
                    print()
                    break
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("~~~~~~~~~ * * Congratulations, you won! * * ~~~~~~~")
                break
            continue
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} \n".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("~~~~~~~~~ * * Congratulations, you won! * * ~~~~~~~")
                break
        else:
            print(IMAGES[img])
            if img==7:
                print("$$$$$$$$$ Oops! You lose $$$$$$$$$$ \n")
                print("Correct word was :",secret_word)
                break
            print("  Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)),"\n")
            img+=1
            letters_guessed.append(letter)

hangman(secret_word)