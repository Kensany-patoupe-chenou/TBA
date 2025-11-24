"""Module contenant la classe Item pour représenter les objets du jeu."""
class Item:
    """
    Représente un objet dans le jeu.

    La classe Item est utilisée pour définir un objet que le joueur peut utiliser ou transporter. 
    Chaque objet a un nom, une description et un poids associé.

    Attributs :
        name (str): Le nom de l'objet.
        description (str): Une description détaillée de l'objet.
        weight (str): Le poids de l'objet, exprimé sous forme de chaîne de caractères.
    """
    def __init__(self,name,description,weight):
        """
        Initialise un nouvel objet Item.

        Args:
            name (str): Le nom de l'objet.
            description (str): La description de l'objet.
            weight (str): Le poids de l'objet.
        """
        self.name= name
        self.description= description
        self.weight= weight
    def __str__(self):
        """
        Retourne une chaîne de caractères représentant l'objet.

        Returns:
            str: Une représentation de l'objet au format "(nom, description, poids)".
        """
        return f"({self.name},{self.description},{self.weight})"

