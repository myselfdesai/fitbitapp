# Flask Fitbit API App

This is a app is usefull for hospital / Doctor who can check his client fitbit data , written in Python.

#  How To Use?


## Application Clone

 1. First clone this project
 `git clone https://github.com/myselfdesai/fitbitapp.git`

 2.  Navigate to project directory  fitbitapp
 `cd fitbitapp`
 then install packages using pipenv
 `pipenv install`
 activate environment using
 `pipenv shell`
after successfull of this command you will see `(fitbitapp) yourpcusername:~/fitbitapp$`

## Configuration
Navigate to the `src` directory and rename **config.py.example** file to **config.py** and replace required values / keys details

## Application Setup
 1.  Navigate to project directory  fitbitapp
 `cd fitbitapp`
 then install packages using pipenv
 `pipenv install`
 activate environment using
 `pipenv shell`
 after successfull of this command you will see `(fitbitapp) yourpcusername:~/fitbitapp$`

 2. Navigate to the root of the repository and run:
`cd src `

3. As we are currently using sqlite3 DB
	 in order to create db,  follow below steps
	 make sure you are in src directory
	 run `python`
	 then python shell appears
	 `>>> from src import db`
	 `>>> from src.models import FitbitUser, User`
	 `>>> db.create_all()`
	 you can check the sqlite file is created mentioned location in config.py file for me it was site.db
	 Now create admin user to login for website
	 `>>> user_1 = User(email='admin@xxx.com',password='1BDxxx3C')`
	 `>>> db.session.add(user_1)`
	 `>>> db.session.commit()`
	 exit python shell  Use exit() or Ctrl-D
4. Now run the application
	`python run.py`
