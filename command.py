"""
Ce module définit la classe Command, qui représente une commande dans le jeu,
et les méthodes associées à l'exécution des commandes par l'utilisateur.
"""
class Command:
    """
    This class represents a command. A command is composed of a command word,
     a help string, an action and a number of parameters.

    Attributes:
        command_word (str): The command word.
        help_string (str): The help string.
        action (function): The action to execute when the command is called.
        number_of_parameters (int): The number of parameters expected by the command.
        alias (list[str]): A list of alternative words for the command.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters, alias)
         : The constructor.
        __str__(self) : The string representation of the command.
        matches(self, input_word): Checks if the input matches the command word or its alias.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1
    """
    def __init__(self, command_details):
        self.command_word = command_details.get("command_word")
        self.help_string = command_details.get("help_string")
        self.action = command_details.get("action")
        self.number_of_parameters = command_details.get("number_of_parameters")
        self.alias = command_details.get("alias", None)
    def matches(self, input_word):
        """
        Vérifie si le mot saisi correspond au mot de commande ou à l'un de ses alias.

        Args:
            input_word (str): Le mot saisi par l'utilisateur.

        Returns:
            bool: Retourne True si le mot saisi correspond au mot de
            commande ou à l'un de ses alias, sinon False.
        """
        if self.alias is None:
            return input_word.lower() == self.command_word.lower()
        return input_word.lower() == (self.command_word.lower() or
                                      input_word.lower()
                                      in map(str.lower, self.alias))
    def __str__(self):
        return  self.command_word \
                + self.help_string
