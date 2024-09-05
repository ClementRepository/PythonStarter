print("You just finished your test.")
math_score=(int(input("What math score did you get? ")))
english_score=(int(input("What english score did you get? ")))

if math_score >=90:
    print("You're good at math.")
    if english_score >=90:
        print("Wow, you're good at math and english!")

else:
    print("You need to study more.")
