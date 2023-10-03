import sys # Para parar o programa apos um erro.

def escritoCorretamente(palavra):

    aux = palavra

    if(';' in palavra):
        aux = aux.replace(';', '')
        # print(aux)

    palavrasReservadas = ['programa_SOL', 'loop', 'navegador', '20_min', '1_hora', '1_dia', '2_dias', 'sem_limite', '15_min', 'endereço_meet', 'link_pdf', 'link_video', 'link_whatsapp_web', 'link_email', '1', '2', '3', '4', '5']
    
    if(aux in palavrasReservadas):
        return True
    else:
         return False


palavrasDoCodigoFonte = []
palavrasTratadas = []
linha = 1
ignorar = False
adiconarLinha = False

# Ler o arquivo
texto = open('texto.txt', 'r', encoding='utf-8')
lista = texto.readlines()

print(lista)

for i in range(0, len(lista)):
    aux = lista[i].split(' ')
    palavrasDoCodigoFonte = palavrasDoCodigoFonte + aux
texto.close()

print(palavrasDoCodigoFonte)

# print(palavrasDoCodigoFonte)

for i in range(0, len(palavrasDoCodigoFonte)):

    # Remover Comentários
    if(palavrasDoCodigoFonte[i][0] in '//' or ignorar):
        ignorar = True

        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                    # linha += 1
                    adiconarLinha = True
                    ignorar = False


    # verificar identificador
    elif(palavrasDoCodigoFonte[i][0].isalpha()):

        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                # linha += 1
                adiconarLinha = True

        palavrasDoCodigoFonte[i] = palavrasDoCodigoFonte[i].split()[0]
        palavrasTratadas.append(palavrasDoCodigoFonte[i].split()[0])

        # Se não estiver escrito corretamente
        if(not (escritoCorretamente(palavrasDoCodigoFonte[i]))):
            print('**Erro Lexico')
            print('**Erro com a palavra ' + '\'' + palavrasDoCodigoFonte[i] + '\'' + ' na linha ' + str(linha + 1 if linha  == 0 else linha))
            sys.exit()

    # Verificar digito
    elif(palavrasDoCodigoFonte[i][0].isdigit()):
        
        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                # linha += 1
                adiconarLinha = True

        palavrasDoCodigoFonte[i] = palavrasDoCodigoFonte[i].split()[0]
        palavrasTratadas.append(palavrasDoCodigoFonte[i].split()[0])

        # Se não estiver escrito corretamente
        if(not (escritoCorretamente(palavrasDoCodigoFonte[i]))):
            print('**Erro Lexico')
            print('Erro com a palavra ' + '\'' + palavrasDoCodigoFonte[i] + '\'' + ' na linha ' + str(linha + 1 if linha  == 0 else linha))
            sys.exit()

    if(adiconarLinha):
        linha += 1
        adiconarLinha = False


print()
# print(palavrasDoCodigoFonte)
print("**Quantidade de linhas do código fonte: " + str(linha))
# print(palavrasDoCodigoFonte)
print("**Palavras do Codigo fonte: " + str(palavrasTratadas))
print()