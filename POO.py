class CompteBancaire:
    def __init__(self, titulaire, sommeInitiale):
        self.titulaire = titulaire
        self.solde = sommeInitiale

    def crediter(self, montant):
        self.solde += montant

    def debiter(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            return True

    def __repr__(self):
        return "Le compte de MM,M " +str(self.titulaire)+ " est de " +str(self.solde) + " €"

def afficher_tous_les_comptes(comptes):
    for compte in comptes:
        print(compte)

comptes = []
comptes.append(CompteBancaire("Stark", 1000))
comptes.append(CompteBancaire("Banner", 500))
comptes.append(CompteBancaire("Parker", 700))
comptes.append(CompteBancaire("Rogers", 600))
comptes.append(CompteBancaire("Wayne", 1500))
comptes.append(CompteBancaire("Prince", 2500))

afficher_tous_les_comptes(comptes)
