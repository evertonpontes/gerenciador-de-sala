from os import system, path, makedirs
from time import sleep

body = '\033[32m'
erro = '\033[31m'
success = '\033[33m'


def cadastro():
    system('cls')
    print('+','-'*45,'+')
    print(f'''|{' '*47}|
|\tCADASTRAR SALAS\t\t\t\t|
|{' '*47}|''')
    print('+','-'*45,'+')
    sala = input('DIGITE O NOME DA SALA: ').lower()
    sala = sala.replace(' ', '_')
    if len(sala) >= 4 :
        if not path.exists('./data/'): # verificando se a pasta data não existe
                makedirs('./data/') # criando pasta data
        try:
            arquivo_sala = open('./data/salas.txt', 'r', encoding='utf-8')
            count = 1
            for _ in arquivo_sala:
                count += 1
            arquivo_sala = open('./data/salas.txt', 'a', encoding='utf-8')
            arquivo_sala.write(f'{count}-{sala}\n')
            print(f'''
{success}CADASTRO CONCLUÍDO{body}
            ''')
        except:
            arquivo_sala = open('./data/salas.txt', 'a', encoding='utf-8')
            arquivo_sala.write(f'1-{sala}\n')
            print(f'''
{success}CADASTRO CONCLUÍDO{body}
            ''')
    else:
        print(f'''
{erro}Nome de sala inválido, tente um nome 
com no mínimo 4 caracterers.{body}
        ''')
        sleep(1)
        cadastro()