"""Shadows of Kurohana Academy: IT-140 Project Two text adventure."""

# Ayrisha Miller


def show_instructions():
    """Explain the objective and the commands the player can enter."""
    print("Shadows of Kurohana Academy")
    print(
        "Goal: Collect all 6 enchanted items before confronting the Shadow Master."
    )
    print("Move commands: go north, go south, go east, go west")
    print("Collect an item: get <item name> (example: get Moonstone)")
    print("Warning: Entering the Rooftop without all 6 items ends the game.")


def show_status(current_room, inventory, rooms):
    """Display the current room, available exits, inventory, and any room item."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    print(f"Items collected: {len(inventory)}/6")

    if "item" in rooms[current_room]:
        print(f"Item available: {rooms[current_room]['item']}")

    directions = ("north", "south", "east", "west")
    exits = [
        direction
        for direction in directions
        if direction in rooms[current_room]
    ]
    print(f"Available directions: {', '.join(exits)}")
    print("----------------------")


def main():
    """Run the game until the player wins or encounters the villain too early."""
    # Room directions and items match the Project One academy map.
    rooms = {
        "Main Hall": {"north": "Rooftop", "west": "Courtyard"},
        "Courtyard": {
            "north": "Cafeteria",
            "east": "Main Hall",
            "item": "Moonstone",
        },
        "Cafeteria": {
            "north": "Music Room",
            "south": "Courtyard",
            "item": "Protective Charm",
        },
        "Music Room": {
            "east": "Art Room",
            "south": "Cafeteria",
            "item": "Silver Bell",
        },
        "Art Room": {
            "east": "Science Lab",
            "west": "Music Room",
            "item": "Enchanted Paintbrush",
        },
        "Science Lab": {
            "south": "Library",
            "west": "Art Room",
            "item": "Crystal Vial",
        },
        "Library": {
            "north": "Science Lab",
            "west": "Rooftop",
            "item": "Ancient Spellbook",
        },
        "Rooftop": {"south": "Main Hall", "east": "Library"},
    }

    current_room = "Main Hall"
    inventory = []
    game_over = False

    show_instructions()

    # Input: player enters a movement or get-item command.
    # Output: updated status, feedback, or a final win/loss message.
    while not game_over:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()

        if command.startswith("go "):
            direction = command[3:].strip()
            if (
                direction in ("north", "south", "east", "west")
                and direction in rooms[current_room]
            ):
                current_room = rooms[current_room][direction]
                print(f"You moved {direction} to the {current_room}.")
            else:
                print("Invalid direction. Try an available direction.")

        elif command.startswith("get "):
            requested_item = command[4:].strip()
            room_item = rooms[current_room].get("item")

            if room_item and requested_item == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(f"You collected the {room_item}!")
            elif room_item is None:
                print("There is no item to collect in this room.")
            else:
                print("Invalid item. Please try again.")

        else:
            print("Invalid command. Please try again.")

        # Check if the player encounters the Shadow Master.
        if current_room == "Rooftop":
            if len(inventory) == 6:
                print(
                    "Congratulations! You collected all 6 enchanted items and defeated the Shadow Master!"
                )
            else:
                print("The Shadow Master caught you! GAME OVER!")

            print("Thanks for playing Shadows of Kurohana Academy.")
            game_over = True

if __name__ == "__main__":
    main()
