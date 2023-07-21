print("welcome to Paytm")
class recharge_mobile:
    def __init__(self, type, mobile_number, operator, amount):
        self.type = type
        self.mobile_number = mobile_number
        self.operator = operator
        self.amount = amount

    def show(self):
        print("~~~~~~~$~~~~~~~~~~")
        print("Type : ", self.type)
        print("Mobile number :", self.mobile_number)
        print("Operator :", self.operator)
        print("Amount :", self.amount)
        print("~~~~~~~~$~~~~~~~~~")


recharge_mobile1 = recharge_mobile("prepaid", 6280888589, "jio", 299)
recharge_mobile2 = recharge_mobile("postpaid",8264098161, "airtel", 1000)

recharge_mobile1.show()
recharge_mobile2.show()
