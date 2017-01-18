'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/string-validators


str = raw_input()
print(any(c.isalnum() for c in str))
print(any(c.isalpha() for c in str))
print(any(c.isdigit() for c in str))
print(any(c.islower() for c in str))
print(any(c.isupper() for c in str))
   
