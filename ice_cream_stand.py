name=input("enter your name coustomer:")
def greetings(name):
    print("===================================")
    print(f"===welcome to the ice cream shop {name}===")
    print("===any flavour you want is here====")
    print("===================================")
greetings(name)
price=float(input("enter how much dollars do you buy:"))
cones=int(input("enter the much cones do you want to sold:"))
def calculator(price,cones):
    return price * cones
print("you have to pay:",round(calculator(price,cones),2))
paid=float(input("enter how much are you payed:"))
def calculator2(paid):
    return paid-calculator(price,cones)
paying=round(calculator2(paid),2)
print("you are paying about ",paying)
print("thx for buying ice creaams.")