# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []
    
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

        # Setup items

        guard_uniform = Item("uniforme", "un uniforme usé, posé sur une chaise en bois. Il semble avoir été porté récemment.", 1.5)
        self.items.append(guard_uniform)
        flashlight = Item("lampe torche", "une lampe torche moderne, posée sur une étagère métallique. Elle fonctionne encore.", 0.3)
        self.items.append(flashlight)
        locker_12_key = Item("clé du casier 12", "une clé rouillée, cachée sous l'uniforme. Elle ouvre un casier dans le coin de la pièce.", 0.1)
        self.items.append(locker_12_key)
        museum_map = Item("plan du musée", "un vieux plan du musée, annoté avec des passages secrets.", 0.2)
        self.items.append(museum_map)
        miniature_sarcophagus = Item("sarcophage miniature", "un petit sarcophage en bois doré, posé sur un autel. Il semble scellé.", 3.0)
        self.items.append(miniature_sarcophagus)
        anubis_amulet = Item("amulette d'Anubis", "une amulette en or, suspendue à une chaîne en argent. Elle brille faiblement.", 0.05)
        self.items.append(anubis_amulet)
        ancient_papyrus = Item("papyrus ancien", "un papyrus contenant des hiéroglyphes, caché sous le sarcophage miniature.", 0.1)
        self.items.append(ancient_papyrus)
        tribal_drum = Item("tambour tribal", "un tambour en peau de bête, posé contre un arbre. Il émet un son profond quand on le frappe.", 2.0)
        self.items.append(tribal_drum)
        medicinal_plant = Item("plante médicinale", "une plante aux feuilles vertes et brillantes, accrochée à une liane.", 0.2)
        self.items.append(medicinal_plant )
        jungle_map = Item("carte de la jungle", "une carte avec un chemin marqué en rouge, menant à une grotte cachée.", 0.1)
        self.items.append(jungle_map)
        broken_chain = Item("chaîne brisée", "une chaîne en fer rouillée, brisée en deux. Elle semble avoir été utilisée pour attacher quelqu'un.", 4.0)
        self.items.append(broken_chain)
        intimate_journal = Item("journal intime", "un journal usé, ouvert à une page où il est écrit : 'La liberté est une clé que personne ne peut voler.'", 0.5)
        self.items.append(intimate_journal)
        resistance_medal = Item("médaille de résistance", "une médaille gravée avec les mots : 'La vérité libère.'", 0.08)
        self.items.append(resistance_medal)
        hero_sword = Item("épée d'un héros", "une épée ancienne, posée sur un piédestal. Elle brille d'une lueur bleutée.", 3.0)
        self.items.append(hero_sword)
        magic_mirror = Item("miroir magique", "un miroir en argent, reflétant une image floue de la pièce.", 1.0)
        self.items.append(magic_mirror)
        philosophers_stone = Item("pierre philosophale", "une pierre qui émet une lumière douce, cachée derrière le miroir.", 0.5)
        self.items.append(philosophers_stone)
        ancient_telescope = Item("télescope ancien", "un télescope en laiton, pointé vers une constellation particulière.", 5.0)
        self.items.append( ancient_telescope)
        star_map = Item("carte des étoiles", "une carte du ciel nocturne, avec une étoile marquée en rouge.", 0.1)
        self.items.append(star_map)
        celestial_compass = Item("boussole céleste", "une boussole qui pointe toujours vers le nord et une étoile spécifique.", 0.3)
        self.items.append(celestial_compass)
        bloody_knife = Item("couteau ensanglanté", "un couteau de cuisine, posé sur une table en métal. Il est taché de rouge.", 0.4)
        self.items.append(bloody_knife)
        killer_journal = Item("journal du tueur", "un journal ouvert, rempli de notes et de dessins inquiétants.", 0.6)
        self.items.append(killer_journal)
        handcuff_key = Item("clé de menottes", "une clé cachée dans une fissure du mur, derrière une photo. Elle porte le numéro 666.", 0.05)
        self.items.append(handcuff_key)

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
