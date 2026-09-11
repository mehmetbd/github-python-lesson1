print("======================== ")
print("===welcome to gamestop===")
print("=========================")
low_price=0
high_price=0
expensive_price=0
quality=fps=0
version=0
customers_left=0
total_income=00
serving=True
while serving:
    customer=input("what is your name:")
    games=int(input(f"how much games do you buy {customer}"))
    if games<=0:
        print("item:none")
        continue
    print(f"what are they {customer}")
    customer_count=0
    item_count=1
    while games<= item_count:
        items_name=input("enter the items name:")
        cost=int(input("enter the how much it cost:"))
        many=int(input("enter how much did you buy:"))
        if cost<=0:
            print("cost:none")
            continue
        total=cost*many
        print(f"{items_name}: {many}x{cost}={total}")
        customers+=many
        if cost<50:
            low_price+=many
        elif cost<=100:
            high_price+=many
        else:
            expensive_price+=many
        num+=1
            