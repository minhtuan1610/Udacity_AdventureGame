import random
import time


def print_sleep(message):
    print(message)
    time.sleep(1)


def intro():
    print_sleep(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
        f"Rumor has it that a {enemy} is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep(
        f"In your hand you hold your trusty (but not very effective) {weapon}."
    )


def where_to():
    print_sleep("")
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    print_sleep("What would you like to do?")
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == "1":
        house()
    elif choice == "2":
        cave()


def house():
    print_sleep("You approach the door of the house.")
    print_sleep(
        f"You are about to knock when the door opens and out steps a {enemy}."
    )
    print_sleep(f"Eep! This is the {enemy}'s house!")
    combat(weapon)


def cave():
    global cave_visited
    global weapon
    global new_weapon
    print_sleep("You peer cautiously into the cave.")
    if cave_visited:
        print_sleep(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now."
        )
    elif cave_visited is False:
        print_sleep(
            "It turns out to be only a very small cave. "
            "Your eye catches a glint of metal behind a rock."
        )
        print_sleep(f"You have found the magical {new_weapon}!")
        print_sleep(
            f"You discard your silly old {weapon} and take the sword with you."
        )
        weapon = new_weapon
    cave_visited = True
    print_sleep("You walk back out to the field.")
    where_to()


def combat(weapon):
    print_sleep(f"The {enemy} attacks you!")
    if weapon == "dagger":
        print_sleep(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger."
        )
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Would you like to (1) fight or (2) run away?")
    if choice == "1":
        if weapon == "dagger":
            print_sleep(f"You do your best...")
            print_sleep(f"but your {weapon} is no match for the {enemy}.")
            print_sleep(f"You have been defeated!" "")
        else:
            print_sleep(
                f"As the {enemy} moves to attack, you unsheath your new sword."
            )
            print_sleep(
                f"The {weapon} shines brightly in your hand"
                " as you brace yourself for the attack."
            )
            print_sleep(
                f"But the {enemy} takes one look at your shiny new toy"
                " and runs away!"
            )
            print_sleep(
                f"You have rid the town of the {enemy}." " You are victorious!"
            )
    elif choice == "2":
        print_sleep(
            "You run back into the field."
            " Luckily, you don't seem to have been followed."
        )
        where_to()


def play_game():
    global game_state
    while game_state == "running":
        intro()
        where_to()
        game_state = play_again()


def play_again():
    choice = ""
    while choice not in ["y", "n"]:
        choice = input("Would you like to play again? (y/n)")
        if choice == "n":
            print_sleep("Thanks for playing! See you next time.")
            exit(0)
        elif choice == "y":
            print_sleep("Excellent! Restarting the game ...")
            return "running"


def game():
    while True:
        play_game()
        play_again()


game_state = "running"
while game_state == "running":
    enemies = ["troll", "wicked fairie", "pirate", "gorgon", "dragon"]
    enemy = random.choice(enemies)
    weapon = "dagger"
    cave_visited = False
    new_weapons = [
        "Sword of Ogoroth",
        "Sword of King Arthur",
        "Trident of Poseidon",
        "Power Ring of Green Lantern",
    ]
    new_weapon = random.choice(new_weapons)
    game()
