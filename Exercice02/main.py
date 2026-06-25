students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

nom = input("Entrez le nom de l’étudiant : ")

if nom in students:
    print(f"Notes de {nom} :")

    notes = students[nom]

    for matiere, note in notes.items():
        print(f"{matiere} : {note}")

    moyenne = sum(notes.values()) / len(notes)
    print(f"Moyenne de {nom} : {moyenne}")

else:
    print(f"L'étudiant {nom} n'existe pas dans la liste.")
