from flask import Flask, render_template, request

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
    
    # Adicione uma resposta de retorno para a solicitação POST
    return "Dados do formulário recebidos com sucesso!"

if __name__ == "__main__":
    app.run()