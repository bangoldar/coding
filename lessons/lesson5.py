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