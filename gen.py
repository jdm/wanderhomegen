#!/bin/env python3
import csv
import random

with open('names.csv') as f:
    names = csv.reader(f)
    names = [name for name in names]
with open('traits.csv') as f:
    traits = csv.reader(f)
    traits = [trait for trait in traits if trait[0]]
with open('animals.csv') as f:
    animals = csv.reader(f)
    animals = [animal for animal in animals if animal]
with open('jobs.csv') as f:
    jobs = csv.reader(f)
    jobs = [job for job in jobs if job[0]]

def kith():
    name = random.choice(names)[0]
    trait1 = random.choice(traits)[1]
    while True:
        trait2 = random.choice(traits)[1]
        if trait1 != trait2:
            break
    animal = random.choice(animals)[0]
    job = random.choice(list(filter(lambda x: x[0] in [trait1, trait2], jobs)))[1]
    pronouns = random.choice([
        ["he", "him", "his", "male", "is"],
        ["she", "her", "hers", "female", "is"],
        ["they", "them", "theirs", "non-binary", "are"]
    ])
    pronoun = pronouns[0].capitalize()
    return {
        "name": name,
        "traits": [trait1, trait2],
        "animal": animal,
        "job": job,
        "pronouns": pronouns,
    }


if __name__ == "__main__":
    result = kith()
    print(f"{result['name']} is a {result['pronouns'][3]} {result['animal']}.")
    print(f"{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {result['traits'][0]} and {result['traits'][1]}.")
    print(f"{result['pronouns'][0].capitalize()} {result['pronouns'][4]} a {result['job']}.")
