from collections import OrderedDict

#       ----- Exemplo
"""
palavra = input("Digite um verbo:\n")
a = prim_conj(palavra)
print(a.presente())
"""
class prim_conj:
    """
    Classe da primera cojugação, responsável pelos verbos terminados em ar do indicativo
    """
    def __init__(self, verbo):
        if verbo[-2:] != "ar":
            print("Este verbo não pertence a primera conjugação")
        else:
            self.verbo = verbo
            self.pessoas = ["eu", "tu", "ela/ele", "nós", "vós", "elas/eles"]

    def presente(self):
        irregulares = {}
        irregulares["dar"] = ["dou", "dás", "dá", "damos", "dais", " 	dão"]
        irregulares["estar"] = ["estou","estás","está","estamos","estais","estão"]
        irregulares["passear"] = ["passeio","passeias","passeia","passeamos", "passeais","passeiam"]
        irregulares["averiguar"] = ["averíguo","averíguas","averígua","averiguamos", "averiguais","averíguam"]


        sufixos = ["o", "as", "a", "amos", "ais", "am"]

        return self.resposta(irregulares,sufixos)

    def pret_per(self):
        irregulares = {}
        irregulares["dar"] = ["dei","deste","deu","demos","destes","deram"]
        irregulares["estar"] =  ["estive", "estiveste", "esteve", "estivemos", "estivestes", "estiveram",]
        irregulares["passear"] = ["passeei", "passeaste", "passeou", "passeamos", "passeastes", "passearam"]

        sufixos = [	"ei", "aste", "ou", "ámos", "astes", "aram"]

        return self.resposta(irregulares,sufixos)

    def resposta(self, irregulares, sufixos):
        conjugado = OrderedDict()
        if self.verbo not in irregulares:

            radical = self.verbo[:-2]

            for pessoa, sufixo in zip(self.pessoas, sufixos):
                conjugado[pessoa] = "{radical}{sufixo}".format(radical=radical,sufixo=sufixo)

        else:
            for pessoa, verbo in zip(self.pessoas, irregulares[self.verbo]):
                conjugado[pessoa] = verbo

        return conjugado
