"""Module définissant la classe Character pour le jeu."""

# Define the Character class.
class Character():
    """Représente un personnage dans le jeu."""
    # Define the constructor.
    def __init__(self, character_info, game, debug=False):
        """
        Initialise un personnage.
        
        :param character_info: dict contenant name, description, current_room, msgs
        :param game: instance du jeu
        :param debug: mode debug (par défaut False)
        """
        self.name = character_info['name']
        self.description = character_info['description']
        self.current_room = character_info['current_room']
        self.msgs = character_info['msgs']
        self.debug = debug
        self.game = game


    def move(self):
        """Déplace le personnage si nécessaire."""
        player = self.game.player
        if player.current_room.name == "Chapel":
            entry_room = next((room for room in self.game.rooms if room.name == "Entry"), None)
            if entry_room and self.current_room != entry_room:
                old_room = self.current_room
                self.current_room.characters.pop(self.name.lower(), None)
                self.current_room = entry_room
                entry_room.characters[self.name.lower()] = self
                if self.debug:
                    print(f"DEBUG: {self.name} s'est déplacé de {old_room.name} "
                          f"à {entry_room.name}")
                return True
        if self.debug:
            print(f"DEBUG: {self.name} est resté dans {self.current_room.name}")
        return False

    def get_msg(self):
        """Retourne le message actuel du personnage."""
        if not self.msgs:
            return "Ce personnage n'a rien à dire."
        if (self.game.player.current_room.name == "Chapel" and
            self.current_room.name == "Entry"):
            return ("Vous ne devriez pas être ici. "
                    "Mais vous en avez trop vu donc vous devez mourir")
        msg = self.msgs[self.msg_index]
        self.msg_index = (self.msg_index + 1) % len(self.msgs)
        return msg
def __str__(self):
    return f"{self.name} : {self.description}"
