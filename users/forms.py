from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 

from .models import CustomUser 
 
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:        
        model = CustomUser        
        fields = ('email', 'first_name', 'last_name')  
class CustomUserChangeForm(UserChangeForm):    
    class Meta:        
        model = CustomUser        
        fields = UserChangeForm.Meta.fields