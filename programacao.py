from os import system
import calendar
from datetime import datetime, timedelta
from time import sleep
from calendario import Calendario
from gravacao import abrirRegistro
c = Calendario()

body = '\033[32m'
erro = '\033[31m'
success = '\033[33m'

def fornecerData(sala: str):
    system('cls')
    print('+','-'*45,'+')
    print(f'''
Informe a data para visualizar a programação 
semanal da sala: {sala}    
    ''')
    print('+','-'*45,'+')
    while True:
        try:
            ano = int(input('''
Ano
---> '''))
            print('+','-'*45,'+')
            mes = int(input('''
Mês
---> '''))
            print('+','-'*45,'+')
            dia = int(input('''
Dia
---> '''))
            print('+','-'*45,'+')

            if ano >= 2022 and mes > 0 and dia > 0:
                if c.validarData(ano,mes,dia):
                    data = [ano,mes,dia]
                    break
                else:
                    print(f'''
{erro}Data inválida{body}
                ''')

            else:
                print(f'''
{erro}Data inválida
                ''')
        except:
            print(f'''
{erro}Insira um valor válido!{body}
            ''')
    dias = organizaDiasSemana(data)
    arquivo = abrirRegistro()
    system('cls')
    recuperarProgramacaoSemana(arquivo,sala,data,dias)

def recuperarProgramacaoSemana(arquivo,sala: str,data: list,dias: list): # retorna todas as reservas de uma semana
# parametro arquivo é o arquivo txt, sala é a sala escolhida para visualizar sua programação semanal, data para
# comparar com as datas em arquivo dias são todos os dias da semana
        reservas = []
        for linha in arquivo:
            l=linha.strip().split('; ')
            if sala == l[0]:
                if int(l[1]) == data[0] and int(l[2]) == data[1]:
                    if int(l[3]) in dias:
                        reservas.append(l)
        if len(reservas) > 0:
            for lista in reservas:
                print(f'''
{mostrarSemana(int(lista[3]),dias)}
Nome: {lista[6]}
Sala: {lista[0]}
Data: {lista[3]}/{lista[2]}/{lista[1]}
Horário: {lista[4]} - {lista[5]}
            ''')
                print('+','-'*45,'+')
                sleep(1)
            voltar = input('''
DIGITE QUALQUER TECLA PARA VOLTAR --> ''')
            sleep(1)
            system('cls')                
        else:
            print(f'''
Não há nenhuma programação para {success}{sala}{body} nesta semana.
            ''')
            sleep(1)
            voltar = input('''
DIGITE QUALQUER TECLA PARA VOLTAR --> ''')
            sleep(1)
            system('cls')

def organizaDiasSemana(lista: list): # retorna uma lista de dias correspondentes a um dia da semana de segunda a domingo
        semana = []
        data = f'{lista[0]}-{lista[1]}-{lista[2]}'
        dia_da_semana = calendar.weekday(int(lista[0]), int(lista[1]), int(lista[2]))
        data_convertida = datetime.strptime(data, '%Y-%m-%d').date()

        if dia_da_semana == 0:
            for valor in range(7):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 1:
            for valor in range(-1, 6):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 2:
            for valor in range(-2, 5):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 3:
            for valor in range(-3, 4):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 4:
            for valor in range(-4, 3):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 5:
            for valor in range(-5, 2):
                semana.append((data_convertida + timedelta(days=valor)).day)

        elif dia_da_semana == 6:
            for valor in range(-6, 1):
                semana.append((data_convertida + timedelta(days=valor)).day)

        return semana

def mostrarSemana(diaR: int,dias: list): # retorna uma agenda com os dias da semana, se tiver alguma reserva em algum dia esses dias ganham um realce
        dias_serie = ''
        for dia in dias:
            if diaR == dia:
                if dia < 10:
                    dias_serie += f'{success}0' + str(dia) + body +' '
                else:
                    dias_serie += success + str(dia) + body +' '
            else: 
                if dia < 10:
                    dias_serie += '0' + str(dia) + ' '
                else:
                    dias_serie += str(dia) + ' '

        return f'''Se Te Qa Qi Sx Sa Do
{dias_serie} 
+{'-'*46}+'''