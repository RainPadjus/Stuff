import os
import urllib.request
with urllib.request.urlopen('https://adventofcode.com/2020/day/9/input') as f:
    data = f.read()

print(data)
a = os.path.basename(__file__)
print(a)
