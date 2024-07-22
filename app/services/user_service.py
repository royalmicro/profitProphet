from app.models import User

def create_user(username, email):
    user = User(username=username, email=email)
    return user
