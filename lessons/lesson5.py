### SQL ###


'''
----------------------------------------
| students                             |
----------------------------------------
| id PK AU | name TEXT | grade INTEGER |
----------------------------------------
| 1        | Alex      | 1             | 
| 2        | Dima      | 1             | 
    ...
'''

# import sqlite3



# conn = sqlite3.connect('db.sqlite')
# curs = conn.cursor()

# data = curs.execute('SELECT * FROM students').fetchall()

### C
# curs.execute('INSERT INTO students ("name","grade") VALUES ("Alex","2")')
# conn.commit()

### R
# data = curs.execute('SELECT * FROM students WHERE "id"="1"').fetchall()
# print(data)

### U
# curs.execute('UPDATE students SET "name"="Dima" WHERE "id"="1"')
# conn.commit()

### D
# curs.execute('DELETE FROM students WHERE "id"="1"')
# conn.commit()



'''
Napisat programmy po vedenijy zada4.
V ramkah programmy nuzno dat vozmost delat sledujushee:
    - prosmatrivat vse zada4i
    - dobavljat novuju zada4u
    - izmenjat status zada4i na "gotovo" ili obratnois
    - udalat ustarevshie zada4i

Kazdaja zada4a dolna bit zapisju v tablice DB, so sled. strukturoj:
    - id pk
    - title
    - description
    - status
(ispolzuj func. podhod)
'''
import sqlite3

conn = sqlite3.connect('./task.sqlite')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, status INTEGER)')



def view():
    temp = '|{:^7}|{:^20}|{:^20}|{:^10}|'
    print('-'*62)
    print(temp.format('id', 'title','desc','status'))
    print('-'*62)
    for row in curs.execute('SELECT * FROM tasks').fetchall():
        id = row[0]
        title = row[1]
        description = row[2]
        status = 'True' if row[3] else 'False'
        print(temp.format(id, title, description, status))
    print('-'*62)

def create():
    title = input('title: ')
    description = input('description: ')
    curs.execute(f'INSERT INTO tasks ("title", "description", "status") VALUES ("{title}", "{description}", "0")')
    conn.commit()
    print('task created')

def update_status():
    view()
    task_ids = curs.execute('SELECT id FROM tasks').fetchall() # [(1,),(2,),(3,)]
    choice = int(input('Which task do you want to change?\nid>>'))
    
    if (choice,) in task_ids: # 1 not in [(1,),(2,),(3,)]
        status = curs.execute(f'SELECT status FROM tasks WHERE id = {choice}').fetchone()
        newStatus = not bool(status[0])
        curs.execute(f'UPDATE tasks SET status = {newStatus} WHERE id = {choice}')
        conn.commit()

def delete():
    view()
    task_ids = curs.execute('SELECT id FROM tasks').fetchall() # [(1,),(2,),(3,)]
    choice = int(input('Which task do you want to delete?\nid>>'))

    if (choice,) in task_ids:
        curs.execute(f'DELETE FROM tasks WHERE id = {choice}')
        conn.commit()

def menu():
    choice = int(input(f'1: view task\n2: create task\n3: change status\n4: delete task\n>>>'))
    if choice == 1:
        view()
    elif choice == 2:
        create()
    elif choice == 3:
        update_status()
    elif choice == 4:
        delete()
    else:
        print('enter vaild choice')
    
    menu()

menu()