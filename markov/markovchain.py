import random, sys, os

nonword = "\n"
w1 = nonword
w2 = nonword

table = {}

filename = os.path.abspath("../corpus/sherlock.txt")
sherlock = open(filename, "rb")

for line in sherlock:
	for word in line.split():
		table.setdefault((w1, w2), []).append(word)
		w1, w2 = w2, word

table.setdefault( (w1, w2), [] ).append(nonword)

w1 = nonword
w2 = nonword

maxwords = 10000
output = ""

for i in xrange(maxwords):
	newword = random.choice(table[(w1,w2)])
	if newword == nonword:
		sys.exit()
	if newword[-1] == '.':
		output += newword + "\n"
	else:
		output += newword + " "
	w1, w2 = w2, newword

outsherlock = open("output/out-markov.txt", "wb")
outsherlock.write(output)

outsherlock.close()
sherlock.close()