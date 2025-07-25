import mysql.connector as sql
from tabulate import tabulate 
def ADD():
    x = input('Are u new to this database [y/n] = ')
    if x.lower() == 'y':
        p = input('ENTER YOUR MYSQL PASSWORD = ')
        u = input('ENTER YOUR MYSQL USERNAME = ')
        mycon = sql.connect(host='localhost',
                     password=p,
                     user = u)
        mycur = mycon.cursor()
        qq = 'create database if not exists cs_project_new'
        mycur.execute(qq)
        aa = 'use cs_project_new'
        mycur.execute(aa)
        c = 'create table if not exists game(GAMEID varchar(10) primary key,\
        GAMENAME varchar(50) not null,GENRE varchar(10) not null,SIZEOFGAME varchar(10) not null,PRICE decimal default 0)'
        mycur.execute(c)
        print('---------------------successfully created the table and database!!------------------')
        #--------------above code is only when database and table not exist then it will create automatically---------
    elif x.lower() == 'n':
        try:
            try:
                con = sql.connect(host='localhost',
                                user = 'root',
                                password='root',
                                database='cs_project_new')
                cur = con.cursor()
                cur.execute('select GAMEID from game')
                print('existing game IDs--->',cur.fetchall())
                gi = input('ENTER GAME-ID [DISTINCT FROM ABOVE] = ')
                gn = input('ENTER GAME-NAME = ')
                g = input('ENTER GENRE OF GAME  = ')
                s = input('ENTER SIZE OF GAME WITH MENTION [GB/MB] = ')
                p = float(input('ENTER PRICE OF GAME [IF NOT ENTERED DEFAULT = 0] = '))
            except ValueError:
                gi = 'g0'
            
                p=0
            if len(gn) == 0:
                gn = 'null'
            if len(g) == 0:
                g = 'null'
            if len(s) == 0:
                s = 'null'
            q = 'insert into game values("{}","{}","{}","{}",{})'.format(gi.upper(),gn.upper(),g.upper(),s.upper(),p)
            cur.execute(q)
            con.commit()
            con.close()
            print('------------------------GAME_RECORD ADDED SUCCESSFULLY!!!--------------------------------------')
            print('\n')
        except:
            print('---------------THERE IS SOMRTHING WENT WRONG!!!!!!-----------------------------------')

def UPDATE():
    con = sql.connect(host='localhost',
                   user = 'root',
                   password='root',
                   database='cs_project_new')
    cur = con.cursor()
    cur.execute('select * from game')
    data = cur.fetchall()
    print(tabulate(data,headers=['GAME-ID','GAME-NAME','GENRE','SIZE-OF-GAME','PRICE'],tablefmt='fancy_grid'))
    print('''
    \t\t\tPRESS 1 TO UPDATE GAME PRICE
    \t\t\tPRESS 2 TO UPDATE GAME SIZE''')
    try:
        c = int(input('Enter choice from above = '))
        if c == 1:
            gi = input('enter GAME-ID to be update = ')
            gp = float(input('enter your new game price = '))
            q = 'update game set price = {} where gameid = "{}"'.format(gp,gi)
            cur.execute(q)
            con.commit()
            con.close()
            print('-------------------------RECORD UPDATED SUCCESSFULLY!!!----------------------------------')

        elif c == 2:
            gi = input('enter GAME-ID to be update = ')
            gs = input('enter new game size = ')
            a = 'update game set sizeofgame = "{}" where gameid = "{}"'.format(gs.upper(),gi)
            cur.execute(a)
            con.commit()
            con.close()
            print('--------------------------RECORD UPDATED SUCCESSFULLY!!!-----------------------------------')
        elif c>2:
            print('------------------------NO OPTION EXISTS-----------------------------------------')
    except ValueError:
        print('WRONG INPUT')

def DELETE():
    con = sql.connect(host='localhost',
                   user = 'root',
                   password='root',
                   database='cs_project_new')
    cur = con.cursor()
    cur.execute('select * from game')
    data = cur.fetchall()
    print(tabulate(data,headers=['GAME-ID','GAME-NAME','GENRE','SIZE-OF-GAME','PRICE'],tablefmt='fancy_grid'))
    gi = input('Enter GameID to be deleted = ')
    n = input('Are u sure to delete [y/n]: ')
    if n.lower() == 'y':
        q = 'delete from game where gameid = "{}"'.format(gi)
        cur.execute(q)
        con.commit()
        con.close()
        print('--------------------RECORD DELETED SUCCESSFULLY!!!!-------------------')
    elif n.lower() == 'n':
        pass

def SHOW():
    con = sql.connect(host='localhost',
                   user = 'root',
                   password='root',
                   database='cs_project_new')
    cur = con.cursor()
    cur.execute('select * from game')
    data = cur.fetchall()
    print(tabulate(data,headers=['GAME-ID','GAME-NAME','GENRE','SIZE-OF-GAME','PRICE'],tablefmt='fancy_grid'))
    con.close()

def SEARCH():
    con = sql.connect(host='localhost',
                   user = 'root',
                   password='root',
                   database='cs_project_new')
    cur = con.cursor()
    print('''
    \t\t\tpress 1 to search on the basis of price less than or equals to
    \t\t\tpress 2 to search on the basis of genre''')
    c = int(input('ENTER YOUR PREFRENCE = '))
    try:
        if c == 1:
            n = int(input('enter price under which u search = '))
            q = 'select * from game where price<={}'.format(n)
            cur.execute(q)
            data = cur.fetchall()
            if len(data)!=0:
                print(tabulate(data,headers=['GAME-ID','GAME-NAME','GENRE','SIZE-OF-GAME','PRICE'],tablefmt='fancy_grid'))
                con.close()
            else:
                print('*************SORRY GAME PRICE FILTER NOT AVAILABLE**************')
    except:
        pass
    try:
        if c == 2:
            n = input('enter genre to be search = ')
            q = 'select * from game where genre = "{}"'.format(n)
            cur.execute(q)
            data = cur.fetchall()
            if len(data)!=0:
                print(tabulate(data,headers=['GAME-ID','GAME-NAME','GENRE','SIZE-OF-GAME','PRICE'],tablefmt='fancy_grid'))
                con.close()
            else:
                print('************SORRY GENRE IS NOT YET AVAILABLE****************************')
    except:
        pass
#**************************************************MAIN MENU*********************************************************
print(40*'-','WELCOME TO THE WORLD OF GAMING',40*'-')
try:
    while True:
        print('''
       \t\t\t 1. TO ADD A GAME RECORD
       \t\t\t 2. TO UPDATE GAME RECORD
       \t\t\t 3. TO DELETE A GAME RECORD
       \t\t\t 4. TO DISPLAY THE TABLE
       \t\t\t 5. TO SEARCH IN TABLE 
       \t\t\t 6. EXIT''')
        print('\n')
        c = int(input('Enter Above Choices = '))
        if c == 1:
            ADD()
        elif c == 2:
            UPDATE()
        elif c == 3:
            DELETE()
        elif c == 4:
            SHOW()
        elif c == 5:
            SEARCH()
        elif c>6:
            print('WRONG CHOICE')
            break
        elif c == 6:
            break
        print(100*'*')
        print('\n')
    print('----------------------------THANK YOU HAVE A NICE DAY!!!!-------------------------------------------')
except ValueError:
    print('----------------------------SORRY WRONG VALUE INSERTED !!!!----------------------------------------------')