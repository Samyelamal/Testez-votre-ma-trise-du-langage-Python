## Écrivez votre code ici !
def square(x):
    """
    Calcule le carré d'un nombre.

    x : un nombre (int ou float)

    Retourne : le carré de x, ou None si x n'est pas un nombre
    """
    if not isinstance(x, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None

    return x * x
