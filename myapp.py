
from flask import Flask,render_template,request,redirect,url_for
import pymysql

#creating flask obj

app=Flask(__name__)

#defining route

@app.route('/home')

def abc():
     return render_template('form.html')
     
#insert

@app.route('/insert',methods=['GET','POST'])

def insert():

   if request.method=='POST':
       
     n=request.form['na']
     m=request.form['mob']
     ip=request.form['id']
     a=request.form['amt']
    
     
     
     servername="localhost"
     username="root"
     password=""
     dbname="transport"
       
     try:
         
        db=pymysql.connect(servername,username,password,dbname)
        c=db.cursor()
        query="insert into booking(name,mobile,idproof,amount)values('{}','{}','{}','{}')".format(n,m,ip,a)
         
        c.execute(query)
        db.commit()
        
        return redirect(url_for('dashboard'))
          
     except Exception():

        db.rollback()
        return "failed to connect"
        
@app.route('/dashboard')

def dashboard():
    
     servername="localhost"
     username="root"
     password=""
     dbname="transport"
     try: 
       db=pymysql.connect(servername,username,password,dbname)
       c=db.cursor()
       query="select * from booking"
       c.execute(query)
       
       data=c.fetchall()
       
       return render_template('dashboard.html',row=data)#here to create dashboard file 
       return success
       
     
     except exception:
       return "filed to connect"

@app.route('/delete/<rid>')#use to bind id  to url

def delete(rid):

      
     servername="localhost"
     username="root"
     password=""
     dbname="transport"
     
     try:
       db=pymysql.connect(servername,username,password,dbname)
       c=db.cursor()
       query="delete from booking where id={}".format(rid)
       c.execute(query)
       db.commit()
       return redirect(url_for('dashboard'))
       
       
     except Exception:
       db.rollback()
    
       return"Failed"
       

@app.route('/edit/<rid>')

def edit(rid):

     servername="localhost"
     username="root"
     password=""
     dbname="transport"
      
     try:
       db=pymysql.connect(servername,username,password,dbname)
       c=db.cursor()
       query="select* from booking where id={}".format(rid)
       c.execute(query)
       data=c.fetchone()
       return render_template('editform.html',row=data)
       
     except Exception:
       db.rollback()
       return"Failed"
       
@app.route('/edit/update',methods=['POST','GET'])

def update():
  
  if request.method=="POST":
       
     n=request.form['na']
     m=request.form['mob']
     i=request.form['ip']
     a=request.form['amt']
     rno=request.form['id']
     
     servername="localhost"
     username="root"
     password=""
     dbname="transport"
      
     try:
       db=pymysql.connect(servername,username,password,dbname)
       c=db.cursor()
       query="update booking set name='{}',mobile='{}',idproof='{}',amount='{}'where id='{}'".format(n,m,i,a,rno)
       c.execute(query)
       db.commit()
       return redirect(url_for('dashboard'))
       
      
     except Exception:
       db.rollback()
       return"Failed"
     
    
     
 
      
     
         
    
         

     
app.run()     
