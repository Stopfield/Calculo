# Classe mãe da qual os dois projetos serão derivados
class Projeto:
    
    intervalo1 = 0;
    intervalo2 = 0;

    # É preciso ter intervalos para a função, caso contrario, ela não poderá ser calculada
    def __init__(self, intervalo1, intervalo2):
        self.intervalo1 = intervalo1;
        self.intervalo2 = intervalo2;
    
    # Caso o usuário queira alterar o valor dos intervalos
    def setIntervalos (self, intervalo1, intervalo2):
        self.intervalo1 = intervalo1;
        self.intervalo2 = intervalo2;
    
    def getIntervalos (self):
        print('De %d a %d' %(self.intervalo1, self.intervalo2));

    # Funções para a qual faremos os cálculos e acharemos as áreas
    def funcaoProjeto(self, x = 0):
        pass;

    # Calcula a área a partir do ponto esquerdo
    def ESQ(self, n = 0):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Calcula a área a partir do ponto direito
    def DIR(self, n = 0):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;

        # Como o cálculo da área deve começar pelo ponto à direita do retângulo, soma-se a base ao "x"
        x += base;

        for i in range(n):
            # area = y * x 
            area = self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Calcula a área a partir do ponto médio
    def MED(self, n = 0):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;
        pontoMedio = (x + base) / 2;

        for i in range(n):
            # Aqui pega-se o valor da função no ponto médio
            # area = y * x 
            area = self.funcaoProjeto(pontoMedio) * base;
            x += base;
        return area;
    
    # Calcula a área a partir de trapézios, ao invés de retângulos
    def TRAP(self, n = 0):
        
        # A área do método do trapézio tem uma formula bem simples, pode ser aplicada
        area = (self.ESQ(n) + self.DIR(n)) / 2

        return area;

    # Calcula a área a partir da fórmula de Simpson
    def SIMP(self, peso, n = 0):
        # Fórmula de simpson, sendo definido um peso para a função MED
        area = (peso * self.MED(n) + self.TRAP(n)) / (peso + 1);
        
        return area;