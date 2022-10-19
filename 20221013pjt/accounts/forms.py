from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# 회원가입
class CustomUserCreationFrom(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password1',
            'password2',
        ]

# 회원 수정
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
        ]