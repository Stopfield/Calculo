import math as mt
from mainProjeto import Projeto

# Definição da função do projeto2
class Projeto2(Projeto):
    def funcaoProjeto(self, x = 0):
        return mt.e ** (x - 1);

# Definição da função do Projeto5
class Projeto5(Projeto):
    def funcaoProjeto(self, x = 0):
        return (- (x ** 2)) + 4 * x;
