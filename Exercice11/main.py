## Écrivez votre code ici !
class BankAccount:
    """
    Représente un compte bancaire avec un titulaire et un solde.
    """

    def __init__(self, account_holder, balance=0.0):
        """
        Initialise un compte bancaire.

        account_holder : nom du titulaire
        balance : solde initial (par défaut 0.0)
        """
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        """
        Dépose de l'argent sur le compte.

        amount : montant à déposer (doit être positif)
        """
        if amount <= 0:
            print("Le montant doit être positif !")
            return

        self.balance += amount

    def withdraw(self, amount):
        """
        Retire de l'argent du compte.

        amount : montant à retirer (doit être positif et <= solde)
        """
        if amount <= 0:
            print("Le montant doit être positif !")
            return

        if amount > self.balance:
            print("Fonds insuffisants !")
            return

        self.balance -= amount

    def display_balance(self):
        """
        Affiche le titulaire du compte et le solde.
        """
        print("Titulaire :", self.account_holder)
        print("Solde :", self.balance)
