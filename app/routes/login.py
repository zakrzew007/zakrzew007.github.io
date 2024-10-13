# app/routes/login.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.models import User, db,populate_database  # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
login_bp = Blueprint('login', __name__)

# app/routes/login.py



@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            error = 'User already exists!'
        else:
            hashed_password = generate_password_hash(password)
            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('User registered successfully!')
            return redirect(url_for('login.login_view'))
    return render_template('account/register.html', error=error)
@login_bp.route('/login', methods=['GET', 'POST'])


def login_view():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the user exists and the password is correct
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user) 
            flash('Login successful!')
            return redirect(url_for('main.mainView'))
        else:
            error = 'Invalid username or password'
    return render_template('account/login.html', error=error)  # Pass the error variable to the template

@login_bp.route('/test')
def test():
    from app.models.models import create_test_users, create_test_recipes #type: ignore
    create_test_recipes(create_test_users())
    populate_database()
    return 'Test route'


# app/routes/main.py

