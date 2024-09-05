print("Welcome to the roller coaster! Please tell me how tall you are.")
height=int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the roller coaster.")
    age=int(input("What is your age? "))
    if age <=12:
        bill =5
        print("Child tickets are $5.")
    elif age <=18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3
        #adds 3 dollars to bill

    print(f"Your final bill is {bill}")
else: 
    print("You can't ride the roller coaster.")