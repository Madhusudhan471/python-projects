from datetime import datetime

name=input("Enter Your Name: ")
#Lists oF items
lists='''
Rice     Rs:20/kg
Sugar    Rs:30/kg
Salt     Rs:20/kg
Oil      Rs:80/kg
Paneer   Rs:120/kg
Maggie   Rs:50/Kg
Boost    Rs:90/Each
Colgate  Rs:85/Each
'''
print(lists)

#Declaration of methods 
price      =  0 #first price always be 0
finalamount=  0
pricelist  =  []
totalprice =  0 #in starting Stage total price also Zero
Final_price=  0
ilist      =  []
qlist      =  []
plist      =  []


#rates of different Items in Super market
items= {
    'Rice    Rs':20,
    'Sugar   Rs':30,
    'Salt    Rs':20,
    'Oil     Rs':80,
    'Paneer  Rs':120,
    'Maggie  Rs':50,
    'Boost   Rs':90,
    'Colgate Rs':85,
}

#To Enquiry list of items in super Market
option = int(input("For List Of Items Press 1(one)"))
if option==1:
    print(lists)
for i in range(len(items)):
    input_1=int(input("If You Want to Buy Press 1 or Press 2 for exit "))
    if input_1==2:
        break
    if input_1==1:
        item=input("Please Enter your items :")
        quantity=int(input("Enter Your Quantity :"))
        
        if item in items.keys():
            price=quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice +=price
            ilist.append(item)
            qlist.append(quantity)
            qlist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry You Entered item is not Availble")
    else:
        print("You Entered Wrong Number ")
    for_bill=input("Need Bill Type Yes or No")
    if for_bill == "Yes" :
        pass
    if finalamount != 0:
        print(25* "=","Global Super Market",25*"=")
        print(28*" ","Banglore")
        print("Name : ",name , 30* " ","Date:",datetime.now())
        print(75*"-.")
        print("S NO",8*" ",'items',8*" ")
        for i in range(len(pricelist)):
            print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
        print(75*'-.')
        print(50*" ","Total Amount:","Rs",totalprice)
        print("Gst Amount",50* " ",gst)
        print(75*'-.')
        print(50*" ","final amount :","Rs",finalamount)
        print(75*'-.') 
        print(50*" ","Thanks For visiting ")
        print(75*"-.")         