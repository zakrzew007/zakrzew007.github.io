from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import faker
from random import choice, sample
from flask_login import UserMixin
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Change as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

fake = faker.Faker()

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(350), nullable=False)
    
    profile_image = db.Column(db.String(150), nullable=True)
    
    
    recipes = db.relationship('Recipe', backref='user', lazy=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Recipe(db.Model):
    __tablename__ = 'recipe'
    
    id = db.Column(db.Integer, primary_key=True)
    ingredients = db.Column(db.Text, nullable=False)
    recipe = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.relationship('RecipeTag', back_populates='recipe')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    recipes = db.relationship('RecipeTag', back_populates='tag')

class RecipeTag(db.Model):
    __tablename__ = 'recipe_tags'
    
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)

    recipe = db.relationship('Recipe', back_populates='tags')
    tag = db.relationship('Tag', back_populates='recipes')

# Function to create test users
def create_test_users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            password=generate_password_hash(fake.password())
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

# Function to create test recipes
def create_test_recipes(users, num_recipes=20):
    for i in range(num_recipes):
        ingredients_list = sample(ingredient_list, 5)  # Select random ingredients
        ingredients = ', '.join(ingredients_list)
        steps = ' / '.join(fake.sentences(nb=2))
        recipe = Recipe(
            recipe=fake.sentence(nb_words=2),
            ingredients=ingredients,
            steps=steps,
            user_id=choice(users).id,
            image_url=f"../static/recipeImages/{i + 1}.jpg"
        )
        db.session.add(recipe)
    db.session.commit()
def link_recipes_to_tags():
    # Get all recipes and tags
    recipes = Recipe.query.all()
    tags = Tag.query.all()

    for recipe in recipes:
        # Assign random tags to each recipe
        random_tags = sample(tags, k=min(2, len(tags)))  # Adjust the number of tags as needed
        for tag in random_tags:
            recipe_tag = RecipeTag(recipe_id=recipe.id, tag_id=tag.id)
            db.session.add(recipe_tag)
    
    db.session.commit()

# List of actual ingredients
ingredient_list = [
    'flour', 'sugar', 'butter', 'eggs', 'milk', 'baking powder', 'salt', 'vanilla extract',
    'cocoa powder', 'chocolate chips', 'honey', 'yeast', 'olive oil', 'garlic', 'onion',
    'tomato', 'basil', 'oregano', 'cheese', 'chicken', 'beef', 'pork', 'fish', 'shrimp',
    'rice', 'pasta', 'potato', 'carrot', 'broccoli', 'spinach', 'bell pepper', 'mushroom',
    'apple', 'banana', 'orange', 'lemon', 'lime', 'strawberry', 'blueberry', 'raspberry',
    'yogurt', 'cream', 'mayonnaise', 'mustard', 'ketchup', 'soy sauce', 'vinegar', 'wine'
]

def create_test_tags():
    tags = ['vegan', 'gluten-free', 'dairy-free', 'low-carb', 'paleo', 'keto']
    for tag_name in tags:
        if not Tag.query.filter_by(name=tag_name).first():
            tag = Tag(name=tag_name)
            db.session.add(tag)
    db.session.commit()

def populate_database():
    users = create_test_users()
    create_test_recipes(users)
    create_test_tags()
    link_recipes_to_tags()
    print("Database populated with test data.")
