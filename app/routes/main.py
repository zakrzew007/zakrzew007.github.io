# app/routes/main.py

from flask import Blueprint, render_template
from app.models.models import Recipe, User,populate_database #type: ignore
from app import db #type: ignore
main = Blueprint('main', __name__)

@main.route('/mainView')
def mainView():
    
    recipes = Recipe.query.all()
   
    return render_template('main/mainView.html',recipes=recipes)

