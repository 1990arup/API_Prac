from flask import Flask, request,jsonify
import mysql.connector as conn
import pymongo as mdb
import pandas as pd

app=Flask(__name__)
mydb =conn.connect(host="localhost",user="root",passwd="Swaroop@1990")
cursor=mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.mysqltable (name varchar(30), number int)")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.mysqltable  values(%s , %s)",(name ,number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

@app.route('/update',methods=['POST'])
def update():
    if request.method == 'POST':
        get_name=request.json['get_name']
        cursor.execute("update taskdb.mysqltable set number=number+500 where name = %s",(get_name,))
        mydb.commit()
        return jsonify(str('Updated successfully'))

if __name__=='__main__':
    app.run()