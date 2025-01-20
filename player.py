# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}
    
    # Define the move method.
    def move(self, direction):

        """Move the player in the specified direction."""
        
        # Ensure the direction is valid in the current room's exits.

        direction = direction.upper()
        if direction in self.current_room.exits:
            # Get the next room from the exits dictionary of the current room.
            next_room = self.current_room.exits[direction]
             # If the next room is None, print an error message and return False.
            if next_room is not None:
               self.current_room = next_room
               # Add the room name to the history
               self.history.append(self.current_room.name)
               return True
            else:
                print("\nAucune porte dans cette direction !\n")
                return False
        else:
            print(f"\nDirection '{direction}' non valide dans cette pièce.\n")
            return False
    
    def get_history(self):
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        for room_name in self.history[:-1]:
            history_str += f"     - {room_name}\n"
        return history_str.strip()

    def get_inventory(self):
       
       if len(self.inventory) == 0:
           print("Il n'y a rien dans votre inventaire.")
       else:
           print("Vous avez dans votre inventaire :")
           for item in self.inventory.values():
               print(f"    - {item.name} : {item.description} ({item.weight})")
    