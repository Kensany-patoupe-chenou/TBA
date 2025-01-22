
import random

# Define the Character class.
class Character():
       
    # Define the constructor.
    def __init__(self, name,description,current_room,msgs,game,debug=False):
        self.name = name
        self.description = description
        self.current_room =current_room
        self.msgs = msgs
        self.debug = debug
        self.msg_index = 0
        self.game = game

    def move(self):
        player = self.game.player
        if player.current_room.name == "Chapel":
            entry_room = next((room for room in self.game.rooms if room.name == "Entry"), None)
            if entry_room and self.current_room != entry_room:
                self.current_room.characters.pop(self.name.lower(), None)
                self.current_room = entry_room
                entry_room.characters[self.name.lower()] = self
                if self.debug:
                    print(f"DEBUG: {self.name} s'est déplacé de {old_room.name} à {new_room.name}")
                    return True
        if self.debug:
            print(f"DEBUG: {self.name} est resté dans {self.current_room.name}")
        return False
    
    def get_msg(self):
        if not self.msgs:
            return "Ce personnage n'a rien à dire."
        
        # Verifying if the plyer is in the chapel and the  NPC in the entry
    
        if self.game.player.current_room.name == "Chapel" and self.current_room.name == "Entry":
            return "Vous ne devriez pas être ici. Mais vous en avez trop vu donc vous devez mourir"
                
        msg = self.msgs[self.msg_index]
        self.msg_index = (self.msg_index + 1) % len(self.msgs)  # Passer au message suivant de manière cyclique
        return msg

    def __str__(self):
      return f"{self.name} :{self.description}"