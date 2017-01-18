
# https://www.hackerrank.com/challenges/python-string-split-and-join


def split_and_join(line):
	# writ your code here
	words = line.split(" ")
	return "-".join(words)