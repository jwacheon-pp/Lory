from django.shortcuts import get_object_or_404
from users.models import User

def get_user_detail(user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user