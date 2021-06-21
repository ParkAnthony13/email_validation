from flask.helpers import get_flashed_messages
from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.email import Email
# from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success')
def emails():
    emails = Email.get_all()
    return render_template('success.html',emails = emails)

@app.route('/process',methods=['POST'])
def new_dojo():
    if not Email.validate_user(request.form):
        return redirect('/')
    if not Email.duplicates():
        return redirect('/')
    data = {
        'name':request.form['name'],
        'email':request.form['email']
    }
    Email.insert(data)
    return redirect('/success')

@app.route('/delete/<int:id>')
def delete(id):
    Email.delete({'id':id})
    return redirect('/success')

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_user(request.form):
        print(get_flashed_messages())
        return redirect('/')
    # return redirect('/success')