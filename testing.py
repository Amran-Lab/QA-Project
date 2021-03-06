import urllib3
from flask import Flask,render_template,request,redirect, url_for
from flask_mysqldb import MySQL
import os 
app = Flask(__name__)
sqlhost = os.environ['SQLHOST']
sqlpass = os.environ['SQLPASS']
app.config['MYSQL_HOST'] = sqlhost
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = sqlpass
app.config['MYSQL_DB']= 'project1'

mysql = MySQL(app)
def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/')
    assert 200 == r.status
def test_about():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/about')
    assert 200 == r.status

def test_login():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://130.211.114.138:5000/login')
    assert 404 == r.status

def test_insert_db():
    with app.app_context():                                                      #need context for it to work
        cur = mysql.connection.cursor()
        cur.execute("Select * from MreviewTable")                                  #this and next command will get records before update
        records_before = cur.fetchall()
        cur.execute("INSERT INTO MreviewTable (user_id_1,movie_id_1,movie_review) VALUES ('5','1' , 'Test Review')")
        mysql.connection.commit()
        cur.execute("Select * from MreviewTable")                                           #this gets record after update
        records_after = cur.fetchall()          
        cur.close()
    recordb = len(records_before)                                                        #finds length of records before change
    new_id = records_before[recordb-1][0]+1                                                     #finds the id of the previous record and + 1 for autoincrement new rec
    recorda = len(records_after) 
    #assert (new_id,5,1,'Test Review') == records_after[recorda-1]                           #compares what should be there to most recent
    assert records_before[len(records_before)-1] != records_after[len(records_after)-1]

def test_delete_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("Select * from MreviewTable")                                  #this and next command will get records before update
        records_before = cur.fetchall()
        cur.execute("Delete from MreviewTable where review_id = %s",[int(records_before[len(records_before)-1][0])])
        mysql.connection.commit()
        cur.execute("Select * from MreviewTable")                                           #this gets record after update
        records_after = cur.fetchall()          
        cur.close()
    
    assert records_before[len(records_before)-1][0] != records_after[len(records_after)-1][0]