# Description: Game class

# Import modules

from item import Item
from room import Room
from player import Player
from command import Command

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):
        from actions import Actions

        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        help = Command("help", " : afficher cette aide", Actions.help, 0, "help_alias")
        look = Command("look", ": observer l'environnement", Actions.look, 0)
        self.commands["look"] = look

        take= Command("take", "nom_item : Pour prendre un objet", Actions.take, 1)
        self.commands["take"] = take

        drop = Command("drop", "nom_item : Pour déposé un objet", Actions.drop, 1)
        self.commands["drop"] = drop

        check = Command("check", ": afficher votre inventaire", Actions.check, 0)
        self.commands["check"] = check


        
        # Setup rooms

        forest = Room("Forest", "dans une forêt lugubre. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        entry = Room("Entry", "dans l'entrée du manoir. Vous êtes dans un hall sombre et effrayant.")
        self.rooms.append(entry)
        lampe = Item('lampe', 'une lampe pour tenter de térasser l\'obscurité', '70g')
        entry.inventory_items["lampe"] =lampe



        kitchen = Room("Kitchen", "dans une cuisine macabre. La piece est couverte de sang et le frigo est rempli d'organes humain.")
        self.rooms.append(kitchen)
        couteau = Item('couteau', 'un couteau tranchant pour un massacre amusant', '70g')
        kitchen.inventory_items["couteau"] = couteau


        living_room = Room("Living room", "dans un salon maudit remplis d'âmes errante.")
        self.rooms.append(living_room)
        fusil = Item('fusil', 'un fusil à pompe prêt à être dégainé à bout portant', '3.5kg')
        living_room.inventory_items["fusil"] = fusil



        stairs= Room("Stairs", "devant la cage d'escalier.Vous  avez deja fouiller toute les pièces et il n'y a pas la clé de la sortie. Vous devez monter pour trouver la clé de la sortie et la voiture.")
        self.rooms.append(stairs)
        exit = Room("Exit", "devant la sortie mais la porte est fermée à clé. Vous voyez une voiture a l'extérieure qui peut vous aider à sortir de la forêt.")
        self.rooms.append(exit)
        office = Room("Offfice", "dans un bureau remplis d'armes . La pièce ressemble a une chambre de torture.")
        self.rooms.append(office)
        clé_sortie= Item('clé_sortie', 'les clés de la porte de sortie', '1g')
        office.inventory_items["clé_sortie"] = clé_sortie


        chapel = Room("Chapel", "dans une pièce ammenager come une chapelle.Elle est completement detruite")
        self.rooms.append(chapel)
        bedroom = Room("Bedroom", "dans une plein de tache de sang. La chambre est completement rouge.")
        self.rooms.append(bedroom)
        clé_voiture = Item('lé_voiture', 'les clés de la voiture', '1g')
        bedroom.inventory_items["clé_voiture"] = clé_voiture

        # Create exits for rooms

        forest.exits = {"N" :entry, "E" : None, "S" : None, "O" : None,"U": None,"D": None}
        entry.exits = {"N" : None, "E" : living_room, "S" : None, "O" : kitchen,"U": None,"D": None}
        living_room.exits = {"N" : exit, "E" : None, "S" : None, "O" : entry,"U": None,"D": None}
        kitchen.exits = {"N" : stairs, "E" : entry, "S" : None, "O" : None,"U": None,"D": None}
        stairs.exits = {"N" : None, "E" : None, "S" : kitchen, "O" : None,"U" : office}
        office.exits = {"N" : None, "E" : bedroom, "S" : None, "O" : None,"U": None,"D": stairs}
        bedroom.exits = {"N" : chapel, "E" : None, "S" : None, "O" : office,"U": None,"D": None}
        chapel.exits = {"N" : None, "E" : None, "S" : bedroom, "O" : None,"U": None,"D": None}
        exit.exits = {"N" : None, "E" : None, "S" : living_room, "O" : None,"U": None,"D": None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = forest
        self.player.history.append(self.player.current_room.name)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            

        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0].lower()

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nDirection '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'horreur et de survie !")
        print("Votre voiture est tombée en panne au bord d'une forêt lors d'un voyage et vous apercevez un manoir au loin.")
        print("Vous entrez dans la forêt pour rejoindre le manoir.")
        print("vous arrivez devant le manoir qui a l'air d'être abandoné,donc vous décidez de faire demi-tour")
        print("Malheureseument vous êtes perdue et decidez donc de retourner prendre refuge dans le manoir")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())


def main():
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
