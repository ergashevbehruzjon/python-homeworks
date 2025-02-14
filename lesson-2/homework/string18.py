n=input("Enter a sentence: ").split()
if n[0]==n[-1]:
    print("The first and last words are the same.")
else:
    print("It starts with",n[0],"and ends with",n[-1])