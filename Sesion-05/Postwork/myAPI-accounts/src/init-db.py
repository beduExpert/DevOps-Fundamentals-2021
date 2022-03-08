import os
import mysql.connector as sql

if __name__ == '__main__':
    cnx = sql.connect(
            host       =os.environ['MYSQL_IP'],
            port       =os.environ['MYSQL_PORT'],
            user       =os.environ['MYSQL_USER'],
            password   =os.environ['MYSQL_PASSWORD'],
            )
    f = open('database_schema.sql', 'r')
    cur = cnx.cursor()
    cur.execute(f.read())
    cnx.close()
    f.close()
    print("Initialized the database.\n")
