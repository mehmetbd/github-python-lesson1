total_count=4
original_count=total_count
completed=0
left=1
while left<=total_count:
    if left==1:
        next_count="did you have ferrari"
    elif left==2:
        next_count="did you have a PC"
    elif left==3:    
        next_count="did you have a PS5"
    else:
        print("invalid syntex")
    ans=input(f"{next_count}(yes/maybe/not)")
    if ans=="yes":
        completed+=1
        left+=1
        print("ok")
    elif ans=="maybe":
        print("check it again")
    else:
        print("dont have it")
        print("Q/A left",total_count-completed)
print("Q/A finished")   