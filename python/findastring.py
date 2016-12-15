'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/find-a-string
str = raw_input()
sub_str = raw_input()

matches = 0

if str.find(sub_str) == -1:
   print(0)
else:
   for i in range(0, len(str) - len(sub_str)+1):
      if str[i:i+len(sub_str)] == sub_str:
         matches += 1
   print(matches)