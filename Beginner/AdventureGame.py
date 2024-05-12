while True:
    print("\nWelcome to the Adventure!")
    print("You are in a dark room. There is a door to your right and left.")
    choice = input("Which one do you take? (left/right): ").lower()

    if choice == "right":
        print("You enter a room filled with treasure! You win!")
    elif choice == "left":
        print("You walk into a room with a hungry lion. Game Over!")
    else:
        print("Invalid choice! Game Over!")