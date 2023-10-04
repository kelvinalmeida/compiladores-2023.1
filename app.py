from flask import Flask, render_template, request
import lexico
import sintatico

app = Flask(__name__)

palaCodigoFonte = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/processar_formulario', methods=['POST'])
def form_post():
    codigoFonteReq = request.form['condigoFonte']
    print(codigoFonteReq)
    ReqCodigoFont = codigoFonteReq.split(' ')
    ReqCodigoFont = codigoFonteReq.split('\n')

    global palaCodigoFonte
    palaCodigoFonte = []
    for i in range(0, len(ReqCodigoFont)):
        aux = ReqCodigoFont[i].split(' ')
        palaCodigoFonte = palaCodigoFonte + aux

    print(palaCodigoFonte)
    lexico.palavrasDoCodigoFonte = palaCodigoFonte
    lexico.lexicoStart()
    sintatico.parse()
    
    # Adicione uma resposta de retorno para a solicitação POST
    return "Comando Executados Com Sucesso!"

if __name__ == "__main__":
    app.run()