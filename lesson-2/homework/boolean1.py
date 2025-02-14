u=input("Enter a username: ")
p=input("Enter a password: ")
print("Both are empty" if not (bool(u) and bool(p)) else "Username is empty" if not bool(u) else "Password is empty" if not bool(p) else "Both are not empty")