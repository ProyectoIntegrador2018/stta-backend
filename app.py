from flask import Flask, request
from flask_cors import CORS
from tools.Database import Database
from tools.APIFilResponse import APIFilSuccess, APIFilResponse
from tools.EmailManager import EmailManager

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/boolAdminLogin', methods=["POST","GET"])
def boolAdminLogin():
    data = Database.callSP('boolAdminLogin', [request.form['email'],
                                              request.form['password']])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)


@app.route('/addTokenAdmin', methods=["POST","GET"])
def addTokenAdmin():
    data = Database.callSP('addTokenAdmin', [request.form['email'],1])

    EmailManager.sendPasswordLink(link=data[0][0], email=request.form['email'])
    return APIFilSuccess.response(APIFilResponse.OK, data=[[1]])

@app.route('/getProcesosPasos', methods=["POST","GET"])
def getProcesosPasos():
    data = Database.callSP('getProcesosPasos', [], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/getDocumentos', methods=["POST","GET"])
def getDocumentos():
    data = Database.callSP('getDocumentos', [], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/getPasos', methods=["POST","GET"])
def getPasos():
    data = Database.callSP('getPasos', [request.form['id_proceso']], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/addDocument', methods=["POST","GET"])
def addDocument():
    data = Database.callSP('addDocument', [request.form['filename'],request.form['content']])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

if __name__ == '__main__':
    app.run()
