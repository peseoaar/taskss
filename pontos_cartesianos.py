import os 

def limpar_terminal():
    if os.name == 'posix': 
        os.system('clear')
    elif os.name == 'nt': 
        os.system('cls')

def achar():
    limpar_terminal()
    print("\n   --------------------------------- \nEncontrar quadrante dos pontos cartesianos\n   --------------------------------- ")
    
    x = int(input("Digite o eixo X: "))
    y = int(input("Digite o eixo Y: "))

    if x==0 and y==0:
        print("\nQuadrantes 1, 2, 3 e 4")
    elif x==0 and y>0:
        print("\nQuadrantes 1 e 2")
    elif x==0 and y<0:
        print("\nQuadrantes 3 e 4")
    elif x<0 and y==0:
        print("\nQuadrantes 2 e 3")
    elif x>0 and y==0:
        print("\nQuadrantes 1 e 4")
    elif x<0 and y<0:
        print("\nQuadrante 3")
    elif x<0 and y>0:
        print("\nQuadrante 2")
    elif x>0 and y>0:
        print("\nQuadrante 1")
    elif x>0 and y<0:
        print("\nQuadrante 4")
achar()
def opcao():
    opcao = int(input("\n[1] encontrar outro [2] sair: "))
    match opcao: 
        case 1:
            achar()
        case 2:
            exit()
        case _:
            print("\nOpcao Invalida!\n")
            opcao()
opcao()
        


