# https://www.hackerrank.com/challenges/symmetric-difference?h_r=next-challenge&h_v=zen


one = raw_input()
a = raw_input()
two = raw_input()
b = raw_input()
n = set(map(int, str(a).split()))
m = set(map(int, str(b).split()))

union = n.union(m)
intersection = n.intersection(m)
symmetric_difference = union.difference(intersection)

for i in sorted(symmetric_difference):
	print(i)
