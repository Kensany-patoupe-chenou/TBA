"""Partie principale du jeux"""
# Description: Game class
# Import modules

from item import Item
from room import Room
from player import Player
from command import Command
from character import Character

class Game:
    """Classe principale du jeu."""
    # Constructor
    def __init__(self):
        """Initialise les attributs du jeu."""
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.debug = True
        self.npc = None
    # Setup the game
    def setup(self):
        from actions import Actions
        """Initialise le jeu en configurant les commandes,
          les pièces, les objets, le joueur et les PNJ."""
        self.actions = Actions()
        self.setup_commands()
        self.setup_rooms()
        self.setup_item()
        self.setup_player()
        self.setup_npcs()
    # L'affichage du DEBUG
    def debug_print(self, message):
        """Affiche un message de debug si le mode debug est activé."""
        if self.debug:
            print(f"DEBUG: {message}")
    def setup_commands(self):
        """
       Configure les commandes du jeu.

       Cette méthode initialise toutes les commandes disponibles dans le jeu,
       en définissant leur nom, description, action associée et nombre de paramètres.
       """
        # Setup commands
        self.commands["help"] = Command({"command_word":"help",
                                         "help_string":" : afficher cette aide",
                                         "action": self.actions.help,
                                         "number_of_parameters": 0})
        self.commands["quit"] = Command({"command_word":"quit", "help_string": " : quitter le jeu",
                                         "action": self.actions.quit,"number_of_parameters": 0})
        self.commands["go"] = Command({"command_word":"go",
                                       "help_string": " <direction> : se déplacer dans une "
                                      "direction cardinale (N, E, S, O)",
                                      "action": self.actions.go,"number_of_parameters": 1})
        self.commands["back"] = Command({"command_word":"back",
                                         "help_string": " : revenir à la pièce précédente",
                                         "action": self.actions.back,"number_of_parameters": 0})
        self.commands["look"] = Command({"command_word":"look",
                                         "help_string": ": observer l'environnement",
                                         "action": self.actions.look,"number_of_parameters": 0})
        self.commands["take"] = Command({"command_word":"take",
                                         "help_string": "nom_item : Pour prendre un objet",
                                         "action": self.actions.take,"number_of_parameters": 1})
        self.commands["drop"] = Command({"command_word":"drop",
                                         "help_string": "nom_item : Pour déposé un objet",
                                         "action": self.actions.drop,"number_of_parameters": 1})
        self.commands["check"] = Command({"command_word":"check",
                                          "help_string":": afficher votre inventaire",
                                          "action": self.actions.check,"number_of_parameters": 0})
        self.commands["talk"] = Command({"command_word":"talk",
                                         "help_string":" <personnage> : parler à un personnage",
                                         "action": self.actions.talk,"number_of_parameters": 1})
    def setup_rooms(self):
        """Configure le jeu en initialisant les pièces et les sorties."""
        # Setup rooms
        forest = Room("Forest", "dans une forêt lugubre."
                      " Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        entry = Room("Entry", "dans l'entrée du manoir."
                     " Vous êtes dans un hall sombre et effrayant.")
        self.rooms.append(entry)
        kitchen = Room("Kitchen", "dans une cuisine macabre."
                       " La piece est couverte de sang et le frigo est rempli d'organes humain.")
        self.rooms.append(kitchen)
        living_room = Room("Living room", "dans un salon maudit remplis d'âmes errante.")
        self.rooms.append(living_room)
        stairs= Room("Stairs", "devant la cage d'escalier.")
        self.rooms.append(stairs)
        manor_exit = Room("Manor exit", "devant la sortie mais la porte est fermée à clé."
                    " Vous voyez une voiture a l'extérieure qui"
                    " peut vous aider à sortir de la forêt.")
        self.rooms.append(manor_exit)
        office = Room("Office", "dans un bureau remplis d'armes."
                      " La pièce ressemble a une chambre de torture.")
        self.rooms.append(office)
        chapel = Room("Chapel", "dans une pièce ammenager come une chapelle."
                      "Elle est completement detruite")
        self.rooms.append(chapel)
        bedroom = Room("Bedroom", "dans une chambre plein de tache de sang."
                       " La chambre est completement rouge.")
        self.rooms.append(bedroom)
        self.rooms.extend([forest, entry, kitchen, living_room,
                            stairs, manor_exit, office, chapel, bedroom])
        # Create exits for rooms
        forest.exits = {"N" :entry, "E" : None, "S" : None, "O" : None,"U": None,"D": None}
        entry.exits = {"N" : None, "E" : living_room, "S" : None, "O" : kitchen,"U": None,"D": None}
        living_room.exits = {"N" : manor_exit, "E" : None,
                              "S" : None, "O" : entry,"U": None,"D": None}
        kitchen.exits = {"N" : stairs, "E" : entry, "S" : None, "O" : None,"U": None,"D": None}
        stairs.exits = {"N" : None, "E" : None, "S" : kitchen, "O" : None,"U" : office}
        office.exits = {"N" : None, "E" : bedroom, "S" : None, "O" : None,"U": None,"D": stairs}
        bedroom.exits = {"N" : chapel, "E" : None, "S" : None, "O" : office,"U": None,"D": None}
        chapel.exits = {"N" : None, "E" : None, "S" : bedroom, "O" : None,"U": None,"D": None}
        manor_exit.exits = {"N" : None, "E" : None,
                             "S" : living_room, "O" : None,"U": None,"D": None}
    def setup_item(self):
        """
        Configure les objets du jeu.

        Cette méthode crée tous les objets du jeu et les place 
        dans leurs pièces respectives.
        """
        # Setup inventory
        exit_key= Item("exit_key", "les clés de la porte de sortie", "1g")
        self.rooms[6].inventory_items["exit_key"] = exit_key
        flashlight = Item("flashlight", "une lampe pour tenter de térasser l'obscurité", "70g")
        self.rooms[1].inventory_items["flashlight"] = flashlight
        knife = Item("Knife", "un couteau tranchant pour un massacre amusant", "70g")
        self.rooms[2].inventory_items["Knife"] = knife
        gun = Item("Gun", "un fusil à pompe prêt à être dégainé à bout portant", "3.5kg")
        self.rooms[3].inventory_items["Gun"] = gun
        car_key = Item("car_key", "les clés de la voiture", "1g")
        self.rooms[8].inventory_items["car_key"] =car_key
    def setup_player(self):
        """
        Configure le joueur.

        Cette méthode initialise le joueur, lui demande son nom,
        et définit la pièce de départ ainsi que son historique.
        """
        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = self.rooms[0]
        self.player.history.append(self.player.current_room.name)
    def setup_npcs(self):
        """
        Configure le personnage non-joueur.
        
        Cette méthode crée le PNJ unique du jeu et 
        l'ajoute à sa pièce de départ.
        """
        # Creating the NPC
        forest_room = next((room for room in self.rooms if room.name == "Forest"), None)
        if forest_room:
            self.npc = Character({"name": "Anthony",
                              "description": "Un tueur en série à l'apparence de Jeffrey Dahmer",
                              "current_room": forest_room,
                              "msgs": ["Je chasse ma prochaine victime !"]},
                             game=self, debug=self.debug)
        forest_room.characters[self.npc.name.lower()] = self.npc
    # Play the game
    def play(self):
        """
        Démarre la boucle principale du jeu.

        Cette méthode initialise le jeu, affiche un message de bienvenue,
        et traite les commandes du joueur jusqu'à ce que le jeu soit terminé.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.npc.move()
            self.process_command(input("> "))
    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Traite une commande entrée par le joueur.

        Args:
            command_string (str): La commande entrée par le joueur 
            sous forme de chaîne de caractères.

        Cette méthode analyse la commande, vérifie si elle est valide,
        et exécute l'action correspondante.
        """
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0].lower()
        if command_word not in self.commands:
            print(f"\nDirection '{command_word}' non reconnue."
              " Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
        if command_word == "go" and self.player.current_room.name == "manor_exit":
            #vérifie si les objest nécessaires sont dans l'inventaire
            print("Avez-vous les clés de la sortie et de la voiture ?")
            answer=input("Répondez par oui ou non ")
            if answer == 'oui':
                print('vous avez gagné')
            else:
                print("vous n'avez pas toutes les clés. Trouvez les et revenez")
        else:
            command.action(self, list_of_words, command.number_of_parameters)
    # Print the welcome message
    def print_welcome(self):
        """
        Affiche le message de bienvenue et l'introduction du jeu.

        Cette méthode imprime un message de bienvenue personnalisé pour le joueur,
        décrit le contexte initial du jeu, et fournit des instructions de base.
        Elle affiche également la description de la pièce de départ du joueur.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'horreur et de survie !")
        print("Votre voiture est tombée en panne au bord d'une forêt "
              "lors d'un voyage et vous apercevez un manoir au loin.")
        print("Vous entrez dans la forêt pour rejoindre le manoir.")
        print("vous arrivez devant le manoir qui a l'air d'être abandoné,"
              "donc vous décidez de faire demi-tour")
        print("Malheureseument vous êtes perdue et decidez donc de "
              "retourner prendre refuge dans le manoir")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())
def main():
    """Fonction principale pour lancer le jeu."""
    Game().play()
if __name__ == "__main__":
    main()
