import os
import io

from django import forms
from django.contrib.auth.models import User
#from django.core.files.storage import FileSystemStorage

#from opensim_dev.settings import MEDIA_ROOT,PROFILES_ROOT
from utils_app.utilities import INVLALID_LOCATION
from .models import Profile


#general login form
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields=('username', 'password')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password',widget=forms.PasswordInput,required=True)
	password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput,required=True)

	class Meta:
		model = User
		fields = ('first_name','last_name', 'username', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']

class ProfileEditForm(forms.ModelForm):
	#dob = forms.DateField(required=True, input_formats='%Y-%m-%d')
	class Meta:
		model = Profile
		fields = ('photo',)

	def upload_photo_file(self,request):

		file = request.FILES.get('photo',None)
		if file != None:
		
			folder = str(request.user.id)
			location = os.path.join(PROFILES_ROOT, folder)
			fs = FileSystemStorage(location=location)
			try:
				os.makedirs(os.path.join(PROFILES_ROOT, folder))
			except:
				print("Could not create folder")

			filename = fs.save(file.name, file)
			print(filename)
			#return str(request.user.id)+'/'+filename
			return filename
		return INVLALID_LOCATION()


	
#Will allow users to edit their first name, last name, and
#e-mail, which are stored in the built-in User model.
#class UserEditForm(forms.ModelForm):
#	class Meta:
#		model = User
#		fields = ('first_name', 'last_name', 'email')

	
#Will allow users to edit the extra data we save in the
#custom Profile model. Users will be able to edit their date of birth and
#upload a picture for their profile.

#class ProfileEditForm(forms.ModelForm):
	#dob = forms.DateField(required=True, input_formats='%Y-%m-%d')
#	class Meta:
#		model = Profile
#		fields = ('photo',)

#	def upload_photo_file(self,request):
#
#		file = request.FILES.get('photo',None)
#		if file != None:
		
#			folder = str(request.user.id)
#			location = os.path.join(PROFILES_ROOT, folder)
#			fs = FileSystemStorage(location=location)
#			try:
#				os.makedirs(os.path.join(PROFILES_ROOT, folder))
#			except:
#				print("Could not create folder")

#			filename = fs.save(file.name, file)
#			print(filename)
			#return str(request.user.id)+'/'+filename
#			return filename
#		return INVLALID_LOCATION()

		
		



















