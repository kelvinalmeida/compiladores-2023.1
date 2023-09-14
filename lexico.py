import re

def escritoCorretamente(palavra):
    palavrasReservadas = ['programa_SOL', 'loop', 'navegador', '20_min']
    
    if(palavra in palavrasReservadas):
        return True
    else:
         return False


palavrasComComentarios = []
linha = 1

# Ler o arquivo
texto = open('texto.txt', 'r')
lista = texto.readlines()

for i in range(0, len(lista)):
    aux = lista[i].split(' ')
    palavrasComComentarios = palavrasComComentarios + aux
texto.close()

print(palavrasComComentarios)

for i in range(0, len(palavrasComComentarios)):

    # verificar identificador
    if(palavrasComComentarios[i][0].isalpha()):

        for letra in palavrasComComentarios[i]:
            if(letra == '\n'):
                    linha += 1

        palavrasComComentarios[i] = palavrasComComentarios[i].split()[0]

        # Verificar se está escrito corretamente
        if(escritoCorretamente(palavrasComComentarios[i]) == False):
           print('Erro com a palavra ' + '\'' + palavrasComComentarios[i] + '\'' + ' na linha ' + str(linha))
           break

    # Verificar digito
    if(palavrasComComentarios[i][0].isdigit()):
        for letra in palavrasComComentarios[i]:
            if(letra == '\n'):
                    linha += 1

        palavrasComComentarios[i] = palavrasComComentarios[i].split()[0]

        # Verificar se está escrito corretamente
        if((escritoCorretamente(palavrasComComentarios[i]) == False) and (palavrasComComentarios[i].isdigit() == False)):
           print('Erro com a palavra ' + '\'' + + palavrasComComentarios[i] + '\'' + ' na linha ' + str(linha))
           break

    # Remover Comentários
    

print(linha)