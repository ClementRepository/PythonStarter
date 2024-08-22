command=""
while command.lower() != "quit": #prevents quit in caps
    command=input("> ").lower()
    if command == "start":
        print("Car started.")
    elif command == "stop":
        print("Car stopped.")
    elif command == "accelerate":
        print("Car sped up.")
    elif command == "help":
        print("""
        start - start the car
        stop - stop the car
        accelerate - make the car go faster
        quit - quit the game
        """)
    elif command == "quit":
        print("Game ended. Thanks for playing.")
        break
    else:
        print("Sorry, I don't understand that.")