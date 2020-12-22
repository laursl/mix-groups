# mix-groups

# Motivation
I created this program to help me manage the "coffee chat" activity of one of my college clubs, which is when every few weeks, people get assigned a new group of 3-4 people to meet casually with. I wanted people to always be with people they'd never seen before, but it was too difficult to keep track of each person's history and create assignments by hand. Later, I also had the added complication of there being two different classes in the activity, with one week having groups consist of people of the same class, and the next mixing the two classes.

# Status
The program does all the work of storing each person's history and creating a new satisfying group that matches the type of groups needed depending on the week number inputted. It currently uses a brute force approach and tries random combinations until it finds one that satisfies everyone's history. I use it every two weeks and it saves me about two hours each time. The random approach is only viable because I reset the history every semester and thus it doesn't take too long to find a good assignment (about a minute), however in the long-term I am looking to improve this to have a less costly-running time.
