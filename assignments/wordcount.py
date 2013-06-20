"""Word Count

Given a file containing text (paragraphs), find the count of each word within 
the file excluding punctuation marks. Print the result in a pretty format.
"""


class WordCounter:
	def __init__(self, infile):
		self.file = infile
		self.parsed_items = self.__parse()

	def __parse(self):
		f = open(self.file)
		parsed_items = []
		for line in f:
			items = line.replace('\n','').split()
			for item in items:
				if item.isalnum():
					parsed_items.append(item)
		return parsed_items

	def count_all(self):
		return len(self.parsed_items)

	def count_unique(self):
		return len(set(self.parsed_items))

	def count_by_word(self):
		worddict = {}
		for item in self.parsed_items:
			if item not in worddict:
				worddict[item] = 1
			else:
				worddict[item] += 1
		return worddict

if __name__ == "__main__":
	import sys
	infile = sys.argv[1]
	c = WordCounter(infile)
	print "Count of all words:", c.count_all()
	print "Count of unique words:", c.count_unique()
	print "Count of all words:"
	for word, cnt in c.count_by_word().iteritems():
		print word, "=>", cnt
