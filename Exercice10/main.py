## Écrivez votre code ici !
class Person:
    """
    Représente une personne avec un nom et un âge.
    """

    def __init__(self, name, age):
        """
        Initialise une personne.

        name : nom de la personne
        age : âge de la personne
        """
        self.name = name
        self.age = age

    def display_details(self):
        """
        Affiche les informations de la personne.
        """
        print("Nom :", self.name)
        print("Âge :", self.age)


class Employee(Person):
    """
    Représente un employé, qui est une personne avec un salaire.
    """

    def __init__(self, name, age, salary):
        """
        Initialise un employé.

        name : nom
        age : âge
        salary : salaire
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """
        Affiche les informations de l'employé.
        """
        super().display_details()
        print("Salaire :", self.salary)
