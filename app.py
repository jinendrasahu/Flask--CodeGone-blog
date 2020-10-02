from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
import os
import math

import json


local_server=True
with open('config.json','r') as c:
  params=json.load(c)["params"]

app = Flask(__name__)
app.secret_key='super-secret-key-bro'
app.config["UPLOAD_FOLDER"]=params["upload_folder"]
app.config.update(
  Mail_SERVER='smtp.gmail.com',
  MAIL_PORT='465',
  MAIL_USE_SSL=True,
  MAIL_USERNAME=params['gmail-user'],
  MAIL_PASSWORD=params['gmail-password']
)
mail=Mail(app)
if(local_server):
  app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
  app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
  '''
  sno,name,phone,msg,date,email
  '''
  sno=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(50),nullable=False)
  phone=db.Column(db.String(50),nullable=False)
  msg=db.Column(db.String(50),nullable=False)
  date=db.Column(db.String(50),nullable=False)
  email=db.Column(db.String(50),nullable=False)

class Posts(db.Model):
  sno=db.Column(db.Integer,primary_key=True)
  title=db.Column(db.String(50),nullable=False)
  tagline=db.Column(db.String(50),nullable=False)
  slug=db.Column(db.String(50),nullable=False)
  content=db.Column(db.String(120),nullable=False)
  img=db.Column(db.String(50),nullable=True)
  date=db.Column(db.String(50),nullable=True)

@app.route("/")
def home():
  posts=Posts.query.filter_by().all()#[0:params['no_of_posts']]
  last=math.ceil(len(posts)/int(params['no_of_posts']))
  page=request.args.get('page')
  if(not str(page).isnumeric()):
    page=1
  page=int(page)
  posts=posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+int(params['no_of_posts'])]
  if(page==1):
    prev="#"
    next="/?page="+str(page+1)
  elif(page==last):
    prev="/?page="+str(page-1)
    next="#"
  else:
    prev="/?page="+str(page-1)
    next="/?page="+str(page+1)
  return render_template('home.html',posts=posts,prev=prev,next=next)

@app.route("/about") 
def about():
  return render_template('about.html')

@app.route("/logout") 
def logout():
  session.pop("user")
  return redirect('/dashboard')

  

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
  posts=Posts.query.filter_by().all()
  if("user" in session and session["user"]==params["user"]):
    return render_template('dashboard.html',posts=posts)
  if(request.method=="POST"):
    username=request.form.get('email')
    userpass=request.form.get('pass')
    if(username==params["user"] and userpass==params["password"]):
      session["user"]=username
      return render_template('dashboard.html',posts=posts)
    else:
      return render_template('login.html')
  else:
    return render_template('login.html')

@app.route("/uploaded",methods=["GET","POST"]) 
def uploaded():
  if("user" in session and session["user"]==params["user"]):
    if(request.method=="POST"):
      f=request.files["file1"]
      f.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(f.filename)))
      return "Uploaded Successfully"

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
  post=Posts.query.filter_by(slug=post_slug).first()
  return render_template('post.html',post=post)

@app.route("/delete/<string:sno>",methods=['GET'])
def delete(sno):
  if("user" in session and session["user"]==params["user"]):
     post=Posts.query.filter_by(sno=sno).first()
     db.session.delete(post)
     db.session.commit()
     return redirect('/dashboard')

@app.route("/edit/<string:sno>",methods=['GET','POST'])
def edit(sno):
  post=Posts.query.filter_by(sno=sno).first()
  if("user" in session and session["user"]==params["user"]):
    if(request.method=="POST"):
      title=request.form.get("title")
      tagline=request.form.get("tagline")
      content=request.form.get("content")
      slug=request.form.get("slug")
      img=request.form.get("img")
      date=datetime.now()
      if(sno=='0'):
        entry=Posts(title=title,tagline=tagline,slug=slug,content=content,img=img,date=date)
        db.session.add(entry)
        db.session.commit()
        #return render_template('edit.html',post=post,sno=sno)
      else:
        post=Posts.query.filter_by(sno=sno).first()
        post.title=title
        post.tagline=tagline
        post.content=content
        post.slug=slug
        post.img=img
        post.date=date
        db.session.commit()
        return redirect('/edit/'+sno)
  post=Posts.query.filter_by(sno=sno).first()
  return render_template('edit.html',post=post,sno=sno)

@app.route("/contact",methods=["GET","POST"])
def contact():
  if(request.method=="POST"):
    '''Add entries to database'''
    name=request.form.get('name')
    email=request.form.get('email')
    num=request.form.get('phone')               
    message=request.form.get('msg')
    entry=Contacts(name=name,phone=num,msg=message,date=datetime.now(),email=email)
    db.session.add(entry)
    db.session.commit()
    # mail.send_message('New message from '+name,
    # sender=email,recipients=[params['gmail-user']],
    # body=message+'\n'+phone)
  return render_template('contact.html')

if __name__ == "__main__":
  app.run(debug=True)


#   @app.route("/")
# def hello():
#   myname="Jinendra"
#   return render_template('index.html',name=myname)

# @app.route("/jinu")
# def jinu():
#   return "Jinendra sahu bro!"

# if __name__ == "__main__":
#   app.run(debug=True)