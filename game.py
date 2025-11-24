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
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", " : afficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history 
        back = Command("back"," : revenir à la pièce précédente",Actions.back,0)
        self.commands["back"] = back

        
        # Setup rooms

        egypt = Room("Égypte antique", " une salle plongée dans la pénombre, décorée de hiéroglyphes dorés et de statues majestueuses de pharaons. Au centre, trône un immense sarcophage de Toutânkhamon, brillamment orné.")
        self.rooms.append(egypt)
        jumanji = Room("Jumanji", " une salle décorée comme une jungle, avec des lianes artificielles, des plantes exotiques et des tambours diffusés par des haut-parleurs.")
        self.rooms.append(jumanji)
        slavery = Room("Esclavage", " une salle silencieuse remplie de chaînes anciennes, de documents historiques et d’objets témoignant d’une époque sombre.")
        self.rooms.append(slavery)
        mythology = Room("Mythologie et légendes", " une pièce mystique où des statues de créatures mythiques semblent vous observer dans la pénombre.")
        self.rooms.append(mythology)
        astronomy = Room("Astronomie", " un dôme étoilé où des planètes flottent en suspension et où les constellations brillent autour de vous.")
        self.rooms.append(astronomy)
        locker_room = Room("Vestiaire du gardien", " un petit local encombré de casiers métalliques, de lampes torches et d’un uniforme posé sur une chaise.")
        self.rooms.append(locker_room)
        serial_killer = Room("Serial Killer", " une salle froide et inquiétante, où des preuves criminelles sont exposées derrière des vitrines sous une lumière rougeâtre.")
        self.rooms.append(serial_killer)
        lower_hall = Room("Hall inférieur", " un vaste hall aux colonnes imposantes, éclairé par une forte lumière provenant du plafond.")
        self.rooms.append(lower_hall)
        upper_hall = Room("Hall supérieur", " un espace ouvert donnant vue sur les étages du musée, avec des balustrades anciennes et des vitrines éclairées.")
        self.rooms.append(upper_hall)

        # Create exits for rooms

        egypt.exits = {"N" : None, "E" : None, "S" : upper_hall, "O" : None,"U": None,"D": None}
        jumanji.exits = {"N" : serial_killer, "E" : None, "S" : None, "O" : lower_hall,"U": None,"D": None}
        slavery.exits = {"N" : None, "E" : lower_hall, "S" : None, "O" : None,"U": None,"D": None}
        mythology.exits = {"N" : None, "E" :upper_hall, "S" : None, "O" : None,"U": None,"D": None}
        astronomy.exits = {"N" : None, "E" : None, "S" : None, "O" : upper_hall,"U": None,"D": None}
        locker_room.exits = {"N" : None, "E" : lower_hall, "S" : None, "O" : None,"U": None,"D": None}
        serial_killer.exits = {"N" : None, "E" : None, "S" : jumanji, "O" : lower_hall,"U": None,"D": None}
        lower_hall.exits = {"N" : None, "E" : serial_killer, "S" : None, "O" : slavery,"U": upper_hall,"D": None}
        upper_hall.exits = {"N" : egypt, "E" : astronomy, "S" : None, "O" : mythology,"U": None,"D": lower_hall}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = locker_room
        self.player.history.append(locker_room)

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

        if command_string.strip() == "":
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
