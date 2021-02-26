# Lab 47 - Tracking Inventory with sqlite - Instructor Demo

That code that we just did in that lab was a little sub-par/crappy/NOT-EVEN-AN-API. Let's take what was there, and make it into something to be proud of.


There are lots of changes to make:

1. Also import jsonify from flask - This is so that we can transmit our data back as JSON --- LIKE A REAL API WOULD!!!

    ```python
    from flask import Flask, render_template, request, jsonify
    ```

0. The **addrec()** function is pretty pathetic. It only accepts form data. What if we want to pass JSON to it? Let's fix that as follows:

    ```python
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
    ```

0. **DEMO TIME** - Run the Server. Try the HTML form. Then show students how to pass JSON to our API from curl. Like this:

    `$` `curl -d '{"nm": "Chad", "addr": "overTHERE", "city": "Metropolis", "pin": 90210}' -X POST localhost:5000/addrec -H "Content-Type: application/json"`
    
2. Our student_list function is also just returning HTML. Let's take another look at that. We know that we will **want to** return JSON from our database as well, so let's create a "helper" function and update our **student_list** function to use it.

    ```python
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
    ```
    
0. Now that we have our helper function in place, let's make a new function with a new route that will let us return JSON of the student info from the DB.

    ```python
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
    ```
    
0. **DEMO TIME** - Now that we think we have the ability to return JSON data, let's verify that it works. START THE SERVER. Go to the **localhost:5000/students** path in **aux1** and see JSON get returned. Then in another TMUX pane do the following curl command:

    `$` `curl localhost:5000/students`
  
## Finished Code

Our finished project should look like this.

```python
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
```
