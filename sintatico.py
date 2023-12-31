
import lexico
import sys # Para parar o programa apos um erro.
from selenium import webdriver
import time


driver = webdriver.Chrome()
count = 0
lookahead = ''
vezesLoop = 1
errorReturn = False

def parse():
    global lookahead
    global count
    global vezesLoop
    global errorReturn

    errorReturn = False
    count = 0
    lookahead = lexico.palavrasTratadas[count]
    vezesLoop = 1
    
    if(lookahead == 'programa_SOL'):
        matchLookAhead('programa_SOL')
        programa_SOL()
    else:
        error()


def programa_SOL():
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count
    global vezesLoop
    if(lookahead == 'loop'):
        matchLookAhead('loop')
        vezesLoop = vezes()

        for i in range(0, vezesLoop):
            
            # apos a primeira repetição
            if(i > 0):
                lookahead = lexico.palavrasTratadas[3]
                count = 3

            sequencia()
    else:
        error()
    
def vezes():
    
    global errorReturn
    if(errorReturn):
        return
    
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
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    fase_EPIC = ['20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;']
    presentList = ['link_pdf','link_video', 'endereço_meet']
    

    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 < len(lexico.palavrasTratadas)):
        lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    else:
        error()

    # ir para fases_EPIC
    if((lookahead == 'navegador') and (lookaheadPreeditivo in fase_EPIC)):
        print('------------')
        lexico.comentarios.append('------------' + '<br>')
        print('**FASES_EPIC')
        lexico.comentarios.append('**FASES_EPIC' + '<br>')
        print('------------')
        lexico.comentarios.append('------------' + '<br>')
        fases_EPIC()
    # Ir para Present
    elif((lookahead == 'navegador') and (lookaheadPreeditivo in presentList)):
        # print('**PRESENT')
        print('------------')
        lexico.comentarios.append('------------' + '<br>')
        present()
    else:
        error()

def fases_EPIC():
    
    global errorReturn
    if(errorReturn):
        return
    
    explore()
    present()
    interact()
    critique()

def explore():
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count

    explorerList = ['1_dia;' , '20_min;' , '2_dias;', 'sem_limite;', '15_min;', '1_hora;']
    # presentList = ['link_pdf' , 'link_video' , 'endereço_meet']
    # interactList = ['link_whatsapp_web' , 'link_email' , 'endereço_meet']
    lookaheadPreeditivo = ''

    # Verifica se o count não ultrapassa o array de palavrasTratadas
    try:
        if(count + 1 < len(lexico.palavrasTratadas)):
            lookaheadPreeditivo = lexico.palavrasTratadas[count + 1]
    except:
        error()
        
    # Se não for presente ou interact RETORNA
    # lookaheadPreeditivoPresent = (lookaheadPreeditivo in presentList)
    # lookaheadPreeditivoInteract = (lookaheadPreeditivo in interactList)
    # if(lookaheadPreeditivoPresent or lookaheadPreeditivoInteract):
    #     return

    # Se não for explorer
    if(not (lookaheadPreeditivo in explorerList)):
        return
    
    print('**EXPLORER')
    lexico.comentarios.append('**EXPLORER' + '<br>')

    if(count + 1 == len(lexico.palavrasTratadas)):
        return
    
    if(lookahead == 'navegador'):
        matchLookAhead('navegador')        
        print('Executando o navegador')
        lexico.comentarios.append('Executando o navegador' + '<br>')
        tempo('navegador')
        print('------------')
        lexico.comentarios.append('------------' + '<br>')
        # Recursão do explor
        explore()

    else:
        error()

