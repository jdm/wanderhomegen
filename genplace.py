#!/bin/env python3
import csv
import random
import os
from collections import defaultdict
from gen import kith, describe

natures = defaultdict(lambda: {
    "locations": [],
})
locations = defaultdict(lambda: {
    "aesthetics": [],
    "folklores": [],
})
path = os.path.dirname(__file__)
with open(os.path.join(path, 'natures.csv')) as f:
    natures_values = csv.reader(f)
    for nature in natures_values:
        if nature[0]:
            natures[nature[0]]["locations"] += [nature[1]]
with open(os.path.join(path, 'aesthetics.csv')) as f:
    aesthetics = csv.reader(f)
    for aesthetic in aesthetics:
        if aesthetic[0]:
            locations[aesthetic[0]]["aesthetics"] += [aesthetic[1]]
with open(os.path.join(path, 'folklores.csv')) as f:
    folklores = csv.reader(f)
    for folklore in folklores:
        if folklore[0]:
            locations[folklore[0]]["folklores"] += [folklore[1]]

def place():
    nature_choices = random.sample(list(natures.keys()), k=3)
    location_choices = []
    num_locations = 3

    for nature in nature_choices:
        choice = random.choice(natures[nature]["locations"])
        location_choices += [choice]

    place_aesthetics = set()
    place_folklores = set()
    num_aesthetics = 4
    num_folklores = 2
    place_kith = []

    while len(place_aesthetics) < num_aesthetics:
        location = random.choice(list(location_choices))
        choices = locations[location]["aesthetics"]
        choice = random.choice(choices)
        kith_trait = None

        if "{{" in choice:
            start = choice.index("{{")
            end = choice.index("}}")
            kith_trait = choice[start + 2:end]
        choice = choice.replace("{{", "").replace("}}", "")

        if choice not in place_aesthetics:
            if kith_trait:
                place_kith += [kith(kith_trait)]
            place_aesthetics.add(choice)

    while len(place_folklores) < num_folklores:
        location = random.choice(list(location_choices))
        choices = locations[location]["folklores"]
        choice = random.choice(choices)
        if choice not in place_folklores:
            place_folklores.add(choice)

    return {
        "name": "Misthaven",
        "natures": nature_choices,
        "locations": location_choices,
        "folklores": list(place_folklores),
        "aesthetics": list(place_aesthetics),
        "kith": place_kith,
    }

if __name__ == "__main__":
    result = place()
    nature_desc = [f"{r[1]} ({r[0]})" for r in zip(result["natures"], result["locations"])]
    print(f"{result['name']} has aspects of {', '.join(nature_desc)}.")
    print(f"It has {', '.join(result['aesthetics'])}.")
    print(f"There are legends of {result['folklores'][0]} and {result['folklores'][1]}.")
    if result['kith']:
        print("There are also some creatures who live here:")
    for kith in result['kith']:
        describe(kith)
