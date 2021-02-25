#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        data = request.json
        if data:
            print(data)
            nm = data["nm"]
            addr = data["addr"]
            city = data["city"]
            pin = data["pin"]
        else:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                print(nm, addr, city, pin)
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)", (nm, addr, city, pin))
                con.commit()
                msg = "Record successfully added"
        except sql.OperationalError as err:
            try:
                con.rollback()
            except Exception:
                pass
            msg = f"error in insert operation: {err}"
        finally:
            con.close()
            return render_template("result.html", msg=msg)


def get_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return rows


@app.route('/list')
def list_students():
    rows = get_students()
    return render_template("list.html", rows=rows)


@app.route('/students')
def json_students():
    rows = get_students()
    data = []
    for row in rows:
        row_data = {}
        print(row)
        row_data["name"] = row["name"]
        row_data["addr"] = row["addr"]
        row_data["city"] = row["city"]
        row_data["pin"] = row["pin"]
        data.append(row_data)
    return jsonify(data)


if __name__ == '__main__':
    try:
        conn = sql.connect('database.db')
        print("Opened database successfully")

        conn.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print("Table created successfully")
        conn.close()
        app.run(debug=True)
    except Exception:
        print("App failed on boot")
