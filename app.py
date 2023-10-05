from flask import Flask, render_template, request, jsonify
import lexico
import sintatico

app = Flask(__name__)

palaCodigoFonte = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/processar_formulario', methods=['POST'])
def form_post():
    data = request.json  # Obtenha os dados JSON da solicitação
    # print(data['condigoFonte'])
    codigoFonteReq = data['condigoFonte']

    linhas = codigoFonteReq.split('\n')

    tokens_com_quebras_de_linha = []

    # Processar cada linha
    for i in range(0, len(linhas)):
        aux = []
        if(i < len(linhas) - 1):
            aux.append(linhas[i])
            aux.append('\n')
            string = ''.join(aux)
            tokens_com_quebras_de_linha.append(string)
        else:
            tokens_com_quebras_de_linha.append(linhas[i])

    # aux3 = tokens_com_quebras_de_linha[len(tokens_com_quebras_de_linha) - 1]
    print(tokens_com_quebras_de_linha)


    global palaCodigoFonte
    palaCodigoFonte = []
    for i in range(0, len(tokens_com_quebras_de_linha)):
        aux = tokens_com_quebras_de_linha[i].split(' ')
        palaCodigoFonte = palaCodigoFonte + aux

    print(palaCodigoFonte)
    lexico.palavrasDoCodigoFonte = palaCodigoFonte

    lexico.lexicoStart()

    if(not lexico.erroLexico):
        sintatico.parse()

    exibirResposta = ' '.join(lexico.comentarios)

    print('---> ' + exibirResposta)
    
    # Adicione uma resposta de retorno para a solicitação POST
    # return "Comando Executados Com Sucesso!"
    resultado = {'mensagem': exibirResposta}
    return jsonify(resultado)  
    

if __name__ == "__main__":
    app.run()