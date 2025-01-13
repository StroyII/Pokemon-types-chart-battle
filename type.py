class Type():
    def __init__(self,nom:str,faiblesses:list):
        self.nom = nom
        self.faiblesses = []

        for faiblesse in faiblesses:
            self.faiblesses.append(faiblesse)

        