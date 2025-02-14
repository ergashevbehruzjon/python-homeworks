a=input("Enter first string: ")
b=input("Enter second string: ")
print("The second string '"+b+"' contains the first string '"+a+"'" if a in b else "The first string '"+a+"' contains the second string '"+b+"'" if b in a else "No, doesn't contain.")