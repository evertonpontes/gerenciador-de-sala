# PROJETO DE PROGRAMAÇÃO I
#
# EQUIPE:
# EVERTON PONTES PEREIRA
# JAILTON SANTOS DE OLIVEIRA
# TALIANE VIEIRA DA SILVA

import getpass
from os import system
from menu import menuPrincipalUser, menuPrincipalADM
import config_pass

body = '\033[32m'
erro = '\033[31m'

def telaInicial():
    while True:
        print(f'\t\t{body}GERENCIADOR DE SALAS')
        print('+', '-' * 45, '+')
        print(f'''|{' ' * 45}  |
|\t\tSEJA BEM VINDO(A)\t\t|
|{' ' * 45}  |''')
        print('+', '-' * 45, '+')
        print(f'''|{' '*45}  |
|\tENTRAR COMO\t\t\t\t|
| [1] USUÁRIO (PADRÃO)\t\t\t\t|
| [2] ADMINISTRADOR\t\t\t\t|
| [3] SAIR\t\t\t\t\t|
|{' '*45}  |''')
        print('+', '-' * 45, '+','')

        try:
            opcao = int(input('--> '))
            if opcao == 1:
                system('cls')
                menuPrincipalUser()
            elif opcao == 2:
                print('''
INSIRA A SENHA PARA ENTRAR
                ''')
                senha = getpass.getpass('--> ').encode()
                if config_pass.verificarSenha(senha):
                    system('cls')
                    menuPrincipalADM()
                else:
                    print(f'''
{erro}SENHA INCORRETA{body}
                    ''')
            elif opcao == 3:
                system('cls')
                break
            else:
                print(f'''
{erro}OPÇÃO INVÁLIDA{body}
            ''')
        except:
            print(f'''
{erro}OPÇÃO INVÁLIDA{body}
            ''')

telaInicial()