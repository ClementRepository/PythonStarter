price=1000000
good_credit=True #They have good credit


if good_credit:
    down_payment=price * .1

else:
    down_payment=price * .2
print(f"Down payment: {down_payment}")