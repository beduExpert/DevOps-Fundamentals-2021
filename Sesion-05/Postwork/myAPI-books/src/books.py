import os
from flask import Flask
from flask import Response, request, g
import mysql.connector as sql
import sys
import json

app = Flask(__name__)


@app.before_request
def before_request():
    g.cnx = sql.connect(
            host       =os.environ['MYSQL_IP'],
            port       =os.environ['MYSQL_PORT'],
            user       =os.environ['MYSQL_USER'],
            password   =os.environ['MYSQL_PASSWORD'],
            database   ="myapi-books"
            )

@app.teardown_request
def teardown_request(exception):
    g.cnx.close()
  

@app.route("/health")
def health():
    resp = Response('{ "message" : "Service running. Python version: ' + sys.version + '"}')
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route("/book", methods=['GET', 'POST', 'DELETE'])
def book():
    if request.method == 'GET':
        cursor = g.cnx.cursor()
        cursor.execute(f"SELECT ID, ISBN, Title FROM books where ISBN={request.args['isbn']}")
        results= []
        for (book_id, book_isdn, book_title) in cursor:
            results.append({"id":book_id, "isdn":book_isdn, "title": book_title})
        response = app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
            )
        return response
    if request.method == 'POST':
        cursor = g.cnx.cursor()
        cursor.execute(f"INSERT INTO books (isbn, title) VALUES ('{request.args['isbn']}','{request.args['title']}')")
        g.cnx.commit()
        response = app.response_class(
            response=json.dumps({"msg":f"Saved {request.args['isbn']}"}),
            status=200,
            mimetype='application/json'
            )
        return response
    if request.method == 'DELETE':
        cursor = g.cnx.cursor()
        cursor.execute(f"DELETE FROM books WHERE isbn = \"{request.args['isbn']}\"")
        g.cnx.commit()
        response = app.response_class(
            response=json.dumps({"msg":"Deleted", "count": f"{cursor.rowcount}"}),
            status=200,
            mimetype='application/json'
            )
        return response