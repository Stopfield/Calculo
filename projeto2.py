import numpy as np;
import math as mt;





def funcaoProjeto5(self, x = 0):
    return -(x ** 2) + 4;   # Do intervalo de 0 a 2

class Projeto2:
    # Funções para a qual faremos os cálculos e acharemos as áreas
    def funcaoProjeto2(self, x = 0):
        return mt.e ** (x - 1); # Do intervalo de 0 a 2

    # Função que calcula a área a partir do ponto esquerdo
    def ESQ(self, intervalo1, intervalo2, n = 0):
        base = (intervalo2 - intervalo1) / n;
        x = intervalo1;
        area = 0;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto2(x) * base;
            x += base;
        return area;
    
    def DIR(self, intervalo1, intervalo2, n = 0):
        base = (intervalo2 - intervalo1) / n;
        x = intervalo1;
        area = 0;


        # Como o cálculo da área deve começar pelo ponto à direita do retângulo, soma-se a base ao "x"
        x += base;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto2(x) * base;
            x += base;
        return area;
    