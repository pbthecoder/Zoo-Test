import random

def generate_syllable():
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    syllable = random.choice(consonants)
    syllable += random.choice(vowels)
    if random.random() < 0.5:
        syllable += random.choice(consonants)
    return syllable

def generate_animal_name():
    name = ""
    for _ in range(random.randint(1,3)):
        name += generate_syllable()
    return name.capitalize()

