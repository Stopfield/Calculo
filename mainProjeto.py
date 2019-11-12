import math as mt

# Classe mãe da qual os dois projetos serão derivados
class Projeto:
    
    # Funções para a qual faremos os cálculos e acharemos as áreas
    def funcaoProjeto(self, x = 0):
        pass;

    # Função que calcula a área a partir do ponto esquerdo
    def ESQ(self, intervalo1, intervalo2, n = 0):
        base = (intervalo2 - intervalo1) / n;
        x = intervalo1;
        area = 0;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Função que calcula a área a partir do ponto direito
    def DIR(self, intervalo1, intervalo2, n = 0):
        base = (intervalo2 - intervalo1) / n;
        x = intervalo1;
        area = 0;


        # Como o cálculo da área deve começar pelo ponto à direita do retângulo, soma-se a base ao "x"
        x += base;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Função que calcula a área a partir de trapézios ao invés de retângulos
    def TRAP(self, intervalo1, intervalo2, n = 0):
        pass;

    