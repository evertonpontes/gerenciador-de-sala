from time import sleep
from os import path, makedirs, system

body = '\033[32m'
erro = '\033[31m'
success = '\033[33m'

def abrirRegistro():
    if not path.exists('./data/'):
        makedirs('./data/')
    try:
        # se o arquivo existir abra o arquivo como leitura
        arquivo = open('./data/registro.txt', 'r')
        return arquivo
    except:
        # se o arquivo não existir, cria e depois abre como leitura
        cria_arquivo = open('./data/registro.txt', 'x')
        cria_arquivo.close()
        abrirRegistro()

def salvarRegistro(reg):

    arquivo = open('./data/registro.txt', 'a', encoding='utf-8') # abrindo o arquivo no modo de append(adiciona dados)
    # e se o arquivo nao existir ele cria
    linha = '' # definindo a linha que sera salva no arquivo
    for dado in reg: # FOR vai percorrer sobre cada dado do registro
        if dado == reg[-1]: # se o dado for o ultimo da lista, adicione um newLine, para que as outras reservas que forem
            # salvas no arquiva sejam escritas uma em baixo da outra
            linha += str(dado) + '\n'
        else: # se nao apenas ira dividir os dados por '; '
            linha += str(dado) + '; '
    arquivo.write(linha) # escrevendo a linha no arquivo
    arquivo.close() # fechando
    print(f'''
\t\t{success}REGISTRO SALVO !{body}
                ''') # exibindo uma mensagem para que o usuario saiba que o cadastro foi concluido

def verificarReserva(reg): # verifica se a reserva feita pelo usuario pode ser salva no arquivo txt

    try: # TRY irá abrir o arquivo no modo de leitura (sem edicao) e fara toda a verificacao

        arquivo = open('./data/registro.txt', 'r')
        buscador = 0 # criei uma variavel buscador para verificar se a sala escolhida pelo usuario esta disponivel ou nao
        for linha in arquivo: # FOR ira iterar sobre cada linha do arquivo
            l=linha.strip('\n').split('; ') # strip remove algum caractere (definido no parametro. se nao definir, por padrao,
            # ele remove os espacos, nesse caso ele vai remover o '\n' novaLinha) no inicio e final da frase/linha e o 
            # split vai gerar uma lista dividindo em '; '
            if reg[0] == l[0]: # Comparando a sala do registro com as salas de alguma linha de registro salva
                if reg[1] == l[1] and reg[2] == l[2] and reg[3] == l[3]: # comparando as datas ano/mes/dia
                    if reg[4] == l[4]: # comparando o horario inicial da reserva
                        buscador += 1 # se já tiver uma reserva na mesma sala para mesma data e horario, entao buscador = 1
                        usuario = l[6] # definindo as variáveis para chama-las quando for printar a frase 
                        sala = l[0]
                        data = f'{l[3]}/{l[2]}/{l[1]}'
                        hi = l[4].split(':')
                        hf = l[5].split(':')
                        horario = f'{hi[0]}h as {hf[0]}h'
        
        if buscador:
            print(f'''
    {erro}Não foi possível cadastrar a reserva no sistema. O usuário {success}{usuario}{erro} já reservou a sala {success}{sala}{erro}
para a data {success}{data}{erro}, no horário das {success}{horario}{body} 
                ''')
            voltar = input('''
DIGITE QUALQUER TECLA PARA VOLTAR --> ''')
            sleep(1)
            system('cls')
        else:
            salvarRegistro(reg) # se a sala estiver disponivel para reserva, o programa vai chamar a funcao para salvar o registro
    except:
        salvarRegistro(reg)


    # como o arquivo esta sendo aber em modo de leitura, na primeira vez que executar o comando, se ele nao
    # achar o arquivo ele pode retornar um erro, para isso não acontecer eu usei TRY e EXCEPT, pois se o TRY
    # não encontrar o arquivo/ele ainda nao foi criado, o except vai chamar a funcao de salvar registro
    # que automaticamente cria o arquivo se nao existir.