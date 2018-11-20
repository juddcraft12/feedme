#!/usr/bin/python
import os
import sqlite3
import random

# conn = sqlite3.connect("test.db")

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):  
    conn = sqlite3.connect(db_path)
    return conn

print ("...Opened database successfully")

class Database(object):
    def __init__(self, count):
        self.count = count        

    def add(self):
        self.count += 1
        return self.count

    def getCount(self):
        return self.count

data = Database(3)
def incrementCounter():
    data.add()
    data.getCount()

def create_record_player(db_connect, player):
    print ("...Forming DB record")
    """
    Create a new player into the player table
    :param db_connect:
    :param player:
    :return: project id
    """
    sql = ''' INSERT INTO PLAYER(ID, NAME, HEALTH, ATTACK, DEFENCE)
        VALUES(?,?,?,?,?) '''
    cur = db_connect.cursor()
    cur.execute(sql, player)
    return cur.lastrowid

def insert_record_player(db_connect, id, name, health, attack, defence):
    print ("...Inserting DB record")
    player = (id, name, health, attack, defence)
    create_record_player(db_connect, player)
    print ("...Record add complete. Following record was added:")
    cur = db_connect.cursor()
    cur = db_connect.execute("SELECT * FROM PLAYER")
    for row in cur:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "HEALTH = ", row[2]
        print "ATTACK = ", row[3]
        print "DEFENCE = ", row[4], "\n"

incrementCounter()

# db_connect().execute('''CREATE TABLE PLAYER
#         (ID         INT     PRIMARY KEY     NOT NULL,
#          NAME       TEXT    NOT NULL,
#          HEALTH     INT     NOT NULL,
#          ATTACK     INT,
#          DEFENCE    INT);''')
# print ("Table created successfully")

insert_record_player(db_connect(), data.getCount(), "dummy", 1, 2, 3)

# player = (0, "dummy", 1, 2, 3)
# create_record_player(conn, player)

# conn.execute("INSERT INTO PLAYER (ID,NAME,HEALTH,ATTACK,DEFENCE) \
#     VALUES (1, 'Test', 10, 5, 10 )");

# conn.commit()
# print ("Records created successfully")

# cursor = db_connect.execute("SELECT id, name, health, attack, defence from PLAYER")
# for row in cursor:
#     print "ID = ", row[0]
#     print "NAME = ", row[1]
#     print "HEALTH = ", row[2]
#     print "ATTACK = ", row[3]
#     print "DEFENCE = ", row[4], "\n"

print ("Operation done successfully")

db_connect().close()