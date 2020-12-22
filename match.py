"""A group generating program."""

import random
import sys
import json

# historyfile = sys.argv[2]
weeknum = int(sys.argv[1])

def check(groupfile, historyfile):
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
            print("help")
            history = {}
    fp.close()

    """Check and update history"""
    if history == {}:
        for group in groups:
            for person in group:
                temp = group[:]
                temp.remove(person)
                history[person] = temp
        with open(f'Week{weeknum -1}history.txt', "w+") as f:
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
                        # print("FAILED: " + person + " has already been matched with " + others)
                if bad:
                    return bad
                history[person] += temp

    with open(f'Week{weeknum}history.txt', "w+") as f:
        json.dump(history,f)

    f.close()
    return bad

def group_generator(week,arrayA,arrayB):
    groups = []
    groupA = arrayA
    groupB = arrayB
    random.shuffle(groupA)
    random.shuffle(groupB)
    f = open('output.txt', 'w+')
    if week % 2 == 1:   # generate merged groups of 4
            ctrA, ctrB = len(groupA), len(groupB)
            if len(groupA) > len(groupB):
                while ctrA > ctrB:
                    f.write(f'{groupA[ctrA-1]} {groupA[ctrA-2]} {groupB[ctrB-1]}\n')
                    ctrA = ctrA - 2
                    ctrB = ctrB - 1
            elif len(groupB) > len(groupA):
                while ctrB > ctrA:
                    f.write(f'{groupB[ctrB-1]} {groupB[ctrB-2]} {groupA[ctrA-1]}\n')
                    ctrB = ctrB - 2
                    ctrA = ctrA - 1

            if ctrA % 2 == 1:
                f.write(f'{groupA[ctrA-1]} {groupA[ctrA-2]} {groupB[ctrB-1]}\n')
                ctrA = ctrA - 2
                ctrB = ctrB - 1
                f.write(f'{groupB[ctrB-1]} {groupB[ctrB-2]} {groupA[ctrA-1]}\n')
                ctrA = ctrA - 1
                ctrB = ctrB - 2

            while ctrA >= 2:
                f.write(f'{groupA[ctrA-1]} {groupA[ctrA-2]} {groupB[ctrB-1]} {groupB[ctrB-2]}\n')
                ctrB = ctrB - 2
                ctrA = ctrA - 2

    else:   # Within a Group
        for group in [groupA, groupB]:
            ctr = 0
            if len(group) % 3 == 2:  # first generate two groups of 4
                f.write(f'{group[ctr]} {group[ctr+1]} {group[ctr+2]} {group[ctr+3]}\n')
                ctr = ctr + 4
                f.write(f'{group[ctr]} {group[ctr+1]} {group[ctr+2]} {group[ctr+3]}\n')
                ctr += 4
            elif len(group) % 3 == 1:  # first generate one group of 4
                f.write(f'{group[ctr]} {group[ctr+1]} {group[ctr+2]} {group[ctr+3]}\n')
                ctr += 4
            # generate groups of 3 until run out of elements
            while ctr < len(group):
                f.write(f'{group[ctr]} {group[ctr+1]} {group[ctr+2]}\n')
                ctr = ctr + 3
    f.close()

file1 = '2022.txt'
file2 = '2023.txt'

test_cases = [[file1, file2]]
arrayA = [line.rstrip('\n') for line in open(file1)]
arrayB = [line.rstrip('\n') for line in open(file2)]

group_generator(weeknum, arrayA, arrayB)

historyfile = "Week" + str(weeknum - 1) + "history.txt"
checkval = check('output.txt', historyfile)
tries = 1
while checkval:
    tries += 1
    group_generator(weeknum, arrayA, arrayB)
    checkval = check('output.txt', historyfile)

f = open("output.txt", "r")
lines = f.readlines()
lines = [l for l in lines]
f1 = open(f'Week{weeknum}.txt', "w+")
f1.writelines(lines)
f.close()
f1.close()

sys.stdout.write(f'Done with week {weeknum}. It took {tries} tries')
