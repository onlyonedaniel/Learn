from user.models import User
from django.db.models import Q


def has_register(username, mobile):
    return User.objects.filter(Q(username=username) | Q(mobile=mobile)).exists()


def registe(username, password, mobile):
    user = User(username=username, password=password, mobile=mobile)
    user.save()
    return user
