"""Treasure Hunt

Treasure Matrix

52	54	32	45	51
43	45	25	33	11
24	53	55	15	12
11	42	35	34	14
51	21	22	31	42

The game of treasure hunt is played with the above treasure matrix, to find the cell in which the treasure is hidden. The map is a 5x5 array, containing numbers between 11 and 55. The ten’s digit of the number represents the row and the one’s digit represents the column, of the cell containing the next clue. Starting at the top-left cell, i.e. (1,1), the game is to follow the cells until the treasure cell is found. The treasure cell is the one whose value is same as it’s coordinates. 

The output should be a list of cells visited (the numbers), ending at the treasure cell.

The program should take a 5x5 array (list or tuple) and return the output. Ideally, the program should be able to run as a script taking the input matrix as its arguments.
"""


import sys

def process_matrix(input):
	if isinstance(input, str):
		input = input[1:-1].split('],')
		input = [ item.replace('[','').replace(']','').split(',') for item in input ]
		input = [ [item for item in row] for row in input]
	return input

def find_treasure(matrix):
	curr_pos = [0,0]
	cur_val = treasure = 0
	path = []

	while True:
		cur_val = matrix[curr_pos[0]][curr_pos[1]]
		# positions are indexed 0, so add 1 to form the string that matches with value
		curr_pos_str = ''.join([str(curr_pos[0]+1), str(curr_pos[1]+1)])
		
		# add to the path traversed
		path.append(curr_pos_str)
		
		# if current postion matches current value in that position, treasure is found
		if cur_val == curr_pos_str:
			treasure = cur_val
			break

		# else, the current value becomes the next position to go and check
		curr_pos = [int(cur_val[0])-1, int(cur_val[1])-1]

	return path, treasure

if __name__ == "__main__":
	# uncomment to get matrix as input argument
	#args = sys.argv
	#input = args[1]

	# comment not to test this matrix but get real input
	input = '[52,54,32,45,51],[43,45,25,33,11],[24,53,55,15,12],[11,42,35,34,14],[51,21,22,31,42]'

	matrix = process_matrix(input)
	path, treasure = find_treasure(matrix)
	print "Path traversed: ", ' >> '.join(path), '\n'
	print "Treasure: ", treasure