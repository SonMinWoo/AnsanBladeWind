import sqlite3
import os

def clear_cmd():
        os.system("clear")


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

    print("\n=========================================================")
    print("| {}| {}| {}| {}|" .format("id".center(12,' '),"To Do".center(12,' '),"Due".center(12,' '),"finished?".center(12,' ')))
    print("|-------------------------------------------------------|")
    for row in rows:
        if(row[3] == 1):
            print("| {}| {}| {}| {}|" .format(str(row[0]).center(12,' '),row[1].center(12,' '),row[2].center(12,' '),'O'.center(12,' ')))
        else:
            print("| {}| {}| {}| {}|" .format(str(row[0]).center(12,' '),row[1].center(12,' '),row[2].center(12,' '),'X'.center(12,' ')))
    print("=========================================================\n")

    conn.close()

def add_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    what = input("Todo? ")
    while(len(what) > 12):
        print("Maximum string number of contents is 12. Please reduce the number of letters\n ")
        what = input("Todo? ")

    due = input("Due date? ")
    while(len(due) > 12):
        print("Maximum string number of contents is 12. Please reduce the number of letters\n ")
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
    while(len(sel_what) > 12):
        print("Maximum string number of contents is 12. Please reduce the number of letters\n ")
        sel_what = input("Todo? ")

    sel_due = input("Due date? ")
    while(len(sel_due) > 12):
        print("Maximum string number of contents is 12. Please reduce the number of letters\n ")
        sel_due = input("Due date? ")

    sel_fin = input("Finished (1: yes, 0: no)? ")
    while(1):
        if(sel_fin == '1' or sel_fin == '0'):
            break
        print("Invalid value. Value must be 1 or 0\n")
        sel_fin = input("Finished (1: yes, 0: no)? ")

    cur.execute("update todo set what = ?, due = ?, finished = ? where id = ?", (sel_what, sel_due, sel_fin, sel_id,))
    conn.commit()
    conn.close()

clear_cmd()
create_db()
run_program()
