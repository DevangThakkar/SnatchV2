# ONLINE SNATCH

This describes the functionality provided by the Python script I've created.

List of known issues is [here](github.com/DevangThakkar/SnatchV2/blob/master/issues.txt)

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