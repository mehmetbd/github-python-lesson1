#Operator precedence 1
a=67
b=911
c=21
d=28
e=61
f=(a+b)*(c*d)//e
print("value:",f)
#Operator precedence 2
game="FC Mobile"
username="mehmet hasan 2016 april"
team="spain"
if game=="FC Mobile" and username=="mehmet hasan 2016 april" and team == "spain" or game=="minecraft" and username=="photoman" and team=="nothing":
    print("welcome back to FC Mobile")
else:
    print("welcome back to minecraft")
#Operator numerator
numerator=int(input("enter numerator:"))
denomirator=int(input("enter dinominator:"))
if numerator%denomirator==0:
    print("\n",numerator,"is disivle by",denomirator)
else:
    print("\n",numerator,"is not disivle by",denomirator)
#Operator mean
people=38
wrong_numeber=36
right_number=56
total_number=40
sum=people*total_number
right_sum=sum-((right_number-wrong_numeber))
people_count=right_sum/total_number
print("the right value of people are:",people_count)                