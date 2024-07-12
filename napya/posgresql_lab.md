# postgreSQL with Python

### Lab Objective

**The objective of this lab is to learn ways to interact with postgreSQL using Python**. PostgreSQL is a sql database, therefore, if you have automated against a sql DB before, you'll find many similarities in the code. The most unique thing about connecting to a postgreSQL DB, is the python library that is used is typically `pyscopg2`

Psycopg2 is the most popular postgrSQL database adapter for Python. Check it out here: [https://pypi.org/project/psycopg2/](https://pypi.org/project/psycopg2/)

### Procedure

1. Start in your home directory

    `student@bchd:~$` `cd`

0. Create a space to work.

    `student@bchd:~$` `mkdir -p ~/mycode/postgres_db/`

0. Move into the new space.

    `student@bchd:~$` `cd ~/mycode/postgres_db/`

0. Install a postgreSQL instance locally using apt.

    `student@bchd:~/mycode/postgres_db$` `sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common -y`

0. Connect to postgreSQL 

    `student@bchd:~/mycode/postgres_db$` `sudo -i -u postgres`

0. Configure the instance with a new user. PostgreSQL will prompt you with several questions.

    `postgres@ubuntu` `createuser zach -P --interactive`
    - Enter password for new role: `qwerty` 
    - Enter it again: `qwerty`
    - Shall the new role be a superuser? (y/n) `n`
    - Shall the new role be allowed to create databases? (y/n) `y`
    - Shall the new role be allowed to create more new roles? (y/n) `y`
    
0. Create a new database manually

    `postgres@ubuntu` `createdb testpython`

0. You can interact with PostgreSQL using `psql`

    `postgres@ubuntu` `psql testpython`

0. Try issuing some commands. A full list of `psql` commands can be found here: [https://www.postgresql.org/docs/9.6/app-psql.html](https://www.postgresql.org/docs/9.6/app-psql.html)

    `\dd`

    `\dt`

0. Quit.

    `\q`

0. Type `exit`

0. Install the python library that lets us talk to the PostgreSQL instance, `psycopg2`

    `student@bchd:~/mycode/postgres_db$` `python3 -m pip install psycopg2`

0. Open Jupyter notebook in a new tab.

0. Within Jupyter notebook, navigate to the directory we just created at the CLI

0. Within the Launcher tab, click to **Notebook > Python3 (ipykernel)**

0. Rename your notebook `postgres01.ipynb`

0. Place the following in the first cell:

    ```python
    # python3 -m pip install psycopg2
    import psycopg2

    try:
        connect_str = "dbname='testpython' user='zach' host='localhost' " + \
                      "password='qwerty'"
        
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        
        # create a new table with a single column called "name"
        cursor.execute("""CREATE TABLE IF NOT EXISTS tutorials (name char(40));""")
        
        # run a SELECT statement - no data in there, but we can try it
        cursor.execute("""SELECT * from tutorials""")
        
        conn.commit() # <--- makes sure the change is shown in the database
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
        conn.close()
        
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)    
    ```
    **Shift** + **Enter**

0. Nothing is returned because nothing is in our database. Let's fix that.

0. Write the following in the next cell:

0. Create the following script

    ```python
    # update the following if your user and password for postgresql are different
    # than what is shown below
    user = "zach"
    passw = "qwerty"

    # f-string defines where to connect to
    connect_str = f"dbname='testpython' user='{user}' host='localhost' password='{passw}'"

    conn = psycopg2.connect(connect_str)
    print("Opened database successfully")
    ```
    **Shift** + **Enter**
    
0. In the third cell, copy and paste the following:

    ```python
    # create a cursor that we can issue commands through
    cursor = conn.cursor()

    # This is a sql based database so you'll notice many similarities
    # to working with sqlite
    cursor.execute('''CREATE TABLE IF NOT EXISTS COMPANY
     (ID INT PRIMARY KEY     NOT NULL,
     NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL,
     ADDRESS        CHAR(50),
     SALARY         REAL);''')
    print("Table created successfully")
    ```
    **Shift** + **Enter**
    
0. In the fourth cell, copy and paste the following. This code inserts data into our database.

    ```python
    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 ) ON CONFLICT DO NOTHING")

    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 ) ON CONFLICT DO NOTHING")

    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 ) ON CONFLICT DO NOTHING")

    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Pennsylvania ', 65000.00 ) ON CONFLICT DO NOTHING")

    conn.commit()
    print("Records created successfully")
    ```
    **Shift** + **Enter**
    
0. In the fifth cell, place the following. This code attempts to retrieve some data from our database.

    ```

    cursor.execute("SELECT * FROM COMPANY")

    selects = cursor.fetchall()

    #selects = cursor.execute("SELECT id, name, address, salary from COMPANY")
    for row in selects:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")

    print("Operation done successfully")
    conn.close()
    ```
    **Shift** + **Enter**
    
0. **CHALLENGE 01** - Create a cell that inserts a new entry into the database. You can make up the user, age, state, and salary.

0. *SOLUTION 01* - One possible solution is as follows:

    ```python
    # Place new data into the database
    
    # update the following if your user and password for postgresql are different
    # than what is shown below
    user = "zach"
    passw = "qwerty"

    # f-string defines where to connect to
    connect_str = f"dbname='testpython' user='{user}' host='localhost' password='{passw}'"

    conn = psycopg2.connect(connect_str)
    print("Opened database successfully")

    # create a cursor that we can issue commands through
    cursor = conn.cursor()

    # place our new data into the database
    cursor.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Larry', 99, 'Pennsylvania', 90000.00 ) ON CONFLICT DO NOTHING")

    # commit our work (this dissolves our cursor)
    conn.commit()

    # close the connection
    conn.close()
    ```

0. **CHALLENGE 02** - In a second cell, write some code to retrieve and display your new entry.

0. *SOLUTION 02* - One possible solution is as follows:

    ```python
    # update the following if your user and password for postgresql are different
    # than what is shown below
    user = "zach"
    passw = "qwerty"

    # f-string defines where to connect to
    connect_str = f"dbname='testpython' user='{user}' host='localhost' password='{passw}'"

    conn = psycopg2.connect(connect_str)
    print("Opened database successfully")

    # create a cursor we can work through
    cursor = conn.cursor()

    # select all records where ID is 5
    cursor.execute("SELECT * FROM COMPANY WHERE ID = '5'")


    new_entry = cursor.fetchall()
    print(new_entry)

    conn.close()
    ```

0. From time to time it's important to stop any old kernels that are running. When you're complete, select **Kernel > Shut Down All Kernels...**

0. Close the tab containing Jupyter notebook and return to tmux.

0. If you're tracking your code in an SCM, issue the following commands:
    - `cd ~/mycode`
    - `git add *`
    - `git commit -m "PostgreSQL"`
    - `git push origin`

<br><br><div align="center">


</div>
