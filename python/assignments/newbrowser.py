__author__ = 'Parthan'


import fileinput, sys

if __name__ == "__main__":
	tc = 0
	for line in fileinput.input():
		if not tc:
			tc = line
			continue
		website = line.strip()
		website = website.split('www.')[1]
		lesscnt = 0
		for c in ['a','e','i','o','u']:
			lesscnt += website[:-4].count(c)
		ans = str(len(website)-lesscnt) + "/" + str(len(line.strip())) + "\n"
		sys.stdout.write(ans)
