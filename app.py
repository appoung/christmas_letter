from flask import Flask, render_template, request, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
firebase_db = firestore.client()

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')


# flask login
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        document = firebase_db.collection(u'users').document(username)
        user = document.get()
        if user.exists:
            if user.to_dict()['password'] == password:
                session['username'] = username
                session['password'] = password
                return render_template('index.html')

            else:
                error = '응 비번틀림 ㅋㅋㄹㅃㅃ'

        else:
            error = '응 닉넴없음 ㅋㅋㄹㅃㅃ'
        return render_template('login.html', error=error)
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    if request.method == 'POST':
        data = {
            u'username': request.form['username'],
            u'password': request.form['password']
        }
        # if username exists,return error
        document = firebase_db.collection(u'users').document(
            request.form['username'])
        user = document.get()
        if user.exists:
            error = '닉넴 겹치누ㅠ'
            return render_template('register.html', error=error)
        # else save to database
        else:
            document = firebase_db.collection(
                u'users').document(request.form['username'])
            document.set(data)
            return redirect(url_for('index'))

        # receive data and save to database
        return redirect(url_for('index'))

    return render_template('register.html', error=error)


@app.route('/sendletter/<username>')
def send_letter(username):
    return render_template('sendletter.html', username=username)


@app.route('/dbletter/<username>', methods=['GET', 'POST'])
def db_letter(username):
    if request.method == 'POST':
        # get password by username
        document = firebase_db.collection(u'users').document(username)
        user = document.get()
        password = user.to_dict()['password']
        # count the letter already in user's database and set the letter id
        try:
            letter_num = len(firebase_db.collection(u'letters').document(
                username).get().to_dict())+1
        except:
            letter_num = 1
        letter_id = "letter"+str(letter_num)
        new_data = {
            letter_id: request.form['letter']
        }
        print(new_data)
        # get data from database and add new letter
        document = firebase_db.collection(u'letters').document(username)
        letters = document.get().to_dict()
        # letters is like {'letter': '안뇽'}
        # and i want to add new_data like {'letter1': '안녕하세요'}
        # and result should be like {'letter': '안뇽', 'letter1': '안녕하세요'}
        if letters == None:
            document.set(new_data)
        else:
            letters.update(new_data)
        print(letters)
        document.set(letters)
        return redirect(url_for('successletter'))


@app.route('/successletter')
def successletter():
    return render_template('successletter.html')


@app.route('/letter/<username>/<password>')
def letter(username, password):
    # if theres no letters, letter_text is "편지가 없습니다"
    try:
        document = firebase_db.collection(u'letters').document(username)
        letters = document.get().to_dict()
        letter_text = []
        for letter in letters:
            letter_text.append(letters[letter])
    except:
        letter_text = "편지가 없습니다"

    return render_template('letter.html', username=username, password=password, letters=letter_text)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))


app.run(debug=True, port=5000, host='0.0.0.0')
