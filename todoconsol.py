import sqlite3
import os
import datetime
import consolcolor as color

def clear_cmd():
    os.system("clear")

def page():
    print("""\n\n\n
            ██    █   █    ██     ██   █    █
           █ █   █ █  █   █  █  █  █   ██   █
          ████   █  █ █    █    ████  █  █ █
         █   █   █  ██  █  █   █   █  █   ██
        █    █  █    █   ██   █    █  █    █

         ███   █      ██    ███     ███      █   █  █   ███  █   █  ███
        █  █   █     █ █    █  █   █         █  ██  █    █   ██  █  █  █
       ████   █     ████   █   █   ███       █ █ █  █   █   █  █ █  █  █
       █  █  █      █  █   █  █   █          ██   ██    █   █   █  █  █
      ████   ████  █   █  ████   ████        █    █   ███   █   █  ███
                                                                          """)

    input(color.C_CYAN + "\n\n\nPress Any Key to Continue...\n"+color.C_END)

def create_db():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    table_create_sql = """create table if not exists todo(
        id integer primary key autoincrement,
        what text not null,
        due text not null,
        category text not null,
        finished integer);"""

    cur.execute(table_create_sql)
    conn.close()

def help_msg():
    print("This is simple todo list program. \n \
 - To add data, press '1' and write your todo list. \n \
 - To view data, press '2'. \n \
 - To modify data, press '3'. \n \
 - To delete todo, press '4'. \n \
 - To quit, press '6'. \n \
Made by Hanyang Univ. ERICA AnsanBladeWind \n \
Contact Us: https://github.com/SonMinWoo/AnsanBladeWind \n\n")

def run_program():
    while 1:
        select = input("\nChoose what to do:\n(1: Add data, 2: List todo, 3: Modify todo, 4: Delete todo, 5: Help, 6: Quit) \n").strip()
        if select == '1':
            clear_cmd()
            print(" >> Add Todo")
            add_todo()
        elif select == '2':
            clear_cmd()
            print(" >> List Todo")
            listselect = input("What items are you looking at (1: All, 2: Finished, 3: Not Finished)? \n").strip()
            list_todo(listselect)
        elif select == '3':
            clear_cmd()
            print(" >> Modify Todo")
            modify_todo()
        elif select == '4':
            clear_cmd()
            print(" >> Delete Todo")
            delete_todo()
        elif select == '5':
            clear_cmd()
            print(" >> Help")
            help_msg()
        elif select == '6':
            clear_cmd()
            break

def list_todo(data):
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    rows = filter_todo(data)

    print("\n" + "╔══════╦═════════════════════╦════════════════╦════════════════╦═══════════╗")
    print("║ {}║ {}║ {}║ {}║ {}║" .format("id".center(5,' '),"To Do".center(20,' '),"Due".center(15,' '),"Category".center(15,' '),"finished?".center(10,' ')))
    print("╠══════╬═════════════════════╬════════════════╬════════════════╬═══════════╣")
    for row in rows:
        if(row[4] == 1):
            print("║ {}║ {}║ {}║ {}║ {}║" .format(str(row[0]).center(5,' '),row[1].center(20,' '),row[2].center(15,' '),row[3].center(15,' '),'O'.center(10,' ')))
        else:
            print("║ {}║ {}║ {}║ {}║ {}║" .format(str(row[0]).center(5,' '),row[1].center(20,' '),row[2].center(15,' '),row[3].center(15,' '),'X'.center(10,' ')))
    print("╚══════╩═════════════════════╩════════════════╩════════════════╩═══════════╝")

    conn.close()

def filter_todo(filter):
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    if(filter == '1'):
        cur.execute("select * from todo where 1")
        rows = cur.fetchall()
        conn.close()
        return rows
    elif(filter == '2'):
        cur.execute("select * from todo where finished = 1")
        rows = cur.fetchall()
        conn.close()
        return rows
    elif(filter == '3'):
        cur.execute("select * from todo where finished = 0")
        rows = cur.fetchall()
        conn.close()
        return rows


def add_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    what = input("Todo? \n")
    while(len(what) > 20):
        print("Maximum string number of contents is 20. Please reduce the number of letters\n ")
        what = input("Todo? \n")

    due = input("Due date? (YYYY-mm-dd) \n")
    while(1):
        try:
            valid_date = datetime.datetime.strptime(due, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date. Due must be 'YYYY-mm-dd' format. ")
            due = input("Due date? (YYYY-mm-dd) \n")

    category = input("Which category? \n")
    while(len(category) > 15):
        print("Maximum string number of contents is 15. Please reduce the number of letters\n ")
        category = input("Which category? \n")


    sql = "insert into todo (what, due, category, finished) values (?, ?, ?, ?)"
    cur.execute(sql, (what, due, category, 0))
    conn.commit()
    conn.close()

def modify_todo():
    list_todo('1')
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sel_id = input("Record id? \n")

    #항목별로 수정할 수 있도록 개선
    sel_item = input("Select item \n 1: Todo, 2: Due, 3: Category, 4: Finished \n")

    if(sel_item=='1'):
        sel_what = input("Todo? \n")
        while(len(sel_what) > 20):
            print("Maximum string number of contents is 20. Please reduce the number of letters\n ")
            sel_what = input("Todo? \n")
        cur.execute("update todo set what = ? where id = ?", (sel_what, sel_id))

    elif(sel_item=='2'):
        sel_due = input("Due date? (YYYY-mm-dd) \n")
        while(1):
            try:
                valid_date = datetime.datetime.strptime(sel_due, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date. Due must be 'YYYY-mm-dd' format. ")
                sel_due = input("Due date? (YYYY-mm-dd) \n")
        cur.execute("update todo set due = ? where id = ?", (sel_due, sel_id))

    elif(sel_item=='3'):
        sel_catagory = input("Which category? \n")
        while(len(sel_catagory) > 15):
            print("Maximum string number of contents is 15. Please reduce the number of letters\n ")
            sel_category = input("Which category? \n")
        cur.execute("update todo set category = ? where id = ?", (sel_catagory, sel_id))

    elif(sel_item=='4'):
        sel_fin = input("Finished (1: yes, 0: no)? \n")
        while(1):
            if(sel_fin == '1' or sel_fin == '0'):
                break
            print("Invalid value. Value must be 1 or 0\n")
            sel_fin = input("Finished (1: yes, 0: no)? \n")
        cur.execute("update todo set finished = ? where id = ?", (sel_fin, sel_id))

    conn.commit()
    conn.close()

def delete_todo():
    list_todo('1')
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sel_id = input("Record id? \n")

    cur.execute("delete from todo where id = ?", (sel_id,))
    conn.commit()
    conn.close()


clear_cmd()
page()
clear_cmd()

create_db()
run_program()
