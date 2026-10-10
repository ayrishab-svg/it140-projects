"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


current_room = 'Great Hall'

while current_room != 'exit':
    print('You are in the', current_room)

    command = input('Enter a command: ').strip().lower()

    if command == 'exit':
        current_room = 'exit'
    elif command.startswith('go '):
        direction = command[3:].strip()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print('Invalid direction. Try again.')
    else:
        print('Invalid command. Try again.')
print('Thanks for playing!')
