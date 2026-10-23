from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Users
class CustomUserCreationform(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'avatar', 'bio')
class CustomAuthificationForm(AuthenticationForm):
    pass