class Item:
    def __init__(self,name,description,weight):
        self.name= name
        self.description= description
        self.weight= weight
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight})"



fusil= Item('fusil','un fusil à pompe prêt à être dégainer à bout portant','3.5kg')
couteau=Item('couteau','un couteau tranchant pour un massacre amusant','70g')
clé_sortie=Item('clé de la sortie','les clés de la porte de sortie','1g')
lampe=Item('une lampe','pour tenter de térasser l obscurité','70g')
clé_voiture=Item('clé de la voiture','les clés de la voiture','1g')
