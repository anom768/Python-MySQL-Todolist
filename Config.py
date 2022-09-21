import mysql.connector

class Database() :

    @staticmethod
    def getConnection() :
        db = mysql.connector.connect(
            host = "localhost",
            username = "root",
            password = "",
            database = "py_todo")
        
        return db