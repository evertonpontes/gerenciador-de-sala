import calendar
from datetime import datetime, timedelta

class Calendario:

    ano_atual = datetime.today().year
    mes_atual = datetime.today().month
    dia_atual = datetime.today().day
    meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO',
             'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    def exibirDiaSemana(self,ano: int,mes: int,dia: int): # retorna o nome do dia da semana
        dia_da_semana = calendar.weekday(ano,mes,dia)
        if dia_da_semana == 0:
            return self.dias_semana[0]
        elif dia_da_semana == 1:
            return self.dias_semana[1]
        elif dia_da_semana == 2:
            return self.dias_semana[2]
        elif dia_da_semana == 3:
            return self.dias_semana[3]
        elif dia_da_semana == 4:
            return self.dias_semana[4]
        elif dia_da_semana == 5:
            return self.dias_semana[5]
        elif dia_da_semana == 6:
            return self.dias_semana[6]

    def mostrarMes(self,numero: int): # retorna o mes pelo numero
        return self.meses[numero-1] # recebe o parâmentro numero(inteiro), que equivale ao número do mes

    def anoBissesto(self,ano: int): # verifica ano bisexto
        if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
            return True
        else:
            return False

    def validarData(self,ano: int,mes: int,dia: int): # verifica a validacao de data
        if mes in range(1,13): # verifica se o numero do mes e valido
            if mes == 2: # verifica se e fevereiro
                if self.anoBissesto(ano): # se for ano bisexto
                    if dia in range(1,30): # verifica se fevereiro tem 29 dias
                        return True
                else:
                    if dia in range(1,29): # se nao for bisexto verifica se fev tem 28 dias
                        return True

            elif mes <= 7: # de janeiro a julho
                if mes % 2 == 0 and dia in range(1,31): # verifica se os meses de numero par tem 30 dias exceto fev
                    return True
                elif mes % 2 == 1 and dia in range(1,32): # verifica se meses impares tem 31 dias
                    return True
            
            elif mes > 7: # de agosto a dezembro a situacao inverte
                if mes % 2 == 0 and dia in range(1,32): # meses pares tem 31 dias
                    return True
                elif mes % 2 == 1 and dia in range(1,31): # meses impares tem 30 dias
                    return True
        else:
            return False
