from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreatrionForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [ 
            'username',
            'password1',
            'password2',
        ]

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
        ]