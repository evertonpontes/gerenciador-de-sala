from os import path, makedirs, system
from time import sleep
from reservar_sala import Reserva
from cadastrar_salas import cadastro
import programacao
from calendario import Calendario
from gravacao import abrirRegistro
import config_pass

c = Calendario()
body = '\033[32m'
erro = '\033[31m'

def lerSalas():
    salas = []
    if not path.exists('data'):
        makedirs('data')
    try:
        arquivo_salas = open('data/salas.txt', 'r', encoding='utf-8')
        for linha in arquivo_salas:
            l=linha.strip().split('-')
            salas.append(l)
    except:
        open('data/salas.txt', 'x', encoding='utf-8')
    return salas

def menuPrincipalUser():
    while True:
        salas = lerSalas()
        registro = abrirRegistro()
        data_atual = [c.ano_atual,c.mes_atual,c.dia_atual]
        dia_atual = data_atual[2]
        print('+','-'*45,'+')
        print(f'''|{' '*45}  |
|\t\t MENU PRINCIPAL \t\t|
|{' '*45}  |''')
        print('+','-'*45,'+')
        sleep(1)
        reservasDia(registro,data_atual,dia_atual)
        print('+','-'*45,'+')
        print(f'''|{' '*45}  |
|\t[1] VISUALIZAR SALAS\t\t\t|
|\t[2] SAIR\t\t\t\t|
|{' '*45}  |''')
        print('+','-'*45,'+}')
        try:
            opcao = int(input('--> '))
            if opcao == 1:
                system('cls')
                visualizarSalas(salas)
            elif opcao == 2:
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

def menuPrincipalADM():
    while True:
        salas = lerSalas()
        registro = abrirRegistro()
        data_atual = [c.ano_atual,c.mes_atual,c.dia_atual]
        dia_atual = data_atual[2]
        print('+', '-' * 45, '+')
        print(f'''|{' ' * 45}  |
|\t\t MENU PRINCIPAL \t\t|
|{' ' * 45}  |''')
        print('+', '-' * 45, '+')
        sleep(1)
        reservasDia(registro,data_atual,dia_atual)
        print('+','-'*45,'+')
        print(f'''|{' ' * 45}  |
|\t[1] VISUALIZAR SALAS\t\t\t|
|\t[2] CADASTRAR SALA\t\t\t|
|\t[3] ALTERAR SENHA\t\t\t|
|\t[4] SAIR\t\t\t\t|
|{' ' * 45}  |''')
        print('+','-'*45,'+')
        try:
            opcao = int(input('--> '))
            if opcao == 1:
                system('cls')
                visualizarSalas(salas)
            elif opcao == 2:
                system('cls')
                cadastro()
            elif opcao == 3:
                system('cls')
                config_pass.mudarSenha()
            elif opcao == 4:
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

def reservasDia(registro,data: list,dia: int):
    reservas = []
    try:
        for linha in registro:
            l=linha.strip().split('; ')
            if int(l[1]) == data[0] and int(l[2]) == data[1]:
                if int(l[3]) == dia:
                    reservas.append(l)
    except:
        print(f'''
\tNÃO HÁ REGISTROS DISPONÍVEIS !
        ''')
    
    if len(reservas) > 0:
        print(f'''|{' '*45}  |
|\t\tRESERVAS DO DIA\t\t\t|
|{' '*45}  |''')
        print('+','-'*45,'+')
        sleep(1)
        for lista in reservas:
            print(f''' 
 Nome: {lista[6]} 
 Sala: {lista[0]}
 Horário: {lista[4]} - {lista[5]}
''')
            sleep(1)
    else:
        print(f'''
\t{erro}Não há nenhuma reserva para hoje{body}
            ''')

def visualizarSalas(salas: list):
    
    while True: # verificando se a opção escolhida é válida
        r = Reserva()
        print('+', '-' * 45, '+')
        print(f'|\t\t  SALAS\t\t\t\t|')
        print('+','-'*45,'+')
        print(f'| SELECIONE UMA OPÇÃO DE SALA PARA PROSSEGUIR\t|')
        print('+','-'*45,'+')
        # o for irá navegar pela lista de salas e exibir na tela a sala cadastrada e seu id correspondente.
    
        print(f' [0] VOLTAR\n')
        if len(salas) > 0:
            for i in salas:
                print(f' [{i[0]}] {i[1]}\n')
            try: # para verificar se o usuário não inseriu um caractere vazio ou q não seja numero
                opcao = int(input(f'--> '))
                if opcao == 0:
                    system('cls')
                    break

                elif opcao in range(1,len(salas)+1): # verificando se opção escolhida é igual a alguma id existentente
                    sala = salas[opcao-1][1] # inserindo a sala escolhida no atributo sala
                    print(f'''+{'-' * 46} +
| [1] RESERVAR SALA\t\t\t\t|
+{'-' * 46} +
| [2] VISUALIZAR PROGRAMAÇÃO SEMANAL\t\t|
+{'-' * 46} +
| [3] VOLTAR\t\t\t\t\t|
+{'-' * 46} +''')
                    try:
                        opcao2 = int(input('--> '))
                        if opcao2 == 1:
                            r.menu(sala)
                        elif opcao2 == 2:
                            programacao.fornecerData(sala)
                        elif opcao2 == 3:
                            system('cls')
                    except:
                        print(f'''
{erro}OPÇÃO INVÁLIDA{body}                     
                        ''')

                else:
                    print(f'''
{erro}OPÇÃO INVÁLIDA{body}                  
                        ''')

            except: # retorna uma mensagem de erro
                print(f'''
{erro}OPÇÃO INVÁLIDA{body}            
                        ''')

        elif len(salas) == 0:
            print(f'''
NÃO HÁ SALAS DISPONÍVEIS
            ''')
            opcao = int(input('--> '))
            if opcao == 0:
                break
            else:
                print(f'''
{erro}OPÇÃO INVÁLIDA{body}                 
                    ''')
                sleep(1)            