#MIT License
#Copyright (c) 2019 Devang Thakkar
# https://www.devangthakkar.com
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

import itertools
import random
import sys

"""
This script parses the input passed by the user. There are four possible
cases, with possible subcases.

The first case is where the user wishes to draw tiles from the bag. The
user may input as many dots as the number of words they wishes to draw such
that the minimum number of dots is 1 and the maximum number of dots is 7.

The second case is where the user wishes to send a chat message to the group.
The message needs to begin with a "/" (just the mark, without the quotes, duh)
and may be as long as needed.

The third (and the most important) case is where the user wishes to make or
snatch a word. The minimum allowed word size is 6, normal snatch rules apply.
However, this program is not built to check if attempted words are derivatives
of existing word (Derivative rule) or fall under the 5+1/4+2/3+3 violation
(Composition rule). Word list used is CSW15. The message just needs to be the
word itself - no frills.

The fourth case is for a user to retract their or someone else's word if it is
pointed out to be a violation of the Derivative or Composition rule. The
message needs to be the word prepended by a "-". Withdrawing words is slightly
shitty - the withdrawn word goes into the centre thus if the word was
initially snatched, the user from whom the word was snatched needs to remake
the word. Shitty, I know. Improve it, when you can.

The fifth (and the last, for now) case is to reset the game. Enter ~ to reset
the game.

RETURN CODES:
 0: Chat
 1: Valid attempt
-1: Invalid attempt
 2: Valid draw of tiles
-2: Invalid draw of tiles
 3: Valid withdrawal of tiles
-3: Invalid withdrawal of tiles
 4: Snatching tiles
 5: Shuffling
-9: Reset the game

EXAMPLE RUN:

d1> .......
>>> d1 drew ATRESCO; Centre: ATRESCO
d2> .
>>> d2 drew S; Centre: ATRESCOS
d1> coasters
>>> d1 made COASTERS; Centre:
d1> ......
>>> d1 drew MOEDINA; Centre: MOEDINA
d2> domained
>>> DOMAINED can not be made now; Centre: MOEDINA
d2> domain
>>> d2 made DOMAIN; Centre: E
d1> .........
>>> Do you really want so many tiles? Didn't think so; Centre: E
d1> .......
>>> d1 drew TTREASY; Centre: ETTREASY
d2> treats
>>> d2 made TREATS; Centre: EY
d1> /Wait
d1> /That's not allowed
d2> /Ah. MB.
d2> -TREATS
>>> d2 withdrew TREATS; Centre: EYTREATS
"""

# @profile
def funct():
	# first argument is the letters in the centre
	centre = str(sys.argv[1]).upper().strip()
	# second argument is the word attempted
	attempted = str(sys.argv[2]).upper().strip()
	# third argument is the user attempting the word
	attempter = str(sys.argv[3]).strip()
	#fourth argument is the words already made
	words = str(sys.argv[4]).upper().strip()

	words = words.replace("],","];")
	for char in ["\"", "[", "]", "{", "}"]:
		if char in words:
			words = words.replace(char, "")

	word_arr = words.split(";")
	word_dict = {}
	for user in word_arr:
		username = user.strip().split(":")[0]
		if username:
			for word in ((user.strip().split(":"))[1]).strip().split(","):
				if not username in word_dict:
					word_dict[username] = [word]
				else:
					word_dict[username].append(word) 


	check = True
	draw = False
	withdraw = False
	chat = False
	reset = False

	# DRAWING TILES
	if attempted == '':
		print("-1")
		print(attempted + " is too short; ")
		print("Centre: " + centre)
		sys.exit()

	if attempted[0] == '.':
		check = False
		draw = True

		for letter in attempted:
			if letter != '.':
				draw = False

		if draw:
			print("2")
			print(len(attempted))
		else:
			print("-2")
			print("Perhaps there's a typo; ")
			print("Centre: " + centre)

	# SHUFFLING
	if attempted[0] == '$':
		shuffled_centre = list(centre)
		random.shuffle(shuffled_centre)
		centre = ''.join(shuffled_centre)
		print("5")
		print("Centre: " + centre)

	# CHATTING
	if attempted[0] == '/':
		check = False
		chat = True
		print("0")
		print(attempted[0][1:])

	# WITHDRAWING
	if attempted[0] == '-':
		check = False
		withdraw = True

		flag_w = False

		if attempted == '-':
			print("-1")
			print(attempted + " is an invalid word; ")
			print("Centre: " + centre)
			# flag_w = False
			sys.exit()

		withdrawn = attempted[1:]
		for user in word_dict:
			for word in word_dict[user]:
				if withdrawn == word:
					print("3")
					print(attempter+" has withdrawn "+user+"'s word "+word+"; ")
					shuffled = list(centre+word)
					random.shuffle(shuffled)
					print("Centre: " + centre + ''.join(shuffled))
					print(user.lower())
					print(word)
					flag_w = True
				if flag_w:
					break
			if flag_w:
				break

		if not flag_w:
			print("-3")
			print("You are trying to withdraw a non existing word; ")
			print("Centre: " + centre)

	#RESETTING
	if attempted[0] == '~':
		check = False
		reset = True
		print("-9")
		print(attempter + " has reset the game; ")
		print("Centre: ")

	# CHECKING IF LEGIT WORD
	if check:

		if len(attempted) < 2:
			print("-1")
			print(attempted + " is too short; ")
			print("Centre: " + centre)
			sys.exit()

		temp = centre
		flag = True

		for letter in attempted:
			if letter not in centre:
				flag = False
				centre = temp
				break
			else:
				centre = centre.replace(letter, "", 1)

		choice = (attempted[0]+attempted[1]).upper()

		# prevent crashing because of file not found because of random input
		alphabets = [str(chr(i)) for i in range(65, 91)]
		valid = [''.join(i) for i in itertools.product(alphabets, repeat = 2)]		
		if choice not in valid:
			print("-1")
			print(attempted + " is an invalid word; ")
			centre = temp
			print("Centre: " + centre)
			flag = False
			sys.exit()

		csw15 = set([])
		fname = "new_updated_dict/CSW_" + choice + ".txt"
		with open(fname, "r") as f:
			for line in f:
				csw15.add(line.strip().rstrip())

		if ("\"" + attempted + "\"") not in csw15 and flag:
			print("-1")
			print(attempted + " is an invalid word; ")
			centre = temp
			print("Centre: " + centre)
			flag = False
			sys.exit()

		if flag:
			print("1")
			print(attempter + " made: " + attempted + ", ")
			print("Centre: " + centre)
			sys.exit()

		if not flag:
			flag1 = True
			loser = ""
			lost = ""
			same = False

			for user in word_dict:
				for word in word_dict[user]:
					flag1 = True
					temp_w = word
					if attempted == word:
						same = True
						break
					for letter in attempted:
						if letter not in centre + word:
							flag1 = False
							centre = temp
							break
						else:
							if letter in word:
								word = word.replace(letter, "", 1)
							else:
								centre = centre.replace(letter, "", 1)
					word = temp_w
					temp_a = attempted
					if flag1:
						for letter in word:
							if letter not in attempted:
								flag1 = False
								break
							else:
								attempted = attempted.replace(letter, "", 1)
						attempted = temp_a

					if flag1:
						lost = word
						break
				if same:
					break
				if flag1:
					loser = user
					break

			if not flag1 or same:
				print("-1")
				print(attempted + " is invalid; ")
				centre = temp
				print("Centre: " + centre)
				sys.exit()
			
			if ("\"" + attempted + "\"") not in csw15 and flag1:
				print("-1")
				print(attempted + " is an invalid word ; ")
				centre = temp
				print("Centre: " + centre)
				flag = False
				sys.exit()

			if flag1:
				print("4")
				print(attempter + " made " + attempted + " from " + lost + ";")
				print("Centre: " + centre)
				print(loser.lower())
				print(lost)
				print(attempted)
				sys.exit()

funct()