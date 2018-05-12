#MIT License
#Copyright (c) 2018 Devang Thakkar
# https://home.iitb.ac.in/~devangthakkar
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in 
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#PEP-8 format: Limit all lines to a maximum of 79 characters ----------------|

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