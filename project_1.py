def item_a(choice):
    if choice == "a":
        return "ladder"# Returns "ladder" if choice is 'a'
    elif choice == "b":
        return "net"# Returns "net" if choice is 'b'
    elif choice == "c":
        return "ship"# Returns "ship" if choice is 'c'
    else:
        return None
    
def item_b(choice):
    if choice == "a":
        return "rock"# Returns "rock" if choice is 'a'
    elif choice == "b":
        return "water"# Returns "water" if choice is 'b'
    elif choice == "c":
        return "fire"# Returns "fire" if choice is 'c'
    else:
        return None
    
def item_c(choice):
    if choice == "a":
        return "sea animals"# Returns "seaanimals" if choice is 'a'
    elif choice == "b":
        return "wild animals"# Returns "wildanimals" if choice is 'b'
    elif choice == "c":
        return "domestic animals"# Returns "domestic animals" if choice is 'c'
    else:
        return None

def work_1(item_found):
    if item_found == "ladder":
        print("you took the ladder and use it for cutting fruits")
        print("your work is finished so you return the ladder")
    elif item_found == "net":
        print("you took the net and use it for fishing")
        print(" you catch some fish with your net and earn money")

    elif item_found == "ship":
        print("you are sailing the ship in the sea")
        print("you are going to find the biggest treasure named as One Piece! with your ship ")

    else:
        print("Sorry, invalid item.")

def work_2(item_found):
    if item_found == "rock":
        print("you took the rock and use it to build your new house")
    
    elif item_found == "water":
        print("you are so thirsty so drink enouugh amount of water")

    elif item_found == "fire":
        print("you are stuck in the fire room as soon as possible get of the room")

    else:
        print("Sorry, invalid item.")

def work_3(item_found):
    if item_found == "sea animals":
        print("you have sea animals you can take that animal and you can open an aquirium")
    
    elif item_found == "wild animals":
        print("The  wild animals are so terror as soon as possible get of the room ")

    elif item_found == "domestic animals":
        print("you are having domestic animals so you can open new pet shop")

    else:
        print("Sorry, invalid item.")

def enter_room(door):
    if door == 1:
        print("You are entering the yellow door room.")
        choice = input("Choose a choice (a, b, or c): ")
        found_item = item_a(choice)
        if found_item:
            print("Congratulations! You found a", found_item + "!")
            work_1(found_item)
        else:
            print("Sorry, invalid choice.")

    elif door == 2:
        print("You are entering the pink door room.")
        choice = input("Choose a choice (a, b, or c): ")
        found_item = item_b(choice)
        if found_item:
            print("Congratulations! You found a", found_item + "!")
            work_2(found_item)
        else:
            print("Sorry, invalid choice.")

    elif door == 3:
        print("You are entering the red door room.")
        choice = input("Choose a choice (a, b, or c): ")
        found_item = item_c(choice)
        if found_item:
            print("Congratulations! You found a", found_item + "!")
            work_3(found_item)
        else:
            print("Sorry, invalid choice.")

    else:
        print("Invalid door number!")

doors = ["yellow", "pink", "red"]
#entering the door
door = int(input("Enter a random door number:\n 1 for yellow \n 2 for pink \n 3 for red:\n\t"))
enter_room(door)

