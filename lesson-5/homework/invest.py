def invest(amount,rate,years):
    for i in range(years):
        amount*=1+rate
        print(f"year {i+1}: ${amount:.2f}")
# invest(100,.05,4)
init_amount=int(input("Enter the initial amount: "))
rate=float(input("Enter the interest rate: "))
years=int(input("Enter the number of years: "))
invest(init_amount,rate,years)