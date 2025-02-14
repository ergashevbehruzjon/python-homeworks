n=input("Enter a string: ")
for i in n:
    if i.isdigit():
        print("Yes, it has a digit.")
        break
else:
    print("No, it does not have a digit.")