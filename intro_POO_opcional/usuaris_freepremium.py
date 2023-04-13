class Usuaris:

    tipus_usuari = "Free"
    publicitat = True
    def __init__(self, nid, alias, nom, cognom):
        self.nid = nid
        self.alias = alias
        self.nom = nom
        self.cognom = cognom

    def mostra_dades(self):
        print("El nom i cognoms de l'usuari són:" ,self.nom, self.cognom)
        print("L'ID de l'usuari és: ", self.nid , ".")
        print("L'alias de l'usuari és: " , self.alias , ".")


class UsuarisPremium:

    tipus_usuari = "Premium"
    publicitat = False

    def __init__(self, nid, alias, nom, cognom):
        self.nid = nid
        self.alias = alias
        self.nom = nom
        self.cognoms = cognoms

    def mostra_dades(self):
        print("El nom i cognoms de l'usuari són:" ,self.nom, self.cognom)
        print("L'ID de l'usuari és: ", self.nid , ".")
        print("L'alias de l'usuari és: " , self.alias , ".")


usuari1 = Usuaris("001", "raulito43", "Raúl", "Fernández Gomila")
usuari1.mostra_dades()
print(usuari1.tipus_usuari)