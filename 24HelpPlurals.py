#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/17/2022
#This program is

noun = input("Enter nouns: ")
print("You entered: ", noun)
words = noun.split()
print(words)
amount = len(words)
print(amount)
plural = noun.count('s ')

for i in noun:
    if i[-1] == "s":
        last = 1
    else:
        last = 0

plurals = plural + last
print(plurals)

fraction = plurals / amount
print(fraction)