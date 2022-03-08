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
            database   ="myapi-accounts"
            )

@app.teardown_request
def teardown_request(exception):
    g.cnx.close()
  

@app.route("/health")
def health():
    resp = Response('{ "message" : "Service running. Python version: ' + sys.version + '"}')
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route("/account", methods=['GET', 'POST', 'DELETE'])
def account():
    if request.method == 'GET':
        cursor = g.cnx.cursor()
        cursor.execute(f"SELECT ID, user, pass FROM accounts where user='{request.args['user']}'")
        results= []
        for (account_id, account_user, account_pass) in cursor:
            results.append({"id":account_id, "user":account_user, "pass":account_pass})
        response = app.response_class(
            response=json.dumps(results),
            status=200,
            mimetype='application/json'
            )
        return response
    if request.method == 'POST':
        cursor = g.cnx.cursor()
        cursor.execute(f"INSERT INTO accounts (user, pass) VALUES ('{request.args['user']}','{request.args['pass']}')")
        g.cnx.commit()
        response = app.response_class(
            response=json.dumps({"msg":f"Saved {request.args['user']}"}),
            status=200,
            mimetype='application/json'
            )
        return response
    if request.method == 'DELETE':
        cursor = g.cnx.cursor()
        cursor.execute(f"DELETE FROM accounts WHERE user = \"{request.args['user']}\"")
        g.cnx.commit()
        response = app.response_class(
            response=json.dumps({"msg":"Deleted", "count": f"{cursor.rowcount}"}),
            status=200,
            mimetype='application/json'
            )
        return response

@app.route("/login", methods=['GET'])
def login():
    if request.method == 'GET':
        cursor = g.cnx.cursor()
        qlogin=f"SELECT ID, user, pass FROM accounts where user='{request.args['user']}' AND pass='{request.args['pass']}'"
        cursor.execute(qlogin)
        rows = cursor.fetchall()
        if len(rows):
            response = app.response_class(
                response=json.dumps({"msg":f"Wellcome {request.args['user']}"}),
                status=200,
                mimetype='application/json'
                )
            return response
        else:
            response = app.response_class(
                response=json.dumps({"msg":f"Unauthorized rowcount:{len(rows)}"}),
                status=401,
                mimetype='application/json'
                )
            return response
