# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        forest = Room("Forest", "dans une forêt lugubre. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        entry = Room("Entry", "dans l'entrée du manoir. Vous êtes dans un hall sombre et effrayant.")
        self.rooms.append(entry)
        kitchen = Room("Kitchen", "dans une cuisine macabre. La piece est couverte de sang et le frigo est rempli d'organes humain.")
        self.rooms.append(kitchen)
        living_room = Room("Living room", "dans un salon maudit remplis d'âmes errante.")
        self.rooms.append(living_room)
        stairs= Room("Stairs", "devant la cage d'escalier.Vous  avez deja fouiller toute les pièces et il n'y a pas la clé de la sortie. Vous devez monter pour trouver la clé de la sortie et la voiture.")
        self.rooms.append(stairs)
        exit = Room("Exit", "devant la sortie mais la porte est fermée à clé. Vous voyez une voiture a l'extérieure qui peut vous aider à sortir de la forêt.")
        self.rooms.append(exit)
        office = Room("Offfice", "dans un bureau remplis d'armes . La pièce ressemble a une chambre de torture.")
        self.rooms.append(office)
        chapel = Room("Chapel", "dans une pièce ammenager come une chapelle.Elle est completement detruite")
        self.rooms.append(chapel)
        bedroom = Room("Bedroom", "dans une plein de tache de sang. La chambre est completement rouge.")
        self.rooms.append(bedroom)

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

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
