#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 2/25/2022
#This program is the difficult assignment
word = input("Enter a word:")
codedWord = ""
for ch in word:
    offset = ord(ch) - ord('a') + 13 #how many letters past 'a'
    wrap = offset % 26  #if larger than 26, wrap back to 0
    newChar = chr(ord('a') + wrap)  #compute the new letter
    print(chr(ord('a') + wrap))    #print the wrap & new letter
    codedWord = codedWord + newChar #add the newChar to the coded word

print("Your coded word is:",codedWord)
