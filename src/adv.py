import pprint
from room import Room
from player import Player

# Helper objects
pp = pprint.PrettyPrinter(indent=2)

# Declare all the rooms
print("Starting up... and setting up some cool rooms")
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
print("Now... linking rooms together\n\n")
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# print('DEBUG: rooms are:')
# pp.pprint(room)

# Make a new player object that is currently in the 'outside' room.
playa = Player("Johnny", "outside")
game_input = None
# Write a loop that:
#
while game_input != "q":
    print("Player: {name} is currently in room: {room_current}".format(
        name=playa.name,
        room_current=room[playa.room_current].name
    ))
    print("({description})\n\n".format(description=room[playa.room_current].description))

    game_input=input("What should {name} do now? ".format(name=playa.name))

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if game_input == "q":
    print("Thanks for playing... quitting the game now.")
