import re
from typing import ValuesView

from jinja2.utils import is_undefined
import recipes_app
from recipes_app.config.MySQLConnection import connectToMySQL
from flask import flash




class Recipes:
    db="login"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooking = data['cooking']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def addNewRecipe(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, cooking, date_made, user_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(cooking)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
     
    
    @classmethod
    def get_user_recipe( cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
     
        results = connectToMySQL( cls.db ).query_db( query, data )
        return cls(results[0])
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
     
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, cooking=%(cooking)s, date_made=%(date_made)s,updated_at=now() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
       
        #if len(recipe['cooking'])>1:
            #is_valid=False
            #flash("You must select Yes or No")
        
        if len(recipe['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters","recipe")
        if len(recipe['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","recipe")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date")
       
        return is_valid
    
    @classmethod
    def get_recipes(cls):
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            print(row['date_made'])
            recipes.append( cls(row) )
        return recipes