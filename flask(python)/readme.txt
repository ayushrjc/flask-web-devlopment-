1. I can use either flask or django for server side scripting.(backend)
2. For front-end Im using bootstrap templetes.
3. In current project directory we create a python file to import flask and write program, one static folder(public by default) , and one templates folder(private) in which we create all html file.
4. Im using ** Jinja  templating ** for serfing python programming syntax( like for loops, conditions etc)
5. I use xampp and myphpadmin for backend for the project.
6. After installing xampp and running myphpadmin i created db and tables required.
7. I used Flask SQLAlchemy to connect db to website. ( pip install flask-sqlalchemy )
8. Go to - https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/ 
   for syntax.
9. ** Who to post request ** we use method = ['GET','POST'] in main.py
10. Syntax-  also install connector as it is required for python3 (pip install mysql-connector-python)

	from flask_sqlalchemy import SQLAlchemy
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/techinfernowebsite'
	db = SQLAlchemy(app)

11. then i created config.json file in templetes folder for local uri/ prod uri options. And we use :-
	with open('config.json','r') as c:
    params = json.load(c)["params"]
	local_server = True
	app = Flask(__name__)

	if (local_server):
    		app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
	else:
		app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
12. i can also use this for facebook, twitter and insta profile url to link with logos.

** In json file **
	{
	  "params":
	  {
	    "local_server": "True",
	    "local_uri": "mysql+mysqlconnector://root:@localhost/techinfernowebsite",
	    "prod_uri": "mysql+mysqlconnector://root:@localhost/techinfernowebsite",
	    "fb_url": "https://facebook.com/ayushrajchoudhary",
	    "insta_url": "https://instagram.com/ayush_rj_",
	    "gh_url": "https://github.com/ayushrajchoudhary"
	  }
	}

** In main.py file **
	return render_template("index.html",params = params)

** In layout.html file **
	<a href="{{params['gh_url']}}" target="_blank">