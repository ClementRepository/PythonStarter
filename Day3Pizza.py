print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")
bill=0

#How much they need to pay based on their size choice.


if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Please type either S, M or L for your pizza size.")

#pepperoni bill

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

#final bill based on cheese

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}.")