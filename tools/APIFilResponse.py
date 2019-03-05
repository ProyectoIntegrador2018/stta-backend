import decimal
import json

# ======================================================================================================================

import status as status


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

class APIFilResponse:

    # ------------------------------------------------------------------------------------------------------------------
    responseKey = "resp"
    dbKey = "dbCode"
    msgKey = "detail"
    httpStatusKey = "httpStatus"
    dataKey = "data"

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    OK = {responseKey : 1, msgKey : "Success", dataKey: None }

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    MISSING_ARGUMENTS = {responseKey : -1, msgKey : "Missing arguments"}
    USER_NOT_EXIST = {responseKey : -2, msgKey : "User not exist"}
    INVALID_USER = {responseKey : -3, msgKey : "Invalid user"}
    UNAUTHORIZED_USER = {responseKey : -4, msgKey : "Invalid user"}
    INVALID_OPERATION = {responseKey : -5, msgKey : "Invalid operation"}
    DB_NOT_DEFINED_ERROR = {responseKey : -6, msgKey : "Data base code not defined."}
    DB_CALL_SP_ERROR = {responseKey: -7, msgKey: "SP call error."}
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #                                                       # Non-modificable status. This status is handled by the
    #                                                       # framework.
    #                                                       # file: authentication.py( line 193)
    #                                                       # method: method authenticate_credentials
    SESSION_EXPIRED = {responseKey: -90, msgKey: "---Expired session---"}
    INVALID_TOKEN = {responseKey: -91, msgKey: "---Invalid token---"}
    AUTH_FAILED = {responseKey: -99, msgKey: "---Authentication failed default response---"}

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    DB_EXCEPTION = {
        "-90":  {responseKey: -90, msgKey: "---Expired session---"},
        "-91": {responseKey: -91, msgKey: "---Invalid token---"},
        "-101": {responseKey: -101, msgKey: "Tipo de usuario incorrecto"},
        "-102": {responseKey: -102, msgKey: "El email no esta registrado"},
        "-103": {responseKey: -103, msgKey: "Contraseña incorrecta "},
        "-104": {responseKey: -104, msgKey: "La matricula ya esta registrada."},
        "-105": {responseKey: -105, msgKey: "El email ya esta registrado."},
        "-106": {responseKey: -106, msgKey: "Documento enviado previamente."},
        "-998": {responseKey: -998, msgKey: "DB failed connection."},
        "-999": {responseKey: -999, msgKey: "ROLLBACK DETECTED"}
    }

    # ------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
class APIFilException:

    @staticmethod
    def raiseAPIException(apiResponse, msg=None):
        apiResponse = apiResponse.copy()
        if msg is not None:
            apiResponse[APIFilResponse.msgKey] = msg

        return json.dumps(apiResponse)

    @staticmethod
    def raiseDBException(code, msg=None):
        apiResponse = APIFilResponse.DB_EXCEPTION.get(str(code), None)
        if apiResponse is not None:
            apiResponse = apiResponse.copy()
            if msg is not None:
                apiResponse[APIFilResponse.msgKey] = msg
        else:
            apiResponse = APIFilResponse.DB_NOT_DEFINED_ERROR.copy()
            apiResponse[APIFilResponse.msgKey] = apiResponse[APIFilResponse.msgKey]  + " [CODE " + str(code) + "] "

        return json.dumps(apiResponse)

# ======================================================================================================================
class APIFilSuccess:

    @staticmethod
    def response(apiResponse, msg=None, data=None):
        apiResponse = apiResponse.copy()

        if msg is not None:
            apiResponse[APIFilResponse.msgKey] = msg

        if data is not None:
            apiResponse[APIFilResponse.dataKey] = data

        return  json.dumps(apiResponse , cls=DecimalEncoder, default=APIFilSuccess.datetime_handler)

    def datetime_handler(x):
            return x.__str__()


# ======================================================================================================================