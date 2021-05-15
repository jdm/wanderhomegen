#!/usr/bin/env python3
import cgi
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import genplace
import gen
import re

print("Content-Type: text/html;charset=utf-8")
print()
result = genplace.place()

def link(name, anchor, anchor_text=None):
    text = anchor_text if anchor_text else anchor
    return "<a href='https://joshmatthews.net/wanderhome/" + name + "#" + anchor + "'>" + text + "</a>"

def linkify_traits(l):
    return list(map(lambda x: re.sub("{{(\w+)}}", link("Traits", "\\1"), x), l))

def andify(list):
    return ', and '.join([', '.join(list[0:-1]), list[-1]])

description = list(map(
    lambda x: link("Natures", x[1]) + " " + "(" + link("Natures", x[0] + "_Natures", x[0]) + ")",
    zip(result['natures'], result['locations'])
))
description = andify(description)
print(f"<p>{result['name']} has aspects of {description}.</p>")
print(f"<p>It has {andify(result['aesthetics'])}.</p>")
print(f"<p>There are legends of {andify(linkify_traits(result['folklores']))}.</p>")
if True or result['kith']:
    print("<p>There are also some creatures who live here:")
    print("<ul id=kith>")
    for kith in result['kith']:
        print("<li>")
        gen.describe_html(kith)
        print("</li>")
    print("</ul></p>")
    print("<button onclick='addkith()'>Generate a kith</button>")

print("<script src='../kith.js'></script>")
