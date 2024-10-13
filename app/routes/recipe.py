from flask import Blueprint, render_template
from ..models.models import Recipe, User, RecipeTag, Tag
from sqlalchemy import text

recipes = Blueprint('recipes', __name__)

@recipes.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    
    
    tags = RecipeTag.query.filter_by(recipe_id=recipe_id).all()
    tagNames = []
    for tag in tags:
        tagNames.append(Tag.query.get(tag.tag_id).name)
            
    return render_template('main/recipe.html', recipe=recipe,tags = tagNames)