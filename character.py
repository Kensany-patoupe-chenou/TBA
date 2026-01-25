import random

class Character:
    """
    Classe représentant un personnage non-joueur (PNJ) dans le jeu.

    Attributs :
        name (str) : Le nom du personnage.
        description (str) : La description du personnage.
        current_room (Room) : Le lieu où se trouve le personnage.
        msgs (list[str]) : Une liste de messages à afficher lorsque le joueur interroge le PNJ.
    """
    
   

    def __init__(self, name, description, current_room, msgs, movement_type):
        """
        Initialise un personnage non-joueur.

        Args :
            name : Le nom du personnage.
            description : La description du personnage.
            current_room : La pièce où se trouve le personnage.
            msgs : Une liste de messages que le PNJ peut dire.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.msg_index = 0 
        self._first_meet = True
        self.movement_type = movement_type
        
    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le personnages non joueur.

        Returns:
            str: Une représentation du personnages non joueur au format "(nom, description)".
        """
        return f"{self.name}:{self.description}"
    
    
    def get_msg(self,current_room):
        
        """Retourne le message actuel du personnage."""
        if not self.msgs:
            return "Ce personnage n'a rien à dire."

        msg = self.msgs[self.msg_index]
        self.msg_index = (self.msg_index + 1) % len(self.msgs)
        return msg
    
    def move(self, player_current_room=None):
        """
        Déplace le PNJ aléatoirement dans une pièce adjacente.
        Retourne True si le PNJ s'est déplacé, False sinon.
        """
        
        if self.movement_type == "random":
            # Logique pour Gripsou
            if random.choice([True, False]):
                possible_rooms = [room for room in self.current_room.exits.values() if room is not None]
                if possible_rooms:
                    new_room = random.choice(possible_rooms)
                    if self.name in self.current_room.characters:
                        del self.current_room.characters[self.name]
                    self.current_room = new_room
                    self.current_room.characters[self.name.lower()] = self
                    return True
        elif self.movement_type == "companion":
            # Logique pour Tingen
            if self.current_room != player_current_room:
                if self.name in self.current_room.characters:
                    del self.current_room.characters[self.name]
                self.current_room = player_current_room
                self.current_room.characters[self.name.lower()] = self
                return True
        return False
    
    