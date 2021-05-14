#!/bin/env python3
import csv
import random
import os

path = os.path.dirname(__file__)
with open(os.path.join(path, 'names.csv')) as f:
    names = csv.reader(f)
    names = [name for name in names]
with open(os.path.join(path, 'traits.csv')) as f:
    traits = csv.reader(f)
    traits = [trait for trait in traits if trait[0]]
with open(os.path.join(path, 'animals.csv')) as f:
    animals = csv.reader(f)
    animals = [animal for animal in animals if animal]
with open(os.path.join(path, 'jobs.csv')) as f:
    jobs = csv.reader(f)
    jobs = [job for job in jobs if job[0]]

def kith(trait1=None):
    name = random.choice(names)[0]
    if not trait1:
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


def describe(result):
    print(f"{result['name']} is a {result['pronouns'][3]} {result['animal']}.")
    print(f"{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {result['traits'][0]} and {result['traits'][1]}.")
    print(f"{result['pronouns'][0].capitalize()} {result['pronouns'][4]} a {result['job']}.")


def describe_html(result):
    a = "a" if result['job'][0].lower() not in ['a', 'e', 'i', 'o', 'u'] else "an"
    print(f"<p>{result['name']} is a {result['pronouns'][3]} {result['animal']}.</p>")

    def trait_link(trait):
        return "<a href='https://joshmatthews.net/wanderhome/Traits#" + trait + "'>" + trait + "</a>"

    print(f"<p>{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {trait_link(result['traits'][0])} and {trait_link(result['traits'][1])}.</p>")
    print(f"<p>{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {a} {result['job']}.</p>")


if __name__ == "__main__":
    result = kith()
    describe(result)
