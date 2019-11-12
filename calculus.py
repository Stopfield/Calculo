# Função que a gente faz as resoluções dos projetos
import numpy as np;
import math as mt;




# Funções para a qual faremos os cálculos e acharemos as áreas
def funcaoProjeto2(x = 0):
    return mt.e ** (x - 1); # Do intervalo de 0 a 2

def funcaoProjeto5(x = 0):
    return -(x ** 2) + 4;   # Do intervalo de 0 a 2

# Função que calcula a área a partir do ponto esquerdo
def ESQ(intervalo1, intervalo2, n = 0):
    base = (intervalo2 - intervalo1) / n;
    x = intervalo1;
    area = 0;

    for i in range(n):
        # area = y * x 
        area = funcaoProjeto2(x) * base;
        x += base;
    return area;
