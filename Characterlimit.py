name="Ja"
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters.")

elif len(name) > 50:
    print("Name must not exceed 50 characters.") #elif is for second condition

else:
    print("Name is acceptable.")