#1st activity
print("half pyramid")
star=int(input("enter many star as possible:"))
for i in range(star):
    for j in range(i+1):
        print("*",end=" ")
    print()
#2nd activity
print("floyed half triangle")    
number=1
coloum=int(input("enter many number as possible:"))
for i in range(coloum):
    for j in range(i+1):
        print(number,end=" ")
        number+=1
    print()
#final activity
rows=int(input("enter much rows for diamond shape as possible:"))
if rows%2==0:
    half_rows=int(rows/2)
else:
    half_rows=int(rows/2)+1
s=half_rows-1
for i in range(1,half_rows+1):
    for j in range(1,s+1):
        print(end=" ")
    s=s-1
    num=1
    for j in range(2*i-1):
        print(end=str)(num)
    print()    