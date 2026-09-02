total_chores=5
og_count=total_chores
print(f"you have {og_count} chores,complete them")
complete=0
choice=1
while choice <= total_chores:
    if choice == 1:next_thing="clean your room"
    elif choice == 2:next_thing="beat one game"
    elif choice == 3:next_thing="do your project"
    elif choice == 4:next_thing="do your homework"
    else:
        print("eat your dinner")
    chores=input(f"did you {next_thing}(yes/maybe/not)")
    if chores=="yes":
        complete+=1
        choice+=1
        print("beat a game")
    elif chores=="maybe":
        print("ok then beat a game")
    else:
        print("finish it")
    print("chores reamining",total_chores-choice)
print("everything has been completed well done")    