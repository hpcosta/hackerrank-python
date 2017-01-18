'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/python-mutations

str = raw_input()
line = raw_input()
line.strip()
index = int(line.split(' ')[0].strip())
c = line.split(' ')[1].strip()

l = list(str)
l[index] = c
print(''.join(l))
