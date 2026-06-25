class Rectangle:
    """
    Représente un rectangle avec une largeur et une longueur.
    """

    def __init__(self, width, length):
        """
        Initialise un rectangle.

        width : largeur du rectangle
        length : longueur du rectangle
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calcule l'aire du rectangle.

        Retourne : width * length
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Retourne : 2 * (width + length)
        """
        return 2 * (self.width + self.length)

# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
