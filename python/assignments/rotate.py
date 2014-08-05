"""Rotate Matrix

2. A large matrix is present within a file as CSV. Read this from file and 
form the matrix using lists or tuples. Rotate the matrix by 90 and 180 
degrees, and save them into 90.csv and 180.csv files respectively. [15 points]
"""
import csv

class Matrix(object):
	def __init__(self, infile):
		self.file = infile
		self.matrix = self.__parse()

	def __parse(self):
		matrix = []
		with open(self.file) as csvfile:
			lines = csv.reader(csvfile, delimiter=',')
			for line in lines:
				matrix.append(line)
		return matrix

	def rotate90(self):
		size = len(self.matrix[0])
		result = [item[:] for item in self.matrix[:]]
		for i in range(size):
			for j in range(size):
				result[i][j] = self.matrix[size-1-j][i]
		self.matrix = result

	def writecsv(self, filename):
		with open(filename, 'wb') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=',')
			for row in self.matrix:
				csvwriter.writerow(row)

if __name__ == "__main__":
	matrix = Matrix('/home/parthan/testcsv.csv')
	# rotate 90 and write into 90.csv
	matrix.rotate90()
	matrix.writecsv('/home/parthan/90.csv')
	matrix.rotate90()
	matrix.writecsv('/home/parthan/180.csv')

