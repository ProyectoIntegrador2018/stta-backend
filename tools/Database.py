import datetime

import pymysql.cursors

#=======================================================================================================================
class Database:
    def datetime_handler(x):
            return x.__str__()

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def callSP(spName, spParameters=[], withColNames=False, asDict=False):
        try:
            connection = pymysql.connect(host="mysql-stte.cpmhc4vavlgx.us-east-2.rds.amazonaws.com",
                                         user="tramitestec",
                                         passwd="Ingser19&",
                                         db="STTEDB", charset='UTF8')
            # create a cursor
            cur = connection.cursor()
            # execute the stored procedure passing in
            # search_string as a parameter
            cur.callproc(spName, spParameters)
            # grab the results

            results = cur.fetchall()

            if withColNames:
                colNames = [[]]
                for colName in cur.description:
                    colNames[0].append(colName[0])

                for row in results:
                    colNames.append(row)

                cur.close()
                return colNames
            elif asDict:
                colNames = [[]]
                for colName in cur.description:
                    colNames[0].append(colName[0])

                di = []
                for row in results:
                    i = 0
                    die = dict()
                    for item in row:
                        die[colNames[0][i]] = item
                        i = i + 1
                    di.append(die)

                cur.close()
                return di
            else:
                cur.close()
                return results
        except pymysql.Error as e:
            return [['ERROR-DB', e.__str__()]]


    # ------------------------------------------------------------------------------------------------------------------

# ======================================================================================================================
