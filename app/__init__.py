# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.models.models import User

from app.models.models import db,populate_database  # Import db from models
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['pImgFolder'] = 'app/static/profileImages'
    login_manager = LoginManager()
    login_manager.init_app(app)

    db.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    migrate = Migrate(app, db)
    app.secret_key = 'starypijanydosklepuposzedłpomleko'
    with app.app_context():
        # Import routes and models
        from .routes.main import main
        from .routes.login import login_bp  # Ensure correct import
        from .routes.recipe import recipes
        from .routes.userProfile import userProfile_bp
        app.register_blueprint(main)
        app.register_blueprint(login_bp)  # Register the blueprint
        app.register_blueprint(recipes)
        app.register_blueprint(userProfile_bp)

        db.create_all()
        # Clear all tables
        
        db.session.commit()

    return app

