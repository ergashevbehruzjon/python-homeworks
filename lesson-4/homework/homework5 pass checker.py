pswd=input("Enter a password: ")
if len(pswd)<8:
    print("Password is too short.")
elif pswd.lower()==pswd:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")