# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 16.sqlite.py
@Project            : Crawler_2022
@CreateTime         : 2022/1/23 23:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2022/1/23 23:39 
@Version            : 1.0
@Description        : B站IT私塾
"""
import sqlite3


def sqliteCreate():
    # open if exist or create database
    conn = sqlite3.connect('sqlite.db')
    print("open database successfully")

    # get the cursor
    c = conn.cursor()

    # create table with sql
    # drop table if exists company;
    # can only execute one statement at a time.
    sqlCreateTable = '''
            
            create table company
            (id integer primary key autoincrement,
            name text not null,
            age int not null,
            address char(50),
            salary real);
            
    '''
    c.execute(sqlCreateTable)
    conn.commit()
    conn.close()


def sqliteInsert():
    # open if exist or create database
    conn = sqlite3.connect('sqlite.db')
    print("open database successfully")

    # get the cursor
    c = conn.cursor()

    # can only execute one statement at a time.
    sqlInsert1 = '''
            insert into company(id, name, age, address, salary)
            values (1, 'Tom', 32, 'USA', 8000);

    '''
    sqlInsert2 = '''
                insert into company(id, name, age, address, salary)
                values (2, 'Jerry', 30, 'England', 7000);

        '''
    c.execute(sqlInsert1)
    c.execute(sqlInsert2)
    conn.commit()
    conn.close()


def sqliteQuery():
    # open if exist or create database
    conn = sqlite3.connect('sqlite.db')
    print("open database successfully")

    # get the cursor
    c = conn.cursor()

    # can only execute one statement at a time.
    sqlQuery = '''
            select id, name address, salary from company where 1 = 1;

    '''
    cursor = c.execute(sqlQuery)

    for row in cursor:
        print(row)
        print('name = ' + row[1])
    conn.close()


if __name__ == '__main__':
    sqliteCreate()
    sqliteInsert()
    sqliteQuery()
