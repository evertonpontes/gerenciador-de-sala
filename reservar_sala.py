from os import system
from time import sleep
from calendario import Calendario
from gravacao import verificarReserva

c = Calendario()
body = '\033[32m'
erro = '\033[31m'
success = '\033[33m'

class Reserva:

    def salaReservar(self, sala: str): # definir a sala da reserva
        self.sala = sala # a sala é definida no menu do usuario
    
    def dataReservar(self):
        self.data = [] # definir a data da reserva, o usuario irá escolher o dia da reserva, o mes por padrã é o mes 
        # atual, mas se o dia for menor que o dia atual, será definido o mes seguinte, já o ano também é o ano atual,
        # mas vai depender do mes.
        ano = c.ano_atual # definindo o ano 
        mes = c.mes_atual # definindo o mes
        print('+', '-' * 45, '+')
        print(f'\t\tSALA: {self.sala}')
        print('+', '-' * 45, '+')
        print(f'|\t\t\tDATA\t\t\t|')
        print(f'''|{' '*46} |
|\t{c.dia_atual} de {c.mostrarMes(mes)} de {ano}, {c.exibirDiaSemana(ano,mes,c.dia_atual)}\t\t|
|{' '*46} |''') # exibindo a data atual e o dia da semana
        print('+', '-' * 45, '+')
        
        while True: # loop
            try: # verificando se o usuario inseriu um número
                print('ESCOLHA O DIA DA RESERVA')
                dia = int(input('--> ')) # tenta converter para inteiro
                if dia > 0: # verifica se dia é maior que 0
                    if dia < c.dia_atual and mes == 12: # verificando se dia é menor que dia atual e se mes é dezembro
                        if c.validarData((ano+1),1,dia): # validando a data, verificando se dia está dentro do limite de dias do mes 
                            # e ano correspondente
                            print('+', '-' * 45, '+')
                            print(f'''|{' '*46} |
|\t{dia} de {c.mostrarMes(1)} de {ano+1}, {c.exibirDiaSemana((ano+1),1,dia)}\t\t|
|{' '*46} |''') # exibindo data atualizada
                            print('+', '-' * 45, '+')
                            if c.exibirDiaSemana((ano+1),1,dia) == c.dias_semana[5] or c.exibirDiaSemana((ano+1),1,dia) == c.dias_semana[6]: # verificando se o dia escolhido é num final de semana
                                print(f'''
 {erro}Não pode definir dia da reserva no {c.exibirDiaSemana((ano+1),1,dia)}{body}
                                ''') # exibi mensagem mensagem que não pode definir nessa data     
                            else: # se não, altera o valor de ano e mes, reserva é definida pra janeiro do prox ano e quebra o loop
                                ano += 1
                                mes = 1
                                break
                        else: # se validação retornar False, exibe mensagem avisando para usuário
                            print(f'''
 {erro}A data está incorreta!{body}
            ''')
                    elif dia < c.dia_atual and mes < 12: # verifica se dia é menor que dia atual e mes vem antes de dezembro
                        if c.validarData(ano,(mes+1),dia): # verifica se data é válida
                            print('+', '-' * 45, '+')
                            print(f'''|{' '*46} |
|\t{dia} de {c.mostrarMes(mes+1)} de {ano}, {c.exibirDiaSemana(ano,(mes+1),dia)}\t\t|
|{' '*46} |''') # exibi data atualizada
                            print('+', '-' * 45, '+')
                            if c.exibirDiaSemana(ano,(mes+1),dia) == c.dias_semana[5] or c.exibirDiaSemana(ano,(mes+1),dia) == c.dias_semana[6]:
                                print(f'''
 {erro}Não pode definir dia da reserva no {c.exibirDiaSemana(ano,(mes+1),dia)}{body}
                                ''') # verfica se o dia é num final de semana
                            else: # se não, reserva é definida para o mes seguinte e quebra o loop
                                mes += 1
                                break
                        else: # se a validação da data retorna False
                            print(f'''
 {erro}A data está incorreta{body}
            ''')

                    elif dia > c.dia_atual: # verifica se dia é maior que dia atual
                        if c.validarData(ano,mes,dia): # verifica se data é valida
                            print('+', '-' * 45, '+')
                            print(f'''|{' '*46} |
|\t{dia} de {c.mostrarMes(mes)} de {ano}, {c.exibirDiaSemana(ano,mes,dia)}\t\t|
|{' '*46} |''') # exibi data atualizada
                            print('+', '-' * 45, '+')
                            if c.exibirDiaSemana(ano,mes,dia) == c.dias_semana[5] or c.exibirDiaSemana(ano,mes,dia) == c.dias_semana[6]:
                                print(f'''
 {erro}Não pode definir dia da reserva no {c.exibirDiaSemana(ano,mes,dia)}{body}
                                ''') # verifica se dia é em um final de semana
                            else: # se não, apenas quebra o loop, e mes e ano se mantém o mesmo 
                                break
                        else: # se validação da data retornar False
                            print(f'''
 {erro}A data está incorreta{body}
            ''')
                    elif dia == c.dia_atual: # verifica se dia definido pelo usuario é igual a o dia atual e impede de reservar
                        print(f'''
 {erro}Não pode reservar a sala para hoje.{body}
                        ''')
                else:
                    print(f'''
 {erro}Insira um valor válido para dia.{body}
            ''')
            except: # se dia não for um número, exibi uma mensagem para o usuário
                print(f'''
 {erro}Insira um valor válido para dia.{body}
            ''')
        print(f'''
 Deseja definir esta data? s/n
        ''') # pergunta se deseja salvar a data

        while True:
            opcao = input('--> ')
            if opcao.lower() == 's': # se o usuario digitou 's' a data é sala no atributo self.data
                self.data.append(str(ano))
                self.data.append(str(mes))
                self.data.append(str(dia))
                print(f'''
 {success}Data definida!{body}
                ''')
                break
            elif opcao.lower() == 'n': # se digitou 'n', o método de definir data é chamado novamente
                self.dataReservar()
                break
            else: # se não foi nenhum dos dois, uma mensagem é exibida pro usuario e é pedido pra digitar a opção novamente
                print(f'''
 {erro}Comando não identificado{body}    
    ''')        

       
    def horarioReservar(self): # definir o horario
        global horario_f, horario_i
        self.horario = [] # atributo que vai armazenar o horario
        print('+', '-' * 45, '+')
        print('|\t\tESCOLHA O TURNO\t\t\t|')
        print(f'|\t[1] MANHÃ [2] TARDE\t\t\t|') # escolhendo o turno
        print('+', '-' * 45, '+')

        while True:
            try:
                opcao = int(input('--> '))
                if opcao == 1:
                    turno = 'manhã'
                    break # se a opção for 1 ou 2, o loop é quebrado
                elif opcao == 2:
                    turno = 'tarde'
                    break
                else:
                    print(f'{erro}OPÇÃO INVÁLIDA{body}') # se não, continua no loop
            except:
                print(f'{erro}OPÇÃO INVÁLIDA{body}')

        if turno == 'manhã': # se turno for manhã, uma série de horários é exibida, das 8h as 12h
            print('+', '-' * 45, '+')
            print('|\tESCOLHA O HORÁRIO DA RESERVA\t\t|')
            print('+', '-' * 45, '+')
            print(f''' \n    MANHÃ
\n[1] 8h às 9h
\n[2] 9h às 10h
\n[3] 10h às 11h
\n[4] 11h às 12h
''')
            while True:
                try:
                    opcao2 = int(input('--> '))
                    if opcao2 == 1:
                        horario_i = '08:00:00'
                        horario_f = '09:00:00'
                        break
                    elif opcao2 == 2:
                        horario_i = '09:00:00'
                        horario_f = '10:00:00'
                        break
                    elif opcao2 == 3:
                        horario_i = '10:00:00'
                        horario_f = '11:00:00'
                        break
                    elif opcao2 == 4:
                        horario_i = '11:00:00'
                        horario_f = '12:00:00'
                        break
                    else:
                        print(f'{erro}OPÇÃO INVÁLIDA{body}')
                except:
                    print(f'{erro}OPÇÃO INVÁLIDA{body}')

        elif turno == 'tarde': # se turno for igual a tarde, exibira os horarios da tarde das 13h as 17h
            print('+', '-' * 45, '+')
            print('|\tESCOLHA O HORÁRIO DA RESERVA\t\t|')
            print('+', '-' * 45, '+')
            print(f'''\n   TARDE
\n[5] 13h às 14h
\n[6] 14h às 15h
\n[7] 15h às 16h
\n[8] 16h às 17h
''')
            while True:
                try:
                    opcao2 = int(input('--> '))
                    if opcao2 == 5:
                        horario_i = '13:00:00'
                        horario_f = '14:00:00'
                        break
                    elif opcao2 == 6:
                        horario_i = '14:00:00'
                        horario_f = '15:00:00'
                        break
                    elif opcao2 == 7:
                        horario_i = '15:00:00'
                        horario_f = '16:00:00'
                        break
                    elif opcao2 == 8:
                        horario_i = '16:00:00'
                        horario_f = '17:00:00'
                        break
                    else:
                        print(f'{erro}OPÇÃO INVÁLIDA{body}')
                except:
                    print(f'{erro}OPÇÃO INVÁLIDA{body}')

        self.horario.append(horario_i) # adiciona o horario inicial e final ao atributo self.horario
        self.horario.append(horario_f)
        print('-'*47)
        print(f'\n{success}Horário das {self.horario[0]} as {self.horario[1]}{body}') # exibi o horario escolhido
        
    def nomeReservar(self): # nome do responsavel pela reserva
        self.nome = None # defini nome igual a None
        print('+', '-' * 45, '+')
        print(f'|\t\tDIGITE O SEU NOME\t\t|')
        print('+', '-' * 45, '+')
        nome = input('\n--> ').lower()
        nome = nome.replace(' ','_')
        if len(nome) < 3: # nome tem tamanho mínimo igual a 3
            print(f'Nome deve ter mais de 3 carcteres')
            self.nomeReservar() # se nome for menor que 3, chame novamente o medo nomeReservar()
        else: 
            self.nome_resp = nome

    def menu(self,sala): # método que chama todos os métodos da class
        system('cls') # limap o terminal quando for executado
        registro = [] # defini variavel registro, com todos os dados da reserva
        self.salaReservar(sala)
        self.dataReservar()
        self.horarioReservar()
        self.nomeReservar()
        registro.append(self.sala)
        registro.append(self.data[0])
        registro.append(self.data[1])
        registro.append(self.data[2])
        registro.append(self.horario[0])
        registro.append(self.horario[1])
        registro.append(self.nome_resp) # salvando todos os dados em reserva
        print(f'''+{'-' * 47}+
|\t\tREGISTRO\t\t\t|
+{'-' * 6}+{'-' * 40}+
| Nome | {self.nome_resp}
+{'-' * 6}+
| Sala | {self.sala}
+{'-' * 6}+
| Data | {self.data[2]}/{self.data[1]}/{self.data[0]}
+{'-' * 6}+--+
| Horário | {self.horario[0]} - {self.horario[1]}
+{'-' * 9}+
        ''') # exivi o registro
        while True:
            print(f'\n\tDESEJA SALVAR A RESERVA ? s/n') # perguntandos e deseja salvar a reserva
            opcao = input('--> ')
            if opcao == 's': # se sim, chama função de verificar e depois salva reserva
                verificarReserva(registro)
                sleep(1) # espera 1 segundo
                system('cls') # limpa o terminal
                break # para o loop
            elif opcao == 'n':
                print(f'''
 {erro}FINALIZANDO RESERVA{body}
            ''') # se não, só volta pro menu
                sleep(1)
                system('cls')
                break
            else: # se nenhuma das opções, continua no loop
                print(f'''
{erro}OPÇÃO INVÁLIDA{body}
            ''')
        