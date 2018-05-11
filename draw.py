import sys
import random
import string

"""
Comments

RETURN CODES
"""

centre = str(sys.argv[1]).upper().strip()
bag = str(sys.argv[2]).upper().strip()
draw = int((sys.argv[3]).strip())
drawer = str(sys.argv[4]).strip()

flag = True

if draw > 7:
	print("0")
	print("Do you really want so many tiles? Didn't think so; ")
	print("Centre: " + centre)
	flag = False

if draw < 1:
	print("0")
	print("You may draw no more than 7 tiles and no less than 1 tile; ")
	print("Centre: " + centre)
	flag = False

if len(bag) < draw:
	print("0")
	print("Nope. Number of tiles in the bag is "+str(len(bag))+"; ")
	print("Centre: " + centre)
	flag = False

if flag:
	drawn = ""
	for i in xrange(draw):
		char = random.randint(0,len(bag)-1)
		drawn += bag[char]
		bag = bag.replace(bag[char], "", 1)

	centre += drawn
	print("1")
	print(drawer + " drew " + drawn + "; ")
	print("Centre: " + centre)
	print(bag)