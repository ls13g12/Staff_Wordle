from random import randint

def get_new_word():
    index = randint(0, len(words))
    return words[index]

words = [
    'water',
    'paper',
    'waste',
    'great'
]