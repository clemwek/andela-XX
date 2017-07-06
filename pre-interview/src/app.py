from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['inputPassword'])
        print(request.form['inputEmail'])
        if request.form['inputPassword'] != 'admin' or request.form['inputEmail'] != 'admin@test.com':
            error = 'Invalid credentials, please try again.'
        else:
            return redirect(url_for('bucketlist'))
    return render_template('login.html', error=error)


@app.route('/bucketlist')
def bucketlist():
    return render_template('bucketlist.html')


@app.route('/add_activity/{bucket_id}')
def add_activity(bucket_id):
    return render_template('add_activity.html')


@app.route('/add_bucketlist', methods=['GET', 'POST'])
def add_bucketlist():
    if request.method == 'POST':
        return redirect(url_for('bucketlist'))
    return render_template('add_bucketlist.html')

if __name__ == '__main__':
    app.run(debug=True)
