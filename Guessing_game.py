secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('Guess: '))
    guess_count +=1 #+= means guess count=guess count +1. If first_name is "James" and last_name is "Thomas" then first_name+=last_name has an output of James Thomas.
    if guess==secret_number:
        print("You won!")
        break #stops the loop
else: 
    print('Sorry you failed.')