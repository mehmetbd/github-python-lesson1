print("====================")
print("===cash despenser===")
print("====================")
total120=total100=total90=total70=total50=total30=total10=total5=0
costomers=0
dispensed=0
service=True
while service:
    name=input("what is your name:")
    dispense=input(f"how many money are you dispensing {name}:")
    if dispense==0:
        print("nothing enter the amount \n")
        continue
    print(f"how much {dispense} do you want {name}:")
    left=dispense
    value=1
    while value <= 8:
        if value==1:much=120
        elif value==2:much=100
        elif value==3:much=90
        elif value==4:much=70
        elif value==5:much=50
        elif value==6:much=30
        elif value==7:much=10
        else:much=1
        count=left//much
        if count==0:
            print("how much do you want:")
            left-=count*much
            if much==120:total120+=count
            elif much==100:total100+=count
            elif much==90:total90+=count
            elif much==70:total70+=count
            elif much==50:total50+=count
            elif much==30:total30+=count
            elif much==10:total10+=count
            else:total5+=count
        value+=1
    costomers+=1
    dispensed+=1
    print("money collecting completed")
    next_costomer=input("will there will be another coustomer coming:")
    if next_costomer=="yes":
        service=False
print(f"\nCustomers served : {costomers}")
print(f"Total dispensed : {dispensed} units")
print("ATM session closed. Goodbye!")