from django.contrib.auth import get_user_model
from db.models import User


def create_user(
        username: str,
        password: str,
        first_name: str = None,
        last_name: str = None,
        email: str = None
):
    user = get_user_model().objects.create_user(username=username)
    user.set_password(password)
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if email:
        user.email = email
    user.save()


def get_user(user_id: int):
    return User.objects.get(id=user_id)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
):
    user = User.objects.get(id=user_id)
    if password:
        user.set_password(password)
    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
