# Função em que a gente resolve os problemas
from calculus import * # Importa as funções e métodos do "calculos.py"

while True:
    choice = int(input('Escolha a questão a ser resolvida: '));

    # Sair do programa
    if (choice <= 0):
        break;
    # Projeto 1
    elif (choice == 1):
        pass; # projeto1();
    # Projeto 2
    elif (choice == 2):
        pass; # projeto2();
    else:
        print('Opção inválida!\n');