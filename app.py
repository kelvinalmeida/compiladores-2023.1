from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# @app.route('/login', methods=['GET', 'POST']):
#   if flask.request.method == 'POST':
#     userEmail = request.form['userEmail']
#     userPassword = request.form['userPassword']
#     return flask.redirect('/')
#   return flask.render_template('form_filename.html')

@app.route('/processar_formulario', methods=['POST'])
def form_post():
    codigoFonteReq = request.form['condigoFonte']
    print(codigoFonteReq)
    
    # return userEmail