def tempo(tipo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    if(lookahead == '20_min;'):
        matchLookAhead('20_min;')
        print('por 20_min')
        lexico.comentarios.append('por 20_min' + '<br>')
        abrirComandos(tipo, '20_min;')
    elif(lookahead == '1_dia;'):
        matchLookAhead('1_dia;')
        print('por 1_dia')
        lexico.comentarios.append('por 1_dia' + '<br>')
        abrirComandos(tipo, '1_dia;')
    elif(lookahead == '2_dias;'):
        matchLookAhead('2_dias;')
        print('por 2_dias')
        lexico.comentarios.append('por 2_dias' + '<br>')
        abrirComandos(tipo, '2_dias;')
    elif(lookahead == 'sem_limite;'):
        matchLookAhead('sem_limite;')
        print('por sem_limite')
        lexico.comentarios.append('por sem_limite' + '<br>')
        abrirComandos(tipo, 'sem_limite;')
    elif(lookahead == '15_min;'):
        matchLookAhead('15_min;')
        print('por 15_min')
        lexico.comentarios.append('por 15_min' + '<br>')
        abrirComandos(tipo, '15_min;')
    elif(lookahead == '1_hora;'):
        matchLookAhead('1_hora;')
        print('por 1_hora')
        lexico.comentarios.append('por 1_hora' + '<br>')
        abrirComandos(tipo, '1_hora;')
    else:
        error()

def present():
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count

    if(count + 1 == len(lexico.palavrasTratadas)):
        return
    
    print('**PRESENT')
    lexico.comentarios.append('**PRESENT' + '<br>')
    
    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_pdf'):
            matchLookAhead('link_pdf')
            print('executar link_pdf.')
            lexico.comentarios.append('executar link_pdf.' + '<br>')
            tempo('link_pdf')
        elif(lookahead == 'link_video'):
            matchLookAhead('link_video')            
            print('executar link_video.')
            lexico.comentarios.append('executar link_video.' + '<br>')
            tempo('link_video')
        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')            
            print('executar endereço_meet.')
            lexico.comentarios.append('executar endereço_meet.' + '<br>')
            tempo('endereço_meet')
        else:
            error()
    else:
        error()

    print('------------')
    lexico.comentarios.append('------------' + '<br>')

def interact():
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count

    if(count + 1 == len(lexico.palavrasTratadas)):
        return
    
    print('**INTERACT')
    lexico.comentarios.append('**INTERACT' + '<br>')

    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_whatsapp_web'):
            matchLookAhead('link_whatsapp_web')
            print('executar link_whatsapp_web.')
            lexico.comentarios.append('executar link_whatsapp_web.' + '<br>')
            tempo('link_whatsapp_web')
        elif(lookahead == 'link_email'):
            matchLookAhead('link_email')
            print('executar link_email.')
            lexico.comentarios.append('executar link_email.' + '<br>')
            tempo('link_email')

        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')
            print('executar endereço_meet.')
            lexico.comentarios.append('executar endereço_meet.' + '<br>')
            tempo('endereço_meet')
        else:
            error()
    else:
        error()

    print('------------')
    lexico.comentarios.append('------------' + '<br>')

def critique():
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count
    
    # Verifica se o count não ultrapassa o array de palavrasTratadas
    if(count + 1 == len(lexico.palavrasTratadas)):
        return
    
    print('**CRITIQUE')
    lexico.comentarios.append('**CRITIQUE' + '<br>')

    if(lookahead == 'navegador'):
        matchLookAhead('navegador')
        if(lookahead == 'link_whatsapp_web'):
            matchLookAhead('link_whatsapp_web')
            print('executar link_whatsapp_web.')
            lexico.comentarios.append('executar link_whatsapp_web.' + '<br>')
            tempo('link_whatsapp_web')
        elif(lookahead == 'link_email'):
            matchLookAhead('link_email')
            print('executar link_email.')
            lexico.comentarios.append('executar link_email.' + '<br>')
            tempo('link_email')

        elif(lookahead == 'endereço_meet'):
            matchLookAhead('endereço_meet')
            print('executar endereço_meet.')
            lexico.comentarios.append('executar endereço_meet.' + '<br>')
            tempo('endereço_meet')
        else:
            error()
    else:
        error()

    print('------------')
    lexico.comentarios.append('------------' + '<br>')

def matchLookAhead(token):
    
    global errorReturn
    if(errorReturn):
        return
    
    global lookahead
    global count
    if(token == lookahead):
        if(count < len(lexico.palavrasTratadas) - 1):
            count += 1
            lookahead = lexico.palavrasTratadas[count]
    else:
        error()

def error():
    
    global errorReturn
    errorReturn = True
    print('Erro Sintatico')
    lexico.comentarios.append('Erro Sintatico' + '<br>')
    print()
    lexico.comentarios.append('<br>')
    # sys.exit()


def abrirComandos(tipo, tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
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
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://google.com/")
    timeSleep(tempo)

def abrirVideoConferencia(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://meet.google.com/")
    timeSleep(tempo)

def abrirWhatsappWeb(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://web.whatsapp.com/")
    timeSleep(tempo)

def abrirEmail(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://mail.google.com/")
    timeSleep(tempo)

def abrirPDF(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://inc.saude.gov.br/download/50_receitas.pdf")
    timeSleep(tempo)

def abrirVideo(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    global driver
    driver.get("https://www.youtube.com/")
    timeSleep(tempo)

def timeSleep(tempo):
    
    global errorReturn
    if(errorReturn):
        return
    
    if(tempo == '20_min;'):
        time.sleep(3)
    elif(tempo == '1_dia;'):
        time.sleep(3)
    elif(tempo == '2_dias;'):
        time.sleep(3)
    elif(tempo == 'sem_limite;'):
        time.sleep(3)
    elif(tempo == '15_min;'):
        time.sleep(3)
    elif(tempo == '1_hora;'):
        time.sleep(3)


# lexico()
# parse()
print()