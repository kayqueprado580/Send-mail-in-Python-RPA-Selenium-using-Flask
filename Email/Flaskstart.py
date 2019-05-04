from flask import Flask, request, Response,jsonify
import requests
import json
import dataset
import sys
from datetime import datetime
import bat
global dataStart

app = Flask(__name__)
contadorSessoes = 1

@app.route('/start',methods=['POST'])
def startProcess():
    global contadorSessoes
    dataStart={"status":"success","code":1,"description":"success"}
    if not request.json:
        dataStart['status'] = "error START"
        dataStart['code'] = 66
        dataStart['description']="O objeto recebido não esta no formato json"
        return jsonify(dataStart)
    valuesAcess=request.json
    accountUser=valuesAcess['user']
    accountPort=valuesAcess['port']
    accountPasssword=valuesAcess['password']
    services=valuesAcess['service']
    action=valuesAcess['action']
    service=services.lower()

    if action == "start":
        try:
            arquivolog = open("C:\\Users\\Kayque\\Desktop\\Email\\log.txt","a")
            bat.startProcess(accountUser,accountPasssword,accountPort,service)
            contadorSessoes = contadorSessoes + 1
            #print("start na porta: {} - contadorSessoes: {}".format(accountPort, contadorSessoes))
            now = datetime.now()
            arquivolog.write("{} --- start na porta: {} - contadorSessoes: {} - service: {}\n".format(now.strftime("%d/%m/%y -- %H:%M"), accountPort, contadorSessoes, service))
            arquivolog.close()
            return jsonify(dataStart)
        except Exception as e:
            print(e)
            dataStart['status'] = "error START"
            dataStart['code'] = 299
            dataStart['description']="O sistema encontrou um erro ao tentar iniciar o serviço"
            return jsonify(dataStart),299

    if action == "stop":
        try:
            r = requests.get('localhost/kill'.format(accountPort))
            print(r.status_code)
            arquivolog = open("C:\\Users\\Kayque\\Desktop\\Email\\log.txt","a")
            now = datetime.now()
            arquivolog.write("{} --- stop na porta: {} - service: {}\n".format(now.strftime("%d/%m/%y -- %H:%M"), accountPort, service))
            arquivolog.close()
        except:
            pass
        try:
            bat.stopProcess(accountPort)
        except:
            pass

        return jsonify(dataStart)
    else:
        print("Erro na ação")
        dataStart['status'] = "error START"
        dataStart['code'] = 102
        dataStart['description']="Erro ao finalizar o processo"
        return jsonify(dataStart),102
    return jsonify(dataStart)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',threaded=True) #run app
