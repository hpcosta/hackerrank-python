'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/capitalize

str = raw_input()

sentence = ''
flag = True
for c in str:
   if (c == ' '):
      flag = True
   else:
      if flag:
         flag = False
         if c.isalpha():
            c = c.upper()         
  
   sentence +=c

print(sentence)