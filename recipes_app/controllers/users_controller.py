from flask import render_template, request, redirect, session
from flask import flash 
from flask_bcrypt import Bcrypt
from recipes_app import app
from recipes_app.models.User import User
from recipes_app.models.Recipes import Recipes

bcrypt = Bcrypt(app)


@app.route ('/')
def home():
    return render_template('index.html')


@app.route('/register',methods=['POST'])
def register():

    if not User.validate_registration(request.form):
         return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.addUser(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id'],
       
    }
    return render_template("home.html",user=User.get_user_id(data), recipes=Recipes.get_recipes())

@app.route('/login',methods=['POST'])
def login():
    
    user= User.get_user_email(request.form)
 
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route ('/logout', methods=['GET'])
def closeSession():
        session.clear()
        responseObj={
            'message': 'logout succesfully'
        }
        return responseObj
