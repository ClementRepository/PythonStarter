print("Welcome to the roller coaster! Please tell me how tall you are.")
height=int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the roller coaster.")
else:
    print("You need to be taller to ride the roller coaster.")
    age=int(input("What is your age? "))
    if age <=12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
