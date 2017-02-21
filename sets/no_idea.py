# https://www.hackerrank.com/challenges/no-idea

n, m = raw_input().split()

arra = raw_input().split()
a_set = set(map(int, str(raw_input()).split()))
b_set = set(map(int, str(raw_input()).split()))

print(sum([(int(i) in a_set) - (int(i) in b_set) for i in arra]))
