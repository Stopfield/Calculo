from scipy.integrate import quad

# Classe mãe da qual os dois projetos serão derivados
class Projeto:
    
    intervalo1 = 0;
    intervalo2 = 0;

    # Peso no método de Simpson
    simpWeight = 2;

    # É preciso ter intervalos para a função, caso contrario, ela não poderá ser calculada
    def __init__(self, intervalo1, intervalo2):
        self.intervalo1 = intervalo1;
        self.intervalo2 = intervalo2;
    
    # Caso o usuário queira alterar o valor dos intervalos
    def setIntervalos (self, intervalo1, intervalo2):
        self.intervalo1 = intervalo1;
        self.intervalo2 = intervalo2;
    
    # Define o peso no método de Simpson
    def setSimpWeight(self, weight):
        self.simpWeight = weight;

    # Retorna o peso utilizado na função de Simpson
    def getSimpWeight(self):
        return self.simpWeight;

    # Retorna os intervalos
    def getIntervalos (self):
        intervals = [self.intervalo1, self.intervalo2];
        return intervals;

    # Funções para a qual faremos os cálculos e acharemos as áreas
    def funcaoProjeto(self, x):
        return x;

    # Calcula a área a partir do ponto esquerdo
    def ESQ(self, n):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;

        for i in range(n):
            # area = y * x 
            area += self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Calcula a área a partir do ponto direito
    def DIR(self, n):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;

        # Como o cálculo da área deve começar pelo ponto à direita do retângulo, soma-se a base ao "x"
        x += base;

        for i in range(n):
            # area = y * x 
            area += self.funcaoProjeto(x) * base;
            x += base;
        return area;
    
    # Calcula a área a partir do ponto médio
    def MED(self, n):
        base = (self.intervalo2 - self.intervalo1) / n;
        x = self.intervalo1;
        area = 0;

        pontoMedio = (x + base) / 2;

        for i in range(n):
            # Aqui pega-se o valor da função no ponto médio
            # area = y * x 
            area += self.funcaoProjeto(pontoMedio) * base;
            pontoMedio += base;

        return area;
    
    # Calcula a área a partir de trapézios, ao invés de retângulos
    def TRAP(self, n):
        
        # A área do método do trapézio tem uma formula bem simples, pode ser aplicada
        area = (self.ESQ(n) + self.DIR(n)) / 2

        return area;

    # Calcula a área a partir da fórmula de Simpson
    def SIMP(self, n):
        # Fórmula de simpson, sendo definido um peso para a função MED
        area = (self.simpWeight * self.MED(n) + self.TRAP(n)) / (self.simpWeight + 1);
        
        return area;
    
    # Retorna o erro de determinado método de integração
    def calculateError(self, integrationMethod, numberOfRectangles = []): 

        # ERRO = VALOR EXATO - VALOR APROXIMADO
        # -> Logo, seria o valor da integral com o valor retornado pelos métodos da classe "Projeto"

        listError = [];

        # Para ESQ
        if (integrationMethod == 0):
            for n in numberOfRectangles:
                integral = quad(self.funcaoProjeto, self.intervalo1, self.intervalo2)[0]
                error = integral - self.ESQ(n);
                listError.append(error);

        # Para DIR
        elif (integrationMethod == 1):
            for n in numberOfRectangles:
                integral = quad(self.funcaoProjeto, self.intervalo1, self.intervalo2)[0]
                error = integral - self.DIR(n);
                listError.append(error);

        # Para MED
        elif (integrationMethod == 2):
            for n in numberOfRectangles:
                integral = quad(self.funcaoProjeto, self.intervalo1, self.intervalo2)[0]
                error = integral - self.MED(n);
                listError.append(error);
            
        # Para TRAP
        elif (integrationMethod == 3):
            for n in numberOfRectangles:
                integral = quad(self.funcaoProjeto, self.intervalo1, self.intervalo2)[0]
                error = integral - self.TRAP(n);
                listError.append(error);

        # Para SIMP
        elif (integrationMethod == 4):
            for n in numberOfRectangles:
                integral = quad(self.funcaoProjeto, self.intervalo1, self.intervalo2)[0]
                error = integral - self.SIMP(n);
                listError.append(error);

        return listError;