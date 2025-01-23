class Type():
    def __init__(self,nom:str,faiblesses:list):
        self.nom = nom
        self.faiblesses = faiblesses

    def is_faiblesse(self,type_combattu:type)->bool:
        """
        Return if True/False the type this one fighted is in the weaknesses

        """
        if (type_combattu in self.faiblesses):
            res = True
        else:
            res = False
        
        return res