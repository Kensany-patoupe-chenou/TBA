# Define the Player class.
from quest import QuestManager
class Player():
    """
    Class Player

    Represents the player in the game. The player has a name and is located
    in a current room.
        Attributs:
            self.name(str): name of player
            current_room(Room): Room objetc
            self.history :
            self.inventory :
            self.max_weight :

        Methods :
            move(self, direction): Return True if the move
            is successful, otherwise print an error message and return False.
        
        >>> from room import Room
        >>> from player import Player
        >>> swamp = Room("Swamp", "Un marécage sombre et ténébreux.")
        >>> tower = Room("Tower", "Une tour gigantesque en pierre.")
        >>> swamp.exits = {"N": tower}
        >>> swamp.get_exit("N").name
        'Tower'
        >>> swamp.get_exit("S") is None
        True
        >>> swamp.get_exit_string()
        'Sorties: N'

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory={}
        self.max_weight = 2.5
        self.quest_manager = QuestManager()
        self.rewards = []
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        direction = direction.upper()
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]

            # Set the current room to the next room.
            if next_room is not None:
                self.current_room = next_room
                #On n'ajoute dans l'historique que si la salle suivante est différente
                if not self.history or self.history[-1] != self.current_room:
                    self.history.append(next_room)

                return True
            # If the next room is None, print an error message and return False.
            print("\nAucune porte dans cette direction !\n")
            return False
    #Define the get_history method
    def get_history(self):
        """
        Retourne l'historique des pièces visitées par le joueur.

        Returns:
        str: Une chaîne représentant l'historique des pièces visitées.
        """
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        if self.history:
            history_str += "\n".join(f"     - {room.name}" for room in self.history[:-1])
        return history_str.strip()
    
    def get_inventory(self):
        """
        Affiche l'inventaire du joueur.

        Returns:
        None
        """
        if len(self.inventory) == 0:
            print("Votre inventaire est vide.")
        else:
            print("Vous disposez des items suivants :")
            for item in self.inventory.values():
                print(f"    - {item.name} : {item.description} ({item.weight} kg)")

    def current_weight(self):
        return sum(item.weight for item in self.inventory.values())
    
    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()
    