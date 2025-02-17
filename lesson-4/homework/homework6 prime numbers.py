print(2)
for i in range(3,101):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)