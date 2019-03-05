import json
import sys
from functools import wraps

from flask import Flask, request
from flask_cors import CORS
from tools.Database import Database
from tools.APIFilResponse import APIFilSuccess, APIFilResponse, APIFilException
from tools.EmailManager import EmailManager

app = Flask(__name__)
CORS(app)

def login_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data = Database.callSP('getValidationAdminToken', [request.headers.get('X-Access-Token')])
        if len(data) == 0:
            return APIFilException.raiseAPIException(APIFilResponse.AUTH_FAILED)
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/boolAdminLogin', methods=["POST","GET"])
def boolAdminLogin():
    data = Database.callSP('boolAdminLogin', [request.form['email'],
                                              request.form['password']])
    if data[0][0] == 1:
        if request.form['remember'] == '1':
            data = Database.callSP('addTokenAdmin', [request.form['email'],2])
        else:
            data = Database.callSP('addTokenAdmin', [request.form['email'],3])

    else:
        return APIFilException.raiseDBException(code=data[0][0])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)


@app.route('/addTokenAdmin', methods=["POST","GET"])
def addTokenAdmin():
    data = Database.callSP('addTokenAdmin', [request.form['email'], 1])

    if data[0][0] != 1:
        return APIFilException.raiseDBException(code=data[0][0])

    EmailManager.sendPasswordLink(link=data[0][1], email=request.form['email'])
    return APIFilSuccess.response(APIFilResponse.OK, data=[[1]])

@app.route('/getProcesosPasos', methods=["POST","GET"])
@login_admin_required
def getProcesosPasos():
    data = Database.callSP('getProcesosPasos', [], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/getDocumentos', methods=["POST","GET"])
@login_admin_required
def getDocumentos():
    data = Database.callSP('getDocumentos', [], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/getPasos', methods=["POST","GET"])
@login_admin_required
def getPasos():
    data = Database.callSP('getPasos', [request.form['id_proceso']], asDict=True)

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/logoutAdmin', methods=["POST","GET"])
def logout():
    data = Database.callSP('deleteTokenAdmin', [request.form['token']])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/getValidateEmailTokenAdmin', methods=["POST","GET"])
def getValidateEmailTokenAdmin():
    data = Database.callSP('getValidateEmailTokenAdmin', [request.form['token']])

    if data[0][0] != 1:
        return APIFilException.raiseDBException(code=data[0][0])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/restoreAdmin', methods=["POST","GET"])
def restoreAdmin():
    data = Database.callSP('getValidateEmailTokenAdmin', [request.form['token']])

    if data[0][0] != 1:
        return APIFilException.raiseDBException(code=data[0][0])
    else:
        data = Database.callSP('restoreAdmin', [data[0][2],request.form['password'],request.form['token']])

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/addDocument', methods=["POST","GET"])
@login_admin_required
def addDocument():
    data = Database.callSP('addDocument', [request.form['filename'],request.form['content']])
    return APIFilSuccess.response(APIFilResponse.OK, data=data)

@app.route('/deleteFiles', methods=["POST","GET"])
@login_admin_required
def deleteDocuments():
    files = json.loads(request.form['files'])
    print(files, file=sys.stdout)
    data = [[0]]
    for file in files:
        data = Database.callSP('deleteFile', [file['id']])

    if files[len(files)-1]['id'] == data[0][0]:
        data = [[1]]

    return APIFilSuccess.response(APIFilResponse.OK, data=data)

if __name__ == '__main__':
    app.run()
