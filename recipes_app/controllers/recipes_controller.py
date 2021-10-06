import re
from flask import render_template, request, redirect, session
from flask import render_template,redirect,session,request,flash
from recipes_app import app
from recipes_app.models.User import User
from recipes_app.models.Recipes import Recipes


@app.route ('/recipes/new')
def newRecipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('addRecipe.html',user=User.get_user_id(data))



@app.route ('/recipes/edit/<id>', methods= ['GET'])
def editRecipe(id):
    if 'user_id' not in session:
            return redirect('/logout')
    data1={
        
        "id":int(id)
    }
    data2={
        "id":session['user_id']
    }
    return render_template ('editRecipe.html', recipe=Recipes.get_user_recipe(data1), user=User.get_user_id(data2))

@app.route('/recipe/add',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipes.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "cooking": int(request.form["cooking"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    Recipes.addNewRecipe(data)
    return redirect('/dashboard')

@app.route('/recipe/update',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipes.validate_recipe(request.form):
        return editRecipe(request.form['id'])
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "cooking": int(request.form["cooking"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Recipes.update(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data1 = {
        "id":id
    }
    data2 = {
        "id":session['user_id']
    }
    return render_template("recipes.html",recipe=Recipes.get_user_recipe(data1),user=User.get_user_id(data2))

@app.route('/recipe/delete/<id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":int(id)
    }
    Recipes.delete(data)
    return redirect('/dashboard')

    
    
    
