from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route('/station/1')
def img_1():
    return render_template('tempted.html')


@app.route('/station/2')
def img_2():
    return render_template('betrayed.html')


@app.route('/station/3')
def img_3():
    return render_template('condemned.html')


@app.route('/station/4')
def img_4():
    return render_template('mocked.html')


@app.route('/station/5')
def img_5():
    return render_template('given_cross.html')


@app.route('/station/6')
def img_6():
    return render_template('falls.html')


@app.route('/station/7')
def img_7():
    return render_template('simon_carries.html')


@app.route('/station/8')
def img_8():
    return render_template('stripped.html')


@app.route('/station/9')
def img_9():
    return render_template('nailed.html')


@app.route('/station/10')
def img_10():
    return render_template('dies.html')


@app.route('/station/11')
def img_11():
    return render_template('buried.html')


@app.route('/station/12')
def img_12():
    return render_template('rises.html')


@app.route('/invite')
def invite():
    return render_template('invite.html')
