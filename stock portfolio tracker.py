#Stock Portfolio Tracker
d = {
    "TATA":390,
    "MFR":1000,
    "PNB":200,
    "WIPRO":147,
    "ITC":500
    }
print("Choose your stocks from the following: TATA, MFR, PNB, WIPRO, ITC")
print()
investment=0
dict = {}
while True:
    stk_name = input("In which stock you have invested: ").upper()
    quantity = int(input("How many stocks you have purchased: "))
    print()
    ans = input("any other stock(Yes/No) : ")
    investment+=d[stk_name]*quantity
    dict[stk_name]=quantity
    if ans in ['No', 'NO', 'no']:
        break
print()
print("Total investment you have made is: ", investment)

with open("stock.txt", 'w') as stock:
    stock.write(f"Total investment value is {investment}")
    print("Investment value saved in file stock.txt")
