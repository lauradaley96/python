bill=int(input("Enter your bill:"))
paid=int(input("Enter amount paid:"))
balance = paid-bill
if balance >= 50:
    fifty=int(balance/50)
    print("£50:", fifty)
    balance = balance-(fifty*50)
if balance >= 20:
    twenty=int(balance/20)
    print("£20:", twenty)
    balance=balance-(twenty*20)
if balance >= 10:
    print ("£10:", 1)
    balance=balance-(ten*10)
if balance >=5:
    print("£5", 1)
    balance=balance-(five*5)
if balance >=2:
    two=int(balance/2)
    print("£2:", two)
    balance=balance-
if balance >=1:
    print("£1:", 1)