#!/usr/bin/env python3
import cgi
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import gen

print("Content-Type: text/html")
print()
result = gen.kith()
print(gen.describe_html(kith))
