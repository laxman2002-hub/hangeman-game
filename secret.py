import random
from words import WORDS

def load_words():
    word_list = WORDS.split(" ")
    return word_list

def choose_word():

    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
secret_word = choose_word()
