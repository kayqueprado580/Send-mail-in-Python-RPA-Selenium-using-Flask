from flask import Flask, request, request, Response, jsonify
import mailScripts
import sys
global dataMail

door=sys.argv[1]
usuario=sys.argv[2]
password=sys.argv[3]

app = Flask(__name__)

@app.route("/")
def start():
    dataMail={"status":"success","code":1,"description":"success"}
    mailScripts.openBrowser()
    return jsonify(dataMail)

@app.route('/login',methods=['POST'])
def logar():
    response={"status":"sucess","code":1,"description":"Logado com Sucesso"}
    # valuesEntrada=request.json
    # usuario=valuesEntrada['user']
    # senha=valuesEntrada['password']
    try:
        mailScripts.login(usuario, password)
    except:
        response['status'] = 'failed'
        response['code'] = 0
        response['description'] = "Falha de nao encontrar elemento"
    return jsonify(response)

@app.route('/enviar',methods=['POST'])
def send():
    response={"status":"success","code":1,"description":"success"}
    valuesEntrada=request.json
    remetente=valuesEntrada['para']
    assunto=valuesEntrada['assunto']
    mensagem=valuesEntrada['mensagem']
    try:
        mailScripts.enviar_email(remetente, assunto, mensagem)
    except:
        response['status'] = 'failed'
        response['code'] = 0
        response['description'] = "Falha de nao encontrar elemento"
    return jsonify(response)

@app.route('/kill')
def killer():
    response={"status":"success","code":1,"description":"Navegador Fechado com Sucesso"}

    try:
        mailScripts.kill()
    except:
        response['status'] = 'failed'
        response['code'] = 0
        response['description'] = "Falha ao fechar navegador"
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=door) #run app
