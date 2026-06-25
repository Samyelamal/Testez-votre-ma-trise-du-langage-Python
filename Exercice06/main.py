# Fonction calculate_average
def calculate_average(numbers):
    """
    Calcule la moyenne d'une liste de nombres.

    numbers : liste de nombres (int ou float)

    Retourne : la moyenne des nombres de la liste
    """
    return sum(numbers) / len(numbers)
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
