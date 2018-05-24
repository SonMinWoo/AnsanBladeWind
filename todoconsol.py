import sqlite3
import os

def clear_cmd():
        os.system("clear")

def page():

    print("""  __       __            __    """)
    print(""" /  |  _  /  |          /  |   """)
    print(""" $$ | / \ $$ |  ______  $$ |  _______   ______   _____  ____    ______  """)
    print(""" $$ |/$  \$$ | /      / $$ | /       | /      \ /     \/    \  /      \ """)
    print(""" $$ /$$$  $$ |/$$$$$$  |$$ |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |""")
    print(""" $$ $$/$$ $$ |$$    $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$    $$ |""")
    print(""" $$$$/  $$$$ |$$$$$$$$/ $$ |$$ |_____ $$ |__$$ |$$ | $$ | $$ |$$$$$$$$/ """)
    print(""" $$$/    $$$ |$$       |$$ |$$       |$$    $$/ $$ | $$ | $$ |$$       |""")
    print(""" $$/      $$/  $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/ """)

    while(1):
        key = input('\npress enter to continue')
        if key == '\n':
            break

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

def help_msg():
    print("This is simple todo list program. \n \
To add data, press 'a' and write your todo list. \n \
To view data, press 'l'. \n \
To modify data, press 'm'. \n \
To qhit, press 'q'. \n \
Made by Hanyang Univ. ERICA AnsanBladeWind \n")

def run_program():
    print("HELLO THIS IS TODO PROG BY ANSANBLADEWIND")
    #insert ascii art
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

    print("\n" + "="*59)
    print("| {}| {}| {}| {}|" .format("id".center(5,' '),"To Do".center(20,' '),"Due".center(15,' '),"finished?".center(10,' ')))
    print("|"+"-"*57+"|")
    for row in rows:
        if(row[3] == 1):
            print("| {}| {}| {}| {}|" .format(str(row[0]).center(5,' '),row[1].center(20,' '),row[2].center(15,' '),'O'.center(10,' ')))
        else:
            print("| {}| {}| {}| {}|" .format(str(row[0]).center(5,' '),row[1].center(20,' '),row[2].center(15,' '),'X'.center(10,' ')))
    print("="*59+"\n")

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


page()
clear_cmd()
create_db()
run_program()
