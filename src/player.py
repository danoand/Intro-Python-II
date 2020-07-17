# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    # Construct a Player object instance
    def __init__(self, name, room):
        self.name = name
        self.room_current = room
    
    def __str__(self):
        return "Player Name: {name}, Current Room: {room_current}".format(
            name=self.name,
            room_current=self.room_current)

    