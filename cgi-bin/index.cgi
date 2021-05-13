#!/usr/bin/env python3
import cgi
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import gen

print("Content-Type: text/html")
print()
result = gen.kith()
a = "a" if result['job'][0].lower() not in ['a', 'e', 'i', 'o', 'u'] else "an"
print(f"<p>{result['name']} is a {result['pronouns'][3]} {result['animal']}.</p>")

def trait_link(trait):
    return "<a href='https://joshmatthews.net/wanderhome/Traits#" + trait + "'>" + trait + "</a>"

print(f"<p>{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {trait_link(result['traits'][0])} and {trait_link(result['traits'][1])}.</p>")
print(f"<p>{result['pronouns'][0].capitalize()} {result['pronouns'][4]} {a} {result['job']}.</p>")
