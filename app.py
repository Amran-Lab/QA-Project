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


@app.route('/',methods=['GET','POST'])
def home():
    
    
    
    cur = mysql.connection.cursor()
    #cur.execute("Insert into GameTable (game_name,genre,release_date) VALUES ('GTAT','action','20121005')")
    #mysql.connection.commit()
    cur.execute("SELECT * from GameTable")
    data = cur.fetchall()
    cur.execute("SELECT * from MovieTable")
    movie = cur.fetchall()
    cur.execute("select GreviewTable.review_id,GameTable.game_name,accountTable.first_name, game_review,accountTable.last_name from GameTable,GreviewTable,accountTable where user_id_1=user_id and game_id_1=game_id;")
    data1 = cur.fetchall()
    cur.execute("select MreviewTable.review_id,MovieTable.movie_name,accountTable.first_name, movie_review,accountTable.last_name from MovieTable,MreviewTable,accountTable where user_id_1=user_id and movie_id_1=movie_id;")
    MrevTable = cur.fetchall()
    cur.execute("SELECT * from accountTable")
    account = cur.fetchall()
    #st = data[8][0]
    #string = "delete from GameTable where game_id =" +str(st)
    #cur.execute(string)
    #mysql.connection.commit()
    #rows = cur.fetchall
    cur.close()
    
    data = data
    
    
    #return str(data1)
    return render_template('index.html', data = data,data1 = data1, account = account, movie = movie, MrevTable= MrevTable)
    

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/home/add/game",methods=['GET','POST'])
def add_game_record():
    details=request.form
    user_id_1=details['name']
    gameid=details['game']
    game_review=details['review']
    cur = mysql.connection.cursor()
    cur.execute("select * from GreviewTable where user_id_1=%s and game_id_1=%s",(user_id_1, gameid))
    records = cur.fetchall()
    if len(records)>0:
        cur.execute("UPDATE GreviewTable SET game_review= %s where user_id_1=%s and game_id_1=%s;",(game_review, user_id_1, gameid ))
            
    else:        
        cur.execute("INSERT INTO GreviewTable (user_id_1,game_id_1,game_review) VALUES (%s, %s, %s)", (user_id_1, gameid, game_review))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/home/sign_up",methods=['GET','POST'])
def sign_up():
    details=request.form
    fname1= details['fname']
    lname1= details['lname']  
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO accountTable (first_name,last_name) VALUES (%s, %s)", (fname1,lname1))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))


@app.route("/home/delete",methods=['GET','POST'])
def delete():
    details=request.form
    
    user_id_1= details['name'] 
    cur = mysql.connection.cursor()
    cur.execute("Delete from GreviewTable where user_id_1 = %s",[user_id_1])
    cur.execute("Delete from MreviewTable where user_id_1 = %s",[user_id_1])
    cur.execute("Delete from accountTable where user_id = %s",[user_id_1])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/home/delete/review",methods=['GET','POST'])
def delete_record():
    details=request.form
    user_id_1= details['name']
    game_id_1= details['game']
      
    cur = mysql.connection.cursor()
    cur.execute("Delete from GreviewTable where user_id_1 = %s and game_id_1 = %s",(user_id_1,game_id_1))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/home/add_movie_record",methods=['GET','POST'])
def add_movie_record():
        
        details=request.form
        user_id_1=details['name']
        movie_id_1=details['movie']
        movie_review=details['review']
        cur = mysql.connection.cursor()
        cur.execute("select * from MreviewTable where user_id_1=%s and movie_id_1=%s",(user_id_1, movie_id_1))
        records = cur.fetchall()
        if len(records)>0:
            cur.execute("UPDATE MreviewTable SET movie_review= %s where user_id_1=%s and movie_id_1=%s;",(movie_review, user_id_1, movie_id_1 ))
            
        else:

            cur.execute("INSERT INTO MreviewTable (user_id_1,movie_id_1,movie_review) VALUES (%s, %s, %s)", (user_id_1, movie_id_1, movie_review))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
@app.route("/home/delete/movie_review",methods=['GET','POST'])
def delete_movie_record():
    details=request.form
    user_id_1= details['name']
    movie_id_1= details['movie']
      
    cur = mysql.connection.cursor()
    cur.execute("Delete from MreviewTable where user_id_1 = %s and movie_id_1 = %s",(user_id_1,movie_id_1))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/home1/<id>",methods=['GET','POST'])

def delete_movie_recordby_id(id):
          
    cur = mysql.connection.cursor()
    id = id
    cur.execute("Delete from MreviewTable where review_id = %s",[int(id)])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))

@app.route("/home2/<id>",methods=['GET','POST'])
def delete_game_recordby_id(id):
    
    cur = mysql.connection.cursor()
    id = id
    cur.execute("Delete from GreviewTable where review_id = %s",[int(id)])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('home'))



if __name__== '__main__':
    app.run('0.0.0.0',debug = True)
    