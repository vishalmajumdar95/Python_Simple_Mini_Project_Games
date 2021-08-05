

#############=> Frist ATM <=###########

print(" 2000000 rs in our acount ")

print("WELCOME TO NAVGURUKUL BANK")
more=True
while more==True:
    print('''
    1.insert the card
    if you will put 1 so code will go next line
    ''')
    a=int(input(" "))
    if a==1:
        print(" Chose Language : ")
    else:
        print("invalid card")
        break
    print('''
     1.Hindi
     2.English
     ''')
    a=int(input(" "))
    if a==1:
        print("Hindi")
    else:
        print("English")
    print('''
    1.current acount
    2.saving acount
    ''')
    a=int(input(" "))
    if a==1:
        print("current acount")
    else:
        print("saving acount")
    PIN=int(input("enter your pin : "))
    if PIN==1234:
        print('''
        1.Balance Enqaury
        2.Withdraw Cash
        3.Deposite
        4.Statement
        5.exit
        ''')
    else:
        print("You enter wrong password \ncheck your PIN carefully and then enter your pin:")
        continue
    z=int(input())
    if z==1:
        print("2000000")
        a = input("Want to enter more? y/n >>>")
        if a!="y":
                more = False
    elif z==2:
        amount=int(input("enter amount : "))
        print("Transaction succsesfull")
        print("your remaining balance is",2000000-amount)
        a = input("Want to enter more? y/n >>>")
        if a!="y":
            more = False
    elif z==3:
        print("enter your deposit amount : ")
        amount=int(input("enter your amount : "))
        print("your currently amount is", 2000000+amount)
        a = input("Want to enter more? y/n >>>")
        if a!="y":
            more = False
    elif z==4:
        print("print your statement")
        a = input("Want to enter more? y/n >>>")
        if a!="y":
            more = False
    elif z==5:
        print("THANK YOU FOR COMING HERE")
        a = input("Want to enter more? y/n >>>")
        if a!="y":
            more = False
    else:
        print("chutiya sahi se typing kar")
        a = input("Want to enter more? y/n >>>")
        if a!="y":
            more = False
else:
    print("wrong pin")
    
