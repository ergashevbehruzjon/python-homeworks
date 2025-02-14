n=input("Enter a string: ")
v='aeiou'
s=sum(i in v for i in n)
print("The number of vowels in the string is",s)
print("The number of consonants in the string is",len(n)-s)