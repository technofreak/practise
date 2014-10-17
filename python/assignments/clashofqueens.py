"""Clash of Queens

Queen is a power piece in the chessboard, able to move and attack across the row, the column or diagonally. A chessboard can be represented as a 8x8 array, with 1 in the array represents a Queen on the square and 0 in the array represents an unoccupied square. Given locations of two Queens on the chessboard, write a program to represent the board with the Queens on it and to indicate whether the two Queens could attack each other in this position.

The input to the program with be a tuple of positions of the two queens, as a number between 11 and 88. The output of the program should be a representation of the chessboard with the queens and a True/False whether they could attack each other.

Ideally, the program should be able to run as a script taking the input as an argument.

For example, in the below shown chessboard Queen A is at 34. If Queen B is at 37, 64 or 78, it represents a position where both the queens can attack each other. If Queen B is at 57, it represents a position where the two queens cannot attack each other.

	|	1	2	3	4	5	6	7	8
______________________________________
1	|	0	0	0	0	0	0	0	0
2	|	0	0	0	0	0	0	0	0
3	|	0	0	0	A	0	0	B	0
4	|	0	0	0	0	0	0	0	0
5	|	0	0	0	0	0	0	B	0
6	|	0	0	0	B	0	0	0	0
7	|	0	0	0	0	0	0	0	B
8	|	0	0	0	0	0	0	0	0

"""

import sys

def check_attack(pos1, pos2):
	# collect row and column positions of two queens
	rpos1, cpos1 = int(pos1[0]), int(pos1[1])
	rpos2, cpos2 = int(pos2[0]), int(pos2[1])

	# straight check: whether on same row or column
	if rpos1 == rpos2 or cpos1 == cpos2:
		return True

	# if not lets check for diagonal attack
	diagattack = False

	# initialize at queen 1 pos, lets step back by a row and column
	rpos, cpos = rpos1, cpos1
	while rpos>0 and cpos>0:
		rpos, cpos = rpos-1, cpos-1
		# if queen 2 is found in this square, then diagonal attack is possible
		if rpos == rpos2 and cpos == cpos2:
			diagattack = True
			break

	# if diagonal attack is True, then queens attack each other
	if diagattack: return True
	
	# intialize back at queen 1 pos, lets step forward by a row and column
	rpos, cpos = rpos1, cpos1
	while rpos<9 and cpos<9:
		rpos, cpos = rpos+1, cpos+1
		# if queen 2 is found in this square, then diagonal attack is possible
		if rpos == rpos2 and cpos == cpos2:
			diagattack = True
			break

	# if diagonal attack is True, then queens attack each other, else not
	if diagattack:
		return True
	else:
		return False

def build_checssboard(pos1, pos2):
	# collect row and column positions of two queens
	rpos1, cpos1 = int(pos1[0]), int(pos1[1])
	rpos2, cpos2 = int(pos2[0]), int(pos2[1])

	# build empty chessboard
	cboard = [ [0 for j in xrange(8)] for i in xrange(8) ]

	# position the queens at the right place
	cboard[rpos1-1][cpos1-1] = 1
	cboard[rpos2-1][cpos2-1] = 1

	return cboard 


if __name__ == "__main__":
	args = sys.argv
	file, q1pos, q2pos = args
	attack = check_attack(q1pos, q2pos)
	cboard = build_checssboard(q1pos, q2pos)
	print "Chessboard Representation:\n"
	for row in cboard:
		print ' | ' + ' | '.join([str(item) for item in row]) + ' | '
	if attack:
		print "\nResult: Clash of Queens is possible."
	else:
		print "\nResult: Clash of Queens is not possible."

