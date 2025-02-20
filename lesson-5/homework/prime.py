def is_prime(num):
    if num<2:return False
    for i in range(2,int(num**.5)+1):
        if num%i<1:return False
    return True
num=int(input("Enter a positive integer: "))
print(is_prime(num))