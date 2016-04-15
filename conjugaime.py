from collections import OrderedDict

#       ----- Exemplo
"""
palavra = input("Digite um verbo:\n")
a = prim_conj(palavra)
print(a.presente())
"""
class prim_conj:
    """
    Classe da primera cojugação, responsável pelos verbos terminados em ar
    """
    def __init__(self, verbo):
        if verbo[-2:] != "ar":
            print("Este verbo não pertence a primera conjugação")
        else:
            self.verbo = verbo

    def presente(self):
        """ Recebe um verbo regular e retorna um dicionário com o verbo conjugado"""

        conjugado = OrderedDict()
        irregulares = {}

        irregulares["dar"] = ["dou", "dás", "dá", "damos", "dais", " 	dão"]
        irregulares["estar"] = ["estou","estás","está","estamos","estais","estão"]
        irregulares["passear"] = ["passeio","passeias","passeia","passeamos", "passeais","passeiam"]
        irregulares["aboloar"] = ["abaúlo", "abaúlas", "abaúla", "abaulamos", "abaulais", "abaúlam"]
        irregulares["adequar"] = ["adéquo", "adéquas", "adéqua", "adequamos", "adequais", "adéquam"]

        pessoas = ["eu", "tu", "ela/ele", "nós", "vós", "elas/eles"]

        if self.verbo not in irregulares:

            sufixos = ["o", "as", "a", "amos", "ais", "am"]
            radical = self.verbo[:-2]

            for pessoa, sufixo in zip(pessoas, sufixos):
                conjugado[pessoa] = "{radical}{sufixo}".format(radical=radical,sufixo=sufixo)

        else:
            for pessoa, verbo in zip(pessoas, irregulares[self.verbo]):
                conjugado[pessoa] = verbo

        return conjugado
