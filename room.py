# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory_items={}
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    

    def get_inventory_items(self):
        if len(self.inventory_items) == 0:
            print("Il n'y a rien ici dans cette pièce")
        else:
            print("La pièce contient :")
            for item in self.inventory_items.values():
                print(f"    - {item.name} : {item.description} ({item.weight})")

    

    def take(self, name_item, player):
        
       if name_item in self.inventory_items:
            item = self.inventory_items[name_item]
            player.inventory[name_item] = item  # Ajoute l'item à l'inventaire du joueur
            del self.inventory_items[name_item]  # Retire l'item de la pièce
            print(f"Vous avez pris {item.name}.")


    def drop(self, name_item, player):
       
       if name_item in player.inventory:
            item = player.inventory[name_item]
            self.inventory_items[name_item] = item  # Ajoute l'item à la pièce
            del player.inventory[name_item]  # Retire l'item de l'inventaire du joueur
            print(f"Vous avez déposé {item.name}.")

    def look(self):
       # Looking for item in the room
       if len(self.inventory_items) == 0:
           print("Il n'y a rien dans cette pièce.")
       else:
            if len(self.inventory_items) > 0:
                print("La pièce contient les objets suivants :")
                for item in self.inventory_items.values():
                    print(f"    - {item.name} : {item.description} ({item.weight})")
            # Looking for NPC in the room
            if self.characters:
                for character in self.characters.values():
                    print(f"\n        - {character.name} : {character.description}\n")
            else:
                print("Il n'y a person ici.")