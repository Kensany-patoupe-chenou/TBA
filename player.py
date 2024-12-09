# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):

        """Move the player in the specified direction."""
        
        # Ensure the direction is valid in the current room's exits.

        direction = direction.upper()
        
        if direction not in self.current_room.exits:
            print(f"\nDirection '{direction}' non valide dans cette pièce.\n")
            return False

        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    