

from django import forms
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from .models import NotifyCourseStart


#general login form
class NotifyForm(forms.ModelForm):
	name = forms.CharField(max_length=200,required=True)
	email = forms.EmailField(required=True)
	
	class Meta:
		model = NotifyCourseStart
		fields=['name','email',]

#class UserRegistrationForm(forms.ModelForm):
#	password = forms.CharField(label='Password',widget=forms.PasswordInput)
#	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

#	class Meta:
#		model = User
#		fields = ('first_name','last_name', 'username', 'email')

#	def clean_password2(self):
#		cd = self.cleaned_data
#		if cd['password'] != cd['password2']:
#			raise forms.ValidationError('Passwords don\'t match.')
#		return cd['password2']

	
#Will allow users to edit their first name, last name, and
#e-mail, which are stored in the built-in User model.
#class UserEditForm(forms.ModelForm):
#	class Meta:
#		model = User
#		fields = ('first_name', 'last_name', 'email')

	


		
		



















