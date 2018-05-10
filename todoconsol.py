import sqlite3

def create_db():

    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    table_create_sql = """create table if not exists todo(
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        finished integer);"""

    cur.execute(table_create_sql)
    conn.close()

def run_program():
    while 1:
        select = input("Choose what to do:\n(a: add data, l : List todo, m: Modify todo, q: Quit)?")
        if select == 'a':
            add_todo()
        elif select == 'l':
            list_todo()
        elif select == 'm':
            modify_todo()
        elif select == 'q':
            break

def list_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    sql = "select * from todo where 1"
    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
      print(row[0], row[1], row[2], row[3])

    conn.close()

def add_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    what = input("Todo? ")
    due = input("Due date? ")
    sql = "insert into todo (what, due, finished) values (?, ?, ?)"
    cur.execute(sql, (what, due, 0,))
    conn.commit()
    conn.close()

def modify_todo():
    list_todo()
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    sel_id = input("Record id? ")
    sel_what = input("Todo? ")
    sel_due = input("Due date? ")
    sel_fin = input("Finished (1: yes, 0: no)? ")
    cur.execute("update todo set what = ?, due = ?, finished = ? where id = ?", (sel_what, sel_due, sel_fin, sel_id,))
    conn.commit()
    conn.close()

create_db()
run_program()
