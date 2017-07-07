from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from models.users.user import User

app = Flask(__name__)
app.secret_key = 'supersecret'


app.users = {}
app.bucketlist = {}
app.activity = {}


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        if email not in app.users or password != app.users[email].password:
            error = 'Invalid credentials, please try again.'
        else:
            session['logged_in'] = True
            session['email'] = email
            flash('You are logged in')
            return redirect(url_for('bucketlist'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['inputName'].lower()
        email = request.form['inputEmail'].lower()
        password = request.form['inputPassword'].lower()
        passwordAgain = request.form['inputPasswordAgain'].lower()

        if password == passwordAgain:
            app.users[email] = User(name, email, password)
            session['logged_in'] = True
            session['email'] = email
            flash('You are logged in')
            return redirect(url_for('bucketlist'))
        error = 'password do not march'

    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you are logged out.')
    return redirect(url_for('home'))


@app.route('/bucketlist')
@login_required
def bucketlist():
    return render_template('bucketlist.html')


@app.route('/add_activity/{bucket_id}')
@login_required
def add_activity(bucket_id):
    return render_template('add_activity.html')


@app.route('/add_bucketlist', methods=['GET', 'POST'])
@login_required
def add_bucketlist():
    if request.method == 'POST':
        return redirect(url_for('bucketlist'))
    return render_template('add_bucketlist.html')

if __name__ == '__main__':
    app.run(debug=True)
