# https://www.hackerrank.com/challenges/py-introduction-to-sets


def average(array):
	# your code goes here
	return sum(array) / len(array)

n = raw_input()
line = raw_input()
words = set(map(float, str(line).split(' ')))

print(words)
print(average(words))
