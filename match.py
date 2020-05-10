"""A group generating program."""

import random

size =input("How large should each group be? ")
fname = input("Enter file name: ")

all = []
valid = []
basegroups = {}
tracker = {}

with open(fname,'r') as f:
    for line in f:
        for word in line.split():
            all.append(word)
            valid.append(word)

f.close()
numnames = len(all)
numgroups = numnames // int(size)
for elem in all:
    tracker[elem] = []

for i in range(numgroups):
    basegroups[i] = []
    for j in range(int(size)):
        person = random.choice(valid)
        basegroups[i].append(person)
        valid.remove(person)

if numgroups % int(size) != 0:
    i = 0
    while len(valid) > 0:
        person = random.choice(valid)
        basegroups[i].append(person)
        valid.remove(person)
        i += 1

for name in tracker.keys():
    for group in basegroups.items():
        if any((i == name) for i in group[1]):
            tracker[name] += group

results = open("groups.text","w+")
results.write("Groups 1 \n")
results.write("GROUP \n")
for group in basegroups.items():
     groups = map(lambda x:x+'\n', group[1])
     results.writelines(groups)
     results.write("GROUP \n")
results.close()
