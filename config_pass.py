from genericpath import exists
import hashlib
import getpass
from time import sleep
from os import path, makedirs, system

body = '\033[32m'
erro = '\033[31m'
success = '\033[33m'

def buscarArquivo():
    if not path.exists('./data/'):
        makedirs('./data/')
    if not exists('./data/config'):
        arquivo = open('./data/config', 'w')
        senha = 'admin123'.encode()
        hash = hashlib.sha3_512(senha).hexdigest()
        arquivo.write(hash)
        arquivo.close()


def mudarSenha():
    print(f'''+{'-'*47}+
|\t\tINSIRA A SENHA ATUAL\t\t|
+{'-'*46}+''')
    senha_atual = getpass.getpass('--> ').encode() # getpass mascara a senha, na hora de digitar não é mostrado na tela
    hash = hashlib.sha3_512(senha_atual).hexdigest()
    buscarArquivo()
    arquivo = open('./data/config', 'r')
    hash_atual = arquivo.readline()
    arquivo.close()
    if hash == hash_atual:
        print(f'''+{'-'*47}+
|\t\tDIGITE A NOVA SENHA\t\t|
+{'-'*46}+''')
        nova_senha = getpass.getpass('--> ').encode()
        novo_hash = hashlib.sha3_512(nova_senha).hexdigest()
        arquivo = open('./data/config', 'w')
        arquivo.write(novo_hash)
        print(f'{success}senha alterada{body}')
        sleep(1)
        system('cls')
    else:
        print(f'{erro}senha incorreta{body}')
        sleep(1)
        system('cls')

def verificarSenha(senha: bytes):
    buscarArquivo()
    hash = hashlib.sha3_512(senha).hexdigest()
    arquivo = open('./data/config', 'r')
    hash_atual = arquivo.readline()
    arquivo.close()
    if hash == hash_atual:
        return True
    else:
        return False

