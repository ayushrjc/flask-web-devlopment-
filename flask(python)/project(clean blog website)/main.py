from flask_mail import Mail
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import smtplib
from email.message import EmailMessage


with open('config.json','r') as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)

# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = 'True',
#     # MAIL_USE_TLS = 'True',
#     MAIL_USER = params['gmail_user'],
#     MAIL_PW = params['gmail_pw']
# )
#
# mail = Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class contact(db.Model):
    '''
    sno,name,phone,msg,date,email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class posts(db.Model):
    '''
    sno,name,phone,msg,date,email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)

@app.route("/")
def default():
    post = posts.query.filter_by().all()
    return render_template("index.html",params = params,posts= post)

@app.route("/dashboard")
def dashboard():
    post = posts.query.filter_by().all()
    return render_template("login.html",params = params,posts= post)

@app.route("/index")
def index():
    post = posts.query.filter_by().all()
    return render_template("index.html", params=params, posts=post)

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post = posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html",params = params,post=post)

@app.route("/about")
def about():
    return render_template("about.html",params = params)


@app.route("/contact" , methods = ['GET', 'POST'])
def contacts():
    if(request.method == 'POST'):
        '''Add entry to the data base'''
        name = request.form.get('name')
        email= request.form.get('email')
        phone= request.form.get('phone')
        message= request.form.get('message')
        entry = contact(name=name, phone= phone, msg = message,date = datetime.now(), email = email)
        db.session.add(entry)
        db.session.commit()


        msg = EmailMessage()
        msg['subject'] = 'Reply from Inferno Website'
        msg['From'] = params['gmail_user']
        msg['To'] = email
        msg.set_content('Thanks for responding. we ll get back to you soon.')

        # message = "Thanks for responding"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        # MAKE SURE YOU WRITE EMAIL ID AND PASSWORD IN CONFIG.JSON FILE

        server.login(params['gmail_user'],params['gmail_pw'])
        # server.sendmail("techinfernoarc@gmail.com",email,message)
        server.send_message(msg)
        # mail.send_message('NEW MSG FROM MY BLOG' + " from "+ name,
        #                   sender = email,
        #                   recipients = [params['gmail_user']],
        #                   body = message + "\n" +phone,
        #                   )

    return render_template("contact.html",params = params)


app.run(debug = True)