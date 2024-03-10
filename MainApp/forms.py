from MainApp import models
from django.forms import ModelForm

class UserRegistration(ModelForm):
    class Meta:
        model = models.user_registration
        fields = ["Username", "Password"]
    