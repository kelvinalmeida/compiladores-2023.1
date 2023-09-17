
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
    listasTempos = ['20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;']

    lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]

    if((lookahead == 'navegador') and (lookaheadPreeditivo in listasTempos)):
        matchLookAhead('navegador')
        
    # elif()

def matchLookAhead(token):
    if(token == lookahead):
        count += 1
        lookahead = lexico.palavrasTratadas[count]
    else:
        error()

def error():
    print('Erro Sintatico')