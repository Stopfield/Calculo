# Aqui a gente inicia o programa resolve os problemas
from calculus import *

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
        print('Opção inválida!');