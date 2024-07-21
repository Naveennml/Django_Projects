#from django import forms
#rom django.contrib.auth.models import User
#from .models import UserProfile

#class UserRegistrationForm(forms.ModelForm):
##    password = forms.CharField(widget=forms.PasswordInput)
 #   class Meta:
 #       model = User
 #       fields = ['username', 'password', 'email']

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ['profile_pic', 'profile_link']


from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username','email','password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
