# Description: Game class
DEBUG = True

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []
        self.next_turn=False
    
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
        look = Command("look", " : affiche les objets présents dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : permet de récupérer un objet présent dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : permet deéposé un objet présent dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("ckeck", " : permet de voir les objets présent dans l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", " <nom> : un personnage vous parle", Actions.talk, 1)
        self.commands["talk"] = talk
        charge = Command("charge", " : charge le beamer avec la pièce actuelle", Actions.charge, 1)
        self.commands["charge"] = charge
        use = Command("use", " : utilise le beamer pour se téléporter", Actions.use, 1)
        self.commands["use"] = use
        quest = Command("quest", " : voir les détails à propos d'une quête", Actions.quest, 1)
        self.commands["quest"] = quest
        activate = Command("activate", " : permet d'activer une quête spécifique", Actions.activate, 1)
        self.commands["activate"] = activate
        rewards = Command("rewards", " : permet de voir toutes les récompenses gagnées par le joueur", Actions.rewards, 0)
        self.commands["rewards"] = rewards
        quests = Command("quests", " : permet de lister les quêtes", Actions.quests, 0)
        self.commands["quests"] = quests

        
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
        flashlight = Item("lampe_torche", "une lampe torche moderne, posée sur une étagère métallique. Elle fonctionne encore.", 0.3)
        self.items.append(flashlight)
        locker_12_key = Item("clé_du_casier_12", "une clé rouillée, cachée sous l'uniforme. Elle ouvre un casier dans le coin de la pièce.", 0.1)
        self.items.append(locker_12_key)
        museum_map = Item("plan_du_musée", "un vieux plan du musée, annoté avec des passages secrets.", 0.2)
        self.items.append(museum_map)
        miniature_sarcophagus = Item("sarcophage_miniature", "un petit sarcophage en bois doré, posé sur un autel. Il semble scellé.", 3.0)
        self.items.append(miniature_sarcophagus)
        anubis_amulet = Item("amulette_d_Anubis", "une amulette en or, suspendue à une chaîne en argent. Elle brille faiblement.", 0.05)
        self.items.append(anubis_amulet)
        ancient_papyrus = Item("papyrus_ancien", "un papyrus contenant des hiéroglyphes, caché sous le sarcophage miniature.", 0.1)
        self.items.append(ancient_papyrus)
        tribal_drum = Item("tambour_tribal", "un tambour en peau de bête, posé contre un arbre. Il émet un son profond quand on le frappe.", 2.0)
        self.items.append(tribal_drum)
        medicinal_plant = Item("plante_médicinale", "une plante aux feuilles vertes et brillantes, accrochée à une liane.", 0.2)
        self.items.append(medicinal_plant )
        jungle_map = Item("carte_de_la_jungle", "une carte avec un chemin marqué en rouge, menant à une grotte cachée.", 0.1)
        self.items.append(jungle_map)
        broken_chain = Item("chaîne_brisée", "une chaîne en fer rouillée, brisée en deux. Elle semble avoir été utilisée pour attacher quelqu'un.", 4.0)
        self.items.append(broken_chain)
        intimate_journal = Item("journal_intime", "un journal usé, ouvert à une page où il est écrit : 'La liberté est une clé que personne ne peut voler.'", 0.5)
        self.items.append(intimate_journal)
        resistance_medal = Item("médaille_de_résistance", "une médaille gravée avec les mots : 'La vérité libère.'", 0.08)
        self.items.append(resistance_medal)
        hero_sword = Item("épée_d_un_hero", "une épée ancienne, posée sur un piédestal. Elle brille d'une lueur bleutée.", 3.0)
        self.items.append(hero_sword)
        magic_mirror = Item("miroir_magique", "un miroir en argent, reflétant une image floue de la pièce.", 1.0)
        self.items.append(magic_mirror)
        philosophers_stone = Item("pierre_philosophale", "une pierre qui émet une lumière douce, cachée derrière le miroir.", 0.5)
        self.items.append(philosophers_stone)
        ancient_telescope = Item("télescope_ancien", "un télescope en laiton, pointé vers une constellation particulière.", 5.0)
        self.items.append( ancient_telescope)
        star_map = Item("carte_des étoiles", "une carte du ciel nocturne, avec une étoile marquée en rouge.", 0.1)
        self.items.append(star_map)
        celestial_compass = Item("boussole_céleste", "une boussole qui pointe toujours vers le nord et une étoile spécifique.", 0.3)
        self.items.append(celestial_compass)
        bloody_knife = Item("couteau_ensanglanté", "un couteau de cuisine, posé sur une table en métal. Il est taché de rouge.", 0.4)
        self.items.append(bloody_knife)
        killer_journal = Item("journal_du_tueur", "un journal ouvert, rempli de notes et de dessins inquiétants.", 0.6)
        self.items.append(killer_journal)
        handcuff_key = Item("clé_de_menottes", "une clé cachée dans une fissure du mur, derrière une photo. Elle porte le numéro 666.", 0.05)
        self.items.append(handcuff_key)
        beamer = Item("beamer","Un objet mystérieux capable de vous téléporter.", 0.05)
        self.items.append(beamer)
        beamer.charge = False
        beamer.charged_room = None


        # Setup room inventory

        egypt.inventory[miniature_sarcophagus.name] = miniature_sarcophagus
        egypt.inventory[anubis_amulet.name] = anubis_amulet
        egypt.inventory[ancient_papyrus.name] = ancient_papyrus

        jumanji.inventory[tribal_drum.name] = tribal_drum
        jumanji.inventory[medicinal_plant.name] = medicinal_plant
        jumanji.inventory[jungle_map.name] = jungle_map

        slavery.inventory[broken_chain.name] = broken_chain
        slavery.inventory[intimate_journal.name] = intimate_journal
        slavery.inventory[resistance_medal.name] = resistance_medal
        slavery.inventory[beamer.name] = beamer

        mythology.inventory[hero_sword.name] = hero_sword
        mythology.inventory[magic_mirror.name] = magic_mirror
        mythology.inventory[philosophers_stone.name] = philosophers_stone

        astronomy.inventory[ancient_telescope.name] = ancient_telescope
        astronomy.inventory[star_map.name] = star_map
        astronomy.inventory[celestial_compass.name] = celestial_compass

        locker_room.inventory[guard_uniform.name] = guard_uniform
        locker_room.inventory[flashlight.name] = flashlight
        locker_room.inventory[locker_12_key.name] = locker_12_key
        locker_room.inventory[museum_map.name] = museum_map

        serial_killer.inventory[bloody_knife.name] = bloody_knife
        serial_killer.inventory[killer_journal.name] = killer_journal
        serial_killer.inventory[handcuff_key.name] = handcuff_key


        
        # Setup PNJ
        
        gripsou = Character("Gripsou", 
                            " le spectre du musée, gardien des œuvres et des souvenirs.", 
                            lower_hall, ["Salut, voyageur… \n"
                                        "Je suis Gripsou, ancien conservateur de ce musée.\n"
                                        "Quand l’au-delà m’a appelé, j’ai détourné le regard,\n"
                                        "incapable d’abandonner ce lieu que j’aimais tant,\n"
                                        "et auquel j’ai dédié ma vie.\n"
                                        "Depuis, mon âme y demeure.\n"],
                            movement_type="random")
        lower_hall.characters["Gripsou"] = gripsou
        gripsou._first_meet = True
        print(gripsou)
        
        tingen = Character("Tingen",
                           " l’alter ego créé par Gripsou, né de son amour profond pour le musée.",
                           lower_hall,["Salut, voyageur… \n"
                                       "Je suis Tingen, née de l'amour profond de Gripsou pour ces lieux \n"
                                       "Je te servirai de compagnon dans cette aventure et resterai à tes côtes \n"
                                       "C’est à travers ma voix que tu pourras entendre la sienne, \n"
                                       "et à travers moi que ses secrets te seront révélés..\n"],
                           movement_type="companion")
        lower_hall.characters["Tingen"] = tingen
        print(tingen)
       


        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = locker_room
        self.player.history.append(locker_room)

        def _setup_quests(self):
            """Initialize all quests."""
        exploration_quest = Quest(
            title="Grand Explorateur",
            description="Explorez le musé jusqu'à atteindre la salle où les étoiles racontent le temps.",
            objectives=[ "Visiter Astronomie"],
            reward="Titre de Grand Explorateur"
        )

        find_quest = Quest(
            title="Trouvaille ancestrale",
            description="Récupérez la pierre philosophale dans le panthéon des dieux et des héros.",
            objectives=["take pierre philosophale"],
            reward="Petite augmentation de l'espérance de vie"
        )

        awareness_quest = Quest(
            title="Avide de savoir",
            description="Parlez avec Tingen pour en savoir plus sur qui elle est.",
            objectives=["talk Tingen"],
            reward="Augmentation du QI"
        )


        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(find_quest)
        self.player.quest_manager.add_quest(awareness_quest)

    # Play the game
    def play(self):
        
        self.setup()
        self.print_welcome()
        self._lower_hall_visited = False
        # Loop until the game is finished
        while not self.finished:
                        # Get the command from the player
            self.next_turn=False
            self.process_command(input("> "))
            if self.win():
                print("\n🎉 Félicitations ! Vous avez terminé toutes les quêtes !\n")
                print("""
            Toutes les quêtes sont accomplies.
            Tous les fragments du passé ont trouvé leur place.

            Gripsou s’avance, lentement.
            Pour la première fois, il sourit.

            « Les clés me sont rendues…
            Le musée peut enfin se taire. »

            Les murs cessent de murmurer.
            Les objets redeviennent immobiles.
            Les ombres se figent.

            Vous avez compris l’âme du musée.
            Vous savez désormais qu’il n’était pas maudit…
            mais vivant.

            Avant de disparaître, Gripsou vous fait une dernière demande :
            ne jamais révéler ce que vous avez vu ici.

            Certains secrets doivent rester enfermés,
            et disparaître dans les méandres de l’ombre.
            """)
                print("\n🏆 Vous avez gagné la partie.\n")
                self.finished = True
                break

            if self.loose():
                self.finished = True
                print("💥 GAME OVER 💥")
                break
            
            if self.player.current_room.name == "Hall inférieur" and not self._lower_hall_visited:
                self._lower_hall_visited = True
                if "Gripsou" in self.player.current_room.characters:
                    gripsou = self.player.current_room.characters["Gripsou"]
                    print(f"\n{gripsou.name} dit : {gripsou.get_msg(self.player.current_room)}")
                
                        
            if self.next_turn:
                for room in self.rooms:
                    for character in list(room.characters.values()):
                        if character.movement_type == "random":
                            if self.player.current_room.name != "Hall inferieur":
                                moved = character.move()
                                if DEBUG and moved:
                                    print(f"{character.name} s'est déplacé vers la pièce {character.current_room.name}.\n")
                        elif character.movement_type == "companion":
                            moved = character.move(self.player.current_room)
                            if DEBUG and moved:
                                print(f"{character.name} vous a suivi dans la pièce {character.current_room.name}.\n")   
        return None
        
    def win(self):
        """
        Vérifie si le joueur a gagné la partie.
        Le joueur gagne si toutes les quêtes sont complétées.
        """
        quests = self.player.quest_manager.get_all_quests()
        return all(quest.is_completed for quest in quests)

    def loose(self):
        """
        Vérifie si le joueur a perdu la partie.
        """
        current_room = self.player.current_room
        inventory = self.player.inventory

        if current_room.name == "Serial Killer" and "plante_médicinale" not in self.player.inventory.keys():
            print("\n💀 Vous êtes entré dans une salle mortelle sans protection...")
            print("""
        Tingen renverse accidentellement un poison mortel
        dans la salle Serial Killer.

        L’air devient irrespirable.

        Sans la plante médicinale pour vous sauver,
        votre corps cède.

        Le musée vous engloutit
        dans son silence éternel.
        """)
            return True

        return False

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
        print("Entrez 'help' si vous avez besoin d'aide.\n")
        print("Vous vous réveillez en sursaut dans les vestiaires,\n" 
                "le cœur battant, le souffle court, la tête lourde et l’esprit embrumé.\n"
                "Les souvenirs de votre journée de travail sont fragmentés,\n"
                "comme effacés, engloutis par l’obscurité.\n"
                "Le silence du musée est total, presque étouffant.\n"
                "En tentant de vous relever, une lumière étincelante jaillit soudain du\n" 
                "hall du musée, déchirant l’obscurité et projetant des ombres inquiétantes sur les murs.\n"
                "Quelque chose ne tourne pas rond. Le musée n’est plus endormi… il vous observe.\n"
                "Avant d’oser sortir, une chose est certaine : \n"
                "Vous devez vous armer de courage.")
        print(self.player.current_room.get_long_description())
        
def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
