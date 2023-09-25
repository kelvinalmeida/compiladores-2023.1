
import lexico
import sys # Para parar o programa apos um erro.
from selenium import webdriver
import time

driver = webdriver.Chrome()

count = 0
lookahead = lexico.palavrasTratadas[count]
vezesLoop = 1

def parse():
    global lookahead
    if(lookahead == 'programa_SOL'):
        matchLookAhead('programa_SOL')
        programa_SOL()
    else:
        error()


def programa_SOL():
    global lookahead
    global count
    global vezesLoop
    if(lookahead == 'loop'):
        matchLookAhead('loop')
        vezesLoop = vezes()

        for i in range(0, vezesLoop):
            
            if(i > 0):
                lookahead = lexico.palavrasTratadas[3]
                count = 3

            sequencia()
    else:
        error()
    
def vezes():
    global lookahead
    if(lookahead == '1'):
        matchLookAhead('1')
        return 1
    elif(lookahead == '2'):
        matchLookAhead('2')
        return 2
    elif(lookahead == '3'):
        matchLookAhead('3')
        return 3
    elif(lookahead == '4'):
        matchLookAhead('4')
        return 4
    elif(lookahead == '5'):
        matchLookAhead('5')
        return 5
    else:
        error()

def sequencia():
    global lookahead
    fase_EPIC = ['20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;']
    presentList = ['link_pdf','link_video', 'endereço_meet']

    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        return

    # ir para fases_EPIC
    if((lookahead == 'navegador') and (lookaheadPreeditivo in fase_EPIC)):
        fases_EPIC()
    # Ir para Present
    elif((lookahead == 'navegador') and (lookaheadPreeditivo in presentList)):
        present()
    else:
        error()

def fases_EPIC():
    explore()
    present()
    interact()
    critique()

def explore():
    global lookahead
    global count
    # presentList = ['link_pdf','link_video', 'endereço_meet']
    explorerList = ['20_min;' , '1_hora;' , '1_dia;' , '2_dias;' , 'sem_limite;', '15_min;']


    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        return

    # Se não for explorer RETORNA
    if(not (lookaheadPreeditivo in explorerList)):
        return
    elif(lookahead == 'navegador'):
        matchLookAhead('navegador')
        print('Executando o navegador')
        tempo('navegador')
        # Recursão do explore
        explore()
    else:
        error()

def tempo(tipo):
    global lookahead
    if(lookahead == '20_min;'):
        matchLookAhead('20_min;')
        print('por 20_min')
        abrirComandos(tipo, '20_min;')
    elif(lookahead == '1_dia;'):
        matchLookAhead('1_dia;')
        print('por 1_dia')
        abrirComandos(tipo, '1_dia;')
    elif(lookahead == '2_dias;'):
        matchLookAhead('2_dias;')
        print('por 2_dias')
        abrirComandos(tipo, '2_dias;')
    elif(lookahead == 'sem_limite;'):
        matchLookAhead('sem_limite;')
        print('por sem_limite')
        abrirComandos(tipo, 'sem_limite;')
    elif(lookahead == '15_min;'):
        matchLookAhead('15_min;')
        print('por 15_min')
        abrirComandos(tipo, '15_min;')
    elif(lookahead == '1_hora;'):
        matchLookAhead('1_hora;')
        print('por 1_hora')
        abrirComandos(tipo, '1_hora;')
    else:
        error()

def present():
    global lookahead
    global count

    presentList = ['link_pdf' , 'link_video' , 'endereço_meet']


    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        return

    # Se não for present RETORNA
    if(not (lookaheadPreeditivo in presentList)):
        return

    # if(count + 1 == len(lexico.palavrasTratadas)):
    #     return
    
    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_pdf'):
            matchLookAhead('link_pdf')
            print('executar link_pdf.')
            tempo('link_pdf')
        elif(lookahead == 'link_video'):
            matchLookAhead('link_video')            
            print('executar link_video.')
            tempo('link_video')
        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')            
            print('executar endereço_meet.')
            tempo('endereço_meet')
        else:
            error()
    else:
        error()

def interact():
    global lookahead
    global count

    interactList = ['link_whatsapp_web' , 'link_email' , 'endereço_meet']


    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        return

    # Se não for interact RETORNA
    if(not (lookaheadPreeditivo in interactList)):
        return

    # if(count + 1 == len(lexico.palavrasTratadas)):
    #     return

    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_whatsapp_web'):
            matchLookAhead('link_whatsapp_web')
            print('executar link_whatsapp_web.')
            tempo('link_whatsapp_web')
        elif(lookahead == 'link_email'):
            matchLookAhead('link_email')
            print('executar link_email.')
            tempo('link_email')

        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')
            print('executar endereço_meet.')
            tempo('endereço_meet')
        else:
            error()
    else:
        error()

def critique():
    global lookahead
    global count

    interactList = ['link_whatsapp_web' , 'link_email' , 'endereço_meet']


    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        return

    # Se não for interact RETORNA
    if(not (lookaheadPreeditivo in interactList)):
        return

    # if(count + 1 == len(lexico.palavrasTratadas)):
    #     return

    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_whatsapp_web'):
            matchLookAhead('link_whatsapp_web')
            print('executar link_whatsapp_web.')
            tempo('link_whatsapp_web')
        elif(lookahead == 'link_email'):
            matchLookAhead('link_email')
            print('executar link_email.')
            tempo('link_email')

        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')
            print('executar endereço_meet.')
            tempo('endereço_meet')
        else:
            error()
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
    print()
    sys.exit()


def abrirComandos(tipo, tempo):
    if(tipo == 'navegador'):
        abrirNavegador(tempo)
    elif(tipo == 'link_pdf'):
        abrirPDF(tempo)
    elif(tipo == 'link_video'):
        abrirVideo(tempo)
    elif(tipo == 'link_whatsapp_web'):
        abrirWhatsappWeb(tempo)
    elif(tipo == 'link_email'):
        abrirEmail(tempo)
    elif(tipo == 'endereço_meet'):
        abrirVideoConferencia(tempo)


def abrirNavegador(tempo):
    global driver
    driver.get("https://google.com/")
    timeSleep(tempo)

def abrirVideoConferencia(tempo):
    global driver
    driver.get("https://meet.google.com/")
    timeSleep(tempo)

def abrirWhatsappWeb(tempo):
    global driver
    driver.get("https://web.whatsapp.com/")
    timeSleep(tempo)

def abrirEmail(tempo):
    global driver
    driver.get("https://mail.google.com/")
    timeSleep(tempo)

def abrirPDF(tempo):
    global driver
    driver.get("https://inc.saude.gov.br/download/50_receitas.pdf")
    timeSleep(tempo)

def abrirVideo(tempo):
    global driver
    driver.get("https://www.youtube.com/")
    timeSleep(tempo)

def timeSleep(tempo):
    if(tempo == '20_min;'):
        time.sleep(5)
    elif(tempo == '1_dia;'):
        time.sleep(5)
    elif(tempo == '2_dias;'):
        time.sleep(5)
    elif(tempo == 'sem_limite;'):
        time.sleep(5)
    elif(tempo == '15_min;'):
        time.sleep(5)
    elif(tempo == '1_hora;'):
        time.sleep(5)


# lexico()
parse()
print()