words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = "aeiouy"

resultat = [
    (mot, sum(1 for lettre in mot if lettre in voyelles))
    for mot in words
]

print(resultat)
