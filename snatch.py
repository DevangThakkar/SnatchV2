# miku
import string
import random
import sys

# center = str(sys.argv[1]).upper()
# attempted = str(sys.argv[2]).upper()
k = 7
tiledict = {
'A' : 9,
'B' : 2,
'C' : 2,
'D' : 4,
'E' : 12,
'F' : 2,
'G' : 3,
'H' : 2,
'I' : 9,
'J' : 1,
'K' : 1,
'L' : 4,
'M' : 2,
'N' : 6,
'O' : 8,
'P' : 2,
'Q' : 1,
'R' : 6,
'S' : 4,
'T' : 6,
'U' : 4,
'V' : 2,
'W' : 2,
'X' : 1,
'Y' : 2,
'Z' : 1,
'?' : 2
}

tilestring = list(''.join([L*tiledict[L] for L in string.ascii_uppercase+'?']))
currstring = []
while tilestring != "":
	print("########################")
	k = input("Enter number of tiles to draw from bag\n")
	drawntiles = [tilestring.pop(random.randrange(len(tilestring))) for _ in xrange(k)]
	currstring = currstring + drawntiles
	print("Tiles on the floor:")
	print(currstring) #, tilestring)
	enterWord = raw_input("Enter letters removed from floor. If no letters are removed, press Enter.\n")
	flag = 0
	for i in enterWord:
		flag = 1
		currstring.remove(i)
	if flag:
		print("Tiles on the floor:")
		print(currstring)

	