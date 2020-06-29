from unittest import TestCase
from conjugaime.conjugaime import Indicativo


class IndicativoArPresente(TestCase):
    def teste_andar_deve_retornar_ando_na_primeira_pessoa(self):
        result = Indicativo('andar').presente()['eu']
        self.assertEqual('ando', result)


class IndicativoIrPresente(TestCase):
    def teste_cair_deve_retornar_caio_na_primeira_pessoa(self):
        result = Indicativo('cair').presente()['eu']
        self.assertEqual('caio', result)


class IndicativoErPresente(TestCase):
    def teste_chover_deve_retornar_chovo_na_primeira_pessoa(self):
        result = Indicativo('chover').presente()['eu']
        self.assertEqual('chovo', result)
