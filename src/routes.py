from flask import render_template, url_for, flash, redirect, request
from src import app, db
from src.forms import LoginForm, FitbitUserForm
from src.models import User, FitbitUser
from flask_login import login_user, current_user, logout_user, login_required
import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd

@app.route("/")
@app.route("/home")
def home():
    fitbit_users = FitbitUser.query.all()
    # print(fitbit_users)
    return render_template('home.html', fitbit_users = fitbit_users)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        print('test1')
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/fitbituser/new", methods=['GET', 'POST'])
@login_required
def new_fitbituser():
    form = FitbitUserForm()
    if form.validate_on_submit():
        fitbituser = FitbitUser(
          username=form.username.data,
          client_id = form.client_id.data,
          client_secret_key = form.client_secret_key.data,
          access_token=form.access_token.data,
          refresh_token=form.refresh_token.data,
        )
        db.session.add(fitbituser)
        db.session.commit()
        flash('Your fitbit user has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_fitbituser.html', title='New Fitbit User', form=form, legend='New Fitbit User')

@app.route("/fitbituser/<int:fitbituser_id>/update", methods=['GET', 'POST'])
@login_required
def update_fitbituser(fitbituser_id):
    fitbituser = FitbitUser.query.get_or_404(fitbituser_id)
    form = FitbitUserForm()
    if form.validate_on_submit():
        fitbituser.username = form.username.data
        fitbituser.client_id = form.client_id.data
        fitbituser.client_secret_key = form.client_secret_key.data
        fitbituser.access_token = form.access_token.data
        fitbituser.refresh_token = form.refresh_token.data

        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.username.data = fitbituser.username
        form.client_id.data = fitbituser.client_id
        form.client_secret_key.data = fitbituser.client_secret_key
        form.access_token.data = fitbituser.access_token
        form.refresh_token.data = fitbituser.refresh_token
    return render_template('create_fitbituser.html', title='Update Fitbit User',
                           form=form, legend='Update Fitbit User')

@app.route("/fitbituser_page/<int:fitbituser_id>")
@login_required
def FitbitUserPage(fitbituser_id):
    fitbituser = FitbitUser.query.get_or_404(fitbituser_id)
    CLIENT_ID = fitbituser.client_id
    CLIENT_SECRET = fitbituser.client_secret_key
    ACCESS_TOKEN= fitbituser.access_token
    REFRESH_TOKEN= fitbituser.refresh_token
    auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN, expires_in=2592000)

    oneDate = pd.datetime(year = 2019, month = 5, day = 3)
    oneDayData = auth2_client.intraday_time_series('activities/heart',base_date=oneDate,detail_level='15min')
    print(type(oneDayData))
    # df = pd.DataFrame(oneDayData['activities-heart']['value'])
    # activity_heart_rate = oneDayData['activities-heart']['value']
    # print(type(activity_heart_rate))
    # fitbituser = df.values.tolist()

    return render_template('fitbit.html', fitbituser_data=oneDayData)

def init_fitbit():
    unauth_client = fitbit.Fitbit('<consumer_key>', '<consumer_secret>')
    # certain methods do not require user keys
    unauth_client.food_units()