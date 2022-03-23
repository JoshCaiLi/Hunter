#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/4/2022
#This program is easy assignment

s = input("Enter a string:")
ls = len(s)
for i in range(ls):
    print(s[0:i])
for i in range(ls):
    print(s[i:ls])
    
print('yo')
#  1.  Prompt the user to enter a string and call it s.
#2.  Let ls be the length of s.
#3.  For i from 0 upto ls-1:
#4.     Print s[0:i]
#5.  For i from 0 upto ls-1:
# 6.     Print s[i:ls]
# 5.  Print a closing statement