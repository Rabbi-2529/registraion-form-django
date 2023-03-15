from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class SignupForms(UserCreationForm):
    class meta:
        model=User
        fields=['username','first_name','last_name','email']
class profileForms(UserChangeForm):
    password=None
    class meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login']
        labels={'email':"Email"}                                                                                               