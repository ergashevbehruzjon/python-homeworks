s=input("Enter a string: ")
# s="hello"
# s="assalom"
# s="abcabcdabcdeabcdefabcdefg"
new=''
v='aeiou'
excepted=''
j=1
for i in range(len(s)):
    if j==3:
        if s[i] in v or s[i] in excepted or i>len(s)-2:
            new+=s[i]
            j=2
        else:
            excepted+=s[i]
            new+=s[i]+'_'
            j=0
    else:
        new+=s[i]
    j+=1
print(new)