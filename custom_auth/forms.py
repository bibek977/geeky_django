from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class CustomUserChange(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', 'email', 'date_joined', 'last_login']