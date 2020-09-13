"""A group generating program."""

import random
import sys
import json

groupfile = sys.argv[1]
historyfile = sys.argv[2]
groups = []

"""Open and read groups."""
with open(groupfile,'r') as f:
    for line in f:
        groups.append([word.lower() for word in line.split()])
f.close()

"""Open and read history."""
with open(historyfile, 'r') as fp:
    try:
        history = json.load(fp)
    except ValueError:
        history = {}
fp.close()

"""Check and update history"""
if history == {}:
    for group in groups:
        for person in group:
            temp = group[:]
            temp.remove(person)
            history[person] = temp
    with open(historyfile, "w") as f:
        json.dump(history,f)
    f.close()
    sys.exit(0)

for group in groups:
    bad = False
    for person in group:
        temp = group[:]
        temp.remove(person)
        if person not in history:
            history[person] = temp
        else:
            for others in temp:
                if others in history[person]:
                    bad = True
                    print("FAILED: " + person + " has already been matched with " + others)
            if bad:
                sys.exit(1)
            history[person] += temp

with open(historyfile, "w") as f:
    json.dump(history,f)

f.close()
sys.exit(0)
