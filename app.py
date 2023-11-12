from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# flask login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        # receive data and save to database
        return redirect(url_for('index'))

    return render_template('register.html', error=error)


app.run(debug=True, port=4000)
