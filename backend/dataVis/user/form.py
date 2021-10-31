
import django.forms as froms
from user.models import User


class RegisterForm(froms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = None
