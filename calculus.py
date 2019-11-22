# Aqui é onde os projetos serão resolvidos
from projectDefinition import Projeto2, Projeto5
from scipy.integrate import quad;

# Número de retângulos usados para o cálculo do erro
numRetangulos = [2, 10, 100, 1000];

# Dicitionary para melhorar a leitura do código
errors = {
    "ESQ"  : 0,
    "DIR"  : 1,
    "MED"  : 2,
    "TRAP" : 3,
    "SIMP" : 4
}

# Cria a tabela de erros
def createTableOfContent(listaDeErros, rectangles, method):
    print('\n\n n     | %s' %(method));
    for i in range(len(rectangles)):
        print(' %d  ->  %.50f  ' %(rectangles[i], listaDeErros[i]));
    print('\n\n'); 

##############
# Projeto 2
##############

# Calcular erros no projeto 2
def solucionaProjeto2():
    
    # Inicializa o objeto
    projeto2 = Projeto2(0, 2);

    choice = 1;

    while (choice > 0):
        print('\n\n => Projeto 2 ');
        print(' > Digite um número menor ou igual a 0 para sair');
        print(' ( 1 ) ESQ');
        print(' ( 2 ) DIR');
        print(' ( 3 ) MED');
        print(' ( 4 ) TRAP');
        print(' ( 5 ) SIMP');

        choice = int(input('Qual o método de integração? \n >  '))

        if (choice == 1):
            listaErros = projeto2.calculateError(errors["ESQ"], numRetangulos);
        elif (choice == 2):
            listaErros = projeto2.calculateError(errors["DIR"], numRetangulos);
        elif (choice == 3):
            listaErros = projeto2.calculateError(errors["MED"], numRetangulos);
        elif (choice == 4):
            listaErros = projeto2.calculateError(errors["TRAP"], numRetangulos);
        elif (choice == 5):
            listaErros = projeto2.calculateError(errors["SIMP"], numRetangulos);
        else:
            break;
        
        createTableOfContent(listaErros, numRetangulos, list( errors.keys() )[choice - 1]);


##############
# Projeto 5
##############

def solucionaProjeto5():

    # Inicializa o objeto
    projeto5 = Projeto5(0, 2);

    choice = 1;

    while (choice > 0):

        print(' \n\n=> Projeto 2 ');
        print(' > Digite um número menor ou igual a 0 para sair');
        print(' ( 1 ) ESQ');
        print(' ( 2 ) DIR');
        print(' ( 3 ) MED');
        print(' ( 4 ) TRAP');
        print(' ( 5 ) SIMP');

        choice = int(input('Qual o método de integração? \n >  '))

        if (choice == 1):
            listaErros = projeto5.calculateError(errors["ESQ"], numRetangulos);
        elif (choice == 2):
            listaErros = projeto5.calculateError(errors["DIR"], numRetangulos);
        elif (choice == 3):
            listaErros = projeto5.calculateError(errors["MED"], numRetangulos);
        elif (choice == 4):
            listaErros = projeto5.calculateError(errors["TRAP"], numRetangulos);
        elif (choice == 5):
            listaErros = projeto5.calculateError(errors["SIMP"], numRetangulos);
        else:
            break;
    
        createTableOfContent(listaErros, numRetangulos, list(errors.keys())[choice - 1]);
