# print("zomato casestudy")


"""
Get 50% OFF up to ₹100
Valid on total value of items worth ₹159 or more.
WELCOME50


Get 30% OFF up to ₹75 and ₹75 Paytm cashback using Paytm
Valid on total value of items worth ₹299 or more.
ZOMPAYTM


Get 30% OFF up to ₹90 using Simpl
Valid on total value of items worth ₹199 or more
SIMPLPARTY


Get 30% OFF up to ₹155 using SBI Credit Cards
Valid on total value of items worth ₹399 or more
SBITREATS
"""


print("Welcome to zomato ")
total_amount=(int(input("enter total amount: ")))
SIMPLPARTY=(total_amount*0.3)
if (SIMPLPARTY>90):
    SIMPLPARTY=90
WELCOME50=(total_amount*0.5)
if (WELCOME50 > 100):
    WELCOME50 = 100
SBITREATS=(total_amount*0.3)
if (SBITREATS>155):
    SBITREATS=155
ZOMPAYTM=(total_amount*0.3)
if (ZOMPAYTM>75):
    ZOMPAYTM=75
if (total_amount<199):
    print("Sorry you cannot apply promocode")
    print("you have to pay : ", total_amount)
else:
    print("you are eligible to  apply promocode")
    if (total_amount>=199 and total_amount<299):
        print("you can apply 2 promocodes ")
        print("WELCOME50 --> You will get 50% OFF UPTO Rs 100")
        print("SIMPLPARTY --> You will get 30% OFF UPTO  Rs 90")
        print("\n")
        print("SUGGESTION --> WELCOME50 will give you more discount ")

        promocode=input("Enter your promocode :")
        if (promocode=="WELCOME50"):
            total_amount=total_amount-WELCOME50
            print("your total amount is :", total_amount)
        elif (promocode=="SIMPLPARTY"):
            total_amount=total_amount-SIMPLPARTY
            print("Your total amount is : ", total_amount)
        else:
            print("You apply invalid promocode you have to pay :", total_amount)

    elif (total_amount>=299 and total_amount<399):
        print("you can apply 3 promocodes ")
        print("ZOMPAYTM --> you will get 30% OFF UPTO Rs 75 and you will also get PAYTM cashback of Rs 75 ")
        print("WELCOME50 --> You will get 50% OFF UPTO Rs 100")
        print("SIMPLPARTY --> You will get 30% OFF UPTO  Rs 90")
        print("\n")
        print("SUGGESTION --> ZOMPAYTM will give you more discount")
        promocode = input("Enter your promocode :")
        if (promocode == "WELCOME50"):
            total_amount = total_amount - WELCOME50
            print("your total amount is :", total_amount)
        elif (promocode == "SIMPLPARTY"):
            total_amount = total_amount - SIMPLPARTY
            print("Your total amount is : ", total_amount)
        elif (promocode=="ZOMPAYTM"):
            total_amount = total_amount - ZOMPAYTM
            print("your total amount is " , total_amount)
            print("you will get Rs 75 cashback in PAYTM")
        else:
            print("You apply invalid promocode you have to pay :", total_amount)
    else:
        print("you can apply 4 promocodes ")
        print("ZOMPAYTM --> you will get 30% OFF UPTO Rs 75 and you will also get PAYTM cashback of Rs 75 ")
        print("WELCOME50 --> You will get 50% OFF UPTO Rs 100")
        print("SIMPLPARTY --> You will get 30% OFF UPTO  Rs 90")
        print("SBITREATS --> you will get 30% OFF UPTO Rs 155")
        print("\n")
        if (total_amount>500):
            print("SBITREATS will give you more discount ")
        else:
            print(" ZOMPAYTM will give you more discount")
        promocode = input("Enter your promocode :")
        if (promocode == "WELCOME50"):
            total_amount = total_amount - WELCOME50
            print("your total amount is :", total_amount)
        elif (promocode == "SIMPLPARTY"):
            total_amount = total_amount - SIMPLPARTY
            print("Your total amount is : ", total_amount)
        elif (promocode == "ZOMPAYTM"):
            total_amount = total_amount - ZOMPAYTM
            print("your total amount is :", total_amount)
            print("you will get Rs 75 cashback in PAYTM")
        elif (promocode == "SBITREATS"):
            total_amount = total_amount - SBITREATS
            print("your total amount is : ", total_amount)
        else:
            print("You apply invalid promocode you have to pay :", total_amount)




