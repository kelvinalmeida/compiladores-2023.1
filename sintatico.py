
import lexico

count = 0
lookahead = lexico.palavrasTratadas[count]

def parse():
    global lookahead
    if(lookahead == 'programa_SOL'):
        matchLookAhead('programa_SOL')
        programa_SOL()
    else:
        error()


def programa_SOL():
    global lookahead
    if(lookahead == 'loop'):
        matchLookAhead('loop')
        vezes()
        sequencia()
    else:
        error()
    
def vezes():
    global lookahead
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
    global lookahead
    fase_EPIC = ['20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;']
    presentList = ['link_whatsapp_web', 'link_video', 'endereço_meet']

    lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]

    # ir para fases_EPIC
    if((lookahead == 'navegador') and (lookaheadPreeditivo in fase_EPIC)):
        fases_EPIC()

    # Ir para Present
    elif((lookahead == 'navegador') and (lookaheadPreeditivo in presentList)):
        present()
        tempo()
    else:
        error()

def fases_EPIC():
    explore()
    # present()
    # interact()
    # critique()

def explore():
    global lookahead
    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        print('Executando o navegador')
        tempo()
    else:
        error()

def tempo():
    global lookahead
    if(lookahead == '20_min;'):
        matchLookAhead('20_min;')
        print('por 20_min')
    elif(lookahead == '1_dia;'):
        matchLookAhead('1_dia;')
        print('por 1_dia')
    elif(lookahead == '2_dias;'):
        matchLookAhead('2_dias;')
        print('por 2_dias')
    elif(lookahead == 'sem_limite;'):
        matchLookAhead('sem_limite;')
        print('por sem_limite')
    elif(lookahead == '15_min;'):
        matchLookAhead('15_min;')
        print('por 15_min')
    else:
        error()

def present():
    global lookahead

    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        # visualizarPDF()
        # visuzlizarVideo()
        videoConferencia()
    else:
        error()

def videoConferencia():
    global lookahead
    if(lookahead == 'endereço_meet'):
        matchLookAhead('endereço_meet')
        print("Abrindo Vídeo conferencia no meet.")
    else:
        error()


def matchLookAhead(token):
    global lookahead
    global count
    if(token == lookahead):
        if(count < len(lexico.palavrasTratadas) - 1):
            count += 1
            lookahead = lexico.palavrasTratadas[count]
    else:
        error()

def error():
    print('Erro Sintatico')


# lexico()
parse()
print()