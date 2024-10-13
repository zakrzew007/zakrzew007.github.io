from faker import Faker
from models.models import User, Recipe, db
from app import create_app  # Import your Flask application factory

fake = Faker()
def create_test_users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User(
            username=fake.user_name(),
            password=fake.password()
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

def create_test_recipes(users, num_recipes=20):
    for _ in range(num_recipes):
        recipe = Recipe(
            title=fake.sentence(nb_words=5),
            description=fake.text(max_nb_chars=200),
            user_id=fake.random_element(users).id
        )
        db.session.add(recipe)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()  # Create an instance of your Flask app
    with app.app_context():  # Push the application context
        db.create_all()  # Ensure the tables are created
        users = create_test_users()
        create_test_recipes(users)
        print("Test data created successfully.")

