def square(x):
    """
    Calcule le carré d'un nombre.

    x : un nombre (int ou float)

    Retourne : le carré de x, ou None si x n'est pas un nombre
    """
    try:
        return x * x
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None
    
print(square(x))
