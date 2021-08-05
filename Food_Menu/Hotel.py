
 ##### HOTEL FOOD MENU ######


print(" WELCOME TO BABA KA DHABA ")
a=True
while a==True:
    print("1breakfast","2lunch","3snack","4dinner") 
    user=int(input())
    if user==1:
        print("1chai", "2poha", "3macroni", "4friedrice", "5sewai")
        user1=int(input(" "))
        if user1==1:
            print("10rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==2:
            print("20rs half plate, 40rs full plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==3:
            print("30rs half plate, 5ors full plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==4:
            print("40rs half plate, 70rs full plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==5:
            print("20rs half plate, 40rs full plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        else:
            print("invalid input")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
    elif user==2:
        print("1.chole bhature", "2.kadhi rice", "3.biryani", "4.rajma rice", "5.dal rice")
        user1=int(input(" "))
        if user1==1:
            print("50rs per plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==2:
            print("half plate 40rs, full plate 70rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==3:
            print("80rs per plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==4:
            print("half plate 50rs, full plate 80rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==5:
            print("60rs per plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        else:
            print("invalid input")
    elif user==3:
        print("1.maggie", "2.pizza", "3.soup", "4.chowmin", "5.burger")
        user1=int(input(" "))
        if user1==1:
            print("25rs per plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==2:
            print("99rs medium size")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==3:
            print("20rs per cup")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==4:
            print("half plate 30rs, full plate 50rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==5:
            print("30rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        else:
            print("invalid input")
    elif user==4:
        print("1.egg roti", "2.chicken roti", "3.mutton roti", "4.chicken corma roti", "5.chicken biryani")
        user1=int(input(" "))
        if user1==1:
            print(" 4 eggs 4 roti 100rs plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==2:
            print("half plate chicken 4 roti 150rs plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==3:
            print("half plate mutton 4 roti 200rs plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==4:
            print("half plate chicken corma 4 roti 200rs plate")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
        elif user1==5:
            print("half plate 80rs full plate 150rs")
            back=input("Back type >>>y/n")
            if back!="y":
                a=False
    else:
        print("user not chose")

