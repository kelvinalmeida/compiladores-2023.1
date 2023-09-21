import re

def escritoCorretamente(palavra):
    palavrasReservadas = ['programa_SOL', 'loop', 'navegador', '20_min;', '1_hora;', '1_dia;', '2_dias;', 'sem_limite;', '15_min;', 'endereço_meet',]
    
    if(palavra in palavrasReservadas):
        return True
    else:
         return False


palavrasDoCodigoFonte = []
palavrasTratadas = []
linha = 1
ignorar = False

# Ler o arquivo
texto = open('texto.txt', 'r', encoding='utf-8')
lista = texto.readlines()

for i in range(0, len(lista)):
    aux = lista[i].split(' ')
    palavrasDoCodigoFonte = palavrasDoCodigoFonte + aux
texto.close()

# print(palavrasDoCodigoFonte)

for i in range(0, len(palavrasDoCodigoFonte)):

    # Remover Comentários
    if(palavrasDoCodigoFonte[i][0] in '//' or ignorar):
        ignorar = True

        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                    linha += 1
                    ignorar = False


    # verificar identificador
    elif(palavrasDoCodigoFonte[i][0].isalpha()):

        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                    linha += 1

        palavrasDoCodigoFonte[i] = palavrasDoCodigoFonte[i].split()[0]
        palavrasTratadas.append(palavrasDoCodigoFonte[i].split()[0])

        # Verificar se está escrito corretamente
        if(escritoCorretamente(palavrasDoCodigoFonte[i]) == False):
            print('Erro com a palavra ' + '\'' + palavrasDoCodigoFonte[i] + '\'' + ' na linha ' + str(linha))
            break

    # Verificar digito
    elif(palavrasDoCodigoFonte[i][0].isdigit()):
        for letra in palavrasDoCodigoFonte[i]:
            if(letra == '\n'):
                    linha += 1

        palavrasDoCodigoFonte[i] = palavrasDoCodigoFonte[i].split()[0]
        palavrasTratadas.append(palavrasDoCodigoFonte[i].split()[0])

        # Verificar se está escrito corretamente
        if((escritoCorretamente(palavrasDoCodigoFonte[i]) == False) and (palavrasDoCodigoFonte[i].isdigit() == False)):
            print('Erro com a palavra ' + '\'' + palavrasDoCodigoFonte[i] + '\'' + ' na linha ' + str(linha))
            break


print()
print(palavrasDoCodigoFonte)
print("**Quantidade de linhas do código fonte: " + str(linha))
# print(palavrasDoCodigoFonte)
print("**Palavras do Codigo fonte: " + str(palavrasTratadas))
print()