import os
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.models import User, Recipe, RecipeTag, Tag
from flask_login import login_required, current_user,current_user
from werkzeug.utils import secure_filename

userProfile_bp = Blueprint('userProfile', __name__)

@userProfile_bp.route('/userProfile/<string:username>')
@login_required
def user_profile(username):
    userData = User.query.filter_by(username=username).first()
    userRecipes = userData.recipes
    profileImage = username + '.png'
    # Fetch tags for each recipe
    recipes_with_tags = []
    for recipe in userRecipes:
        tags = RecipeTag.query.filter_by(recipe_id=recipe.id).all()
        tagNames = [Tag.query.get(tag.tag_id).name for tag in tags]
        recipes_with_tags.append({
            'recipe': recipe,
            'tags': tagNames
        })
    
    return render_template('userProfile/userProfile.html', user=userData, recipes=recipes_with_tags,profileImage=profileImage)

@userProfile_bp.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        print("No file part")
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        print("No selected file")
        return redirect(request.url)
    
    if file:
        filename = secure_filename(file.filename)
        pimgFolderPath = os.path.join('app', 'static', 'profileImages')
        if not os.path.exists(pimgFolderPath):
            os.makedirs(pimgFolderPath)
        file.save(os.path.join(pimgFolderPath, current_user.username + '.png'))
        print("File successfully uploaded")
        return redirect(url_for('userProfile.user_profile', username=request.form.get('username')))
    
    