import math as mt
from Projeto import Projeto

# Definição da função do projeto2
class Projeto2(Projeto):
    def funcaoProjeto(self, x = 0):
        return mt.e ** (x - 1);

# Definição da função do projeto5
class Projeto5(Projeto):
    def funcaoProjeto(self, x = 0):
        return (- (x ** 2)) + 4 * x;
