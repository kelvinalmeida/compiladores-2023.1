
import lexico

count = 0
lookahead = lexico.palavrasTratadas[count]

def parse():
    if(lookahead == 'programa_SOL'):
        matchLookAhead('programa_SOL')
        programa_SOL()
    else:
        error()


def programa_SOL():
    if(lookahead == 'loop'):
        matchLookAhead('loop')
        vezes()
        sequencia()
    
def vezes():
    if(lookahead == '1'):
        matchLookAhead('1')
    elif(lookahead == '2'):
        matchLookAhead('2')
    elif(lookahead == '3'):
        matchLookAhead('3')
    elif(lookahead == '4'):
        matchLookAhead('4')
    elif(lookahead == '5'):
        matchLookAhead('5')
    else:
        error()

def sequencia():
    listasTempos = ['20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;',]

    lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]

    # ir para fases_EPIC
    if((lookahead == 'navegador') and (lookaheadPreeditivo in listasTempos)):
        explore()
        # present()
        # interact()
        # critique()
        
    # elif()


def explore():
    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        tempo()
        print('Executando Navegador em ' + str(lookahead))
    else:
        error()

def tempo():
    
    if(lookahead == '20_min;'):
        matchLookAhead('20_min;')
    elif(lookahead == '1_dia;'):
        matchLookAhead('1_dia;')
    elif(lookahead == '2_dias;'):
        matchLookAhead('2_dias;')
    elif(lookahead == 'sem_limite;'):
        matchLookAhead('sem_limite;')
    elif(lookahead == '15_min;'):
        matchLookAhead('15_min;')
    else:
        error()

def matchLookAhead(token):
    if(token == lookahead):
        if(count < len(lexico.palavrasTratadas)):
            count += 1
            lookahead = lexico.palavrasTratadas[count]
    else:
        error()

def error():
    print('Erro Sintatico')


# lexico()
parse()