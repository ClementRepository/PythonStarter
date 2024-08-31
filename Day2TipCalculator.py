print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
people=input("How many people to split the bill? ")
tip_percentage=int(tip) /int(100)
total_tip=bill * tip_percentage
total_bill=bill + total_tip
individual_bill=int(total_bill) / int(people)
final_amount=round(individual_bill, 2)
print(f'Each person should pay: ${final_amount}.')