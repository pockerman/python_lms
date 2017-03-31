from django import forms

class ContactForm(forms.Form):
	max_length=100
	contact_name = forms.CharField(required=True,max_length=max_length,label="contact_name")
	contact_email = forms.EmailField(required=True,label="contact_email")
	content = forms.CharField(required=True,widget=forms.Textarea,label="content")
	subject = forms.CharField(required=True,max_length=max_length,label="subject")

	class Meta:
		fields=('contact_name', 'contact_email', 'subject','content')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class HireFormBase(forms.Form):
	max_length=100
	contact_name = forms.CharField(required=True,max_length=max_length,label="contact_name")
	contact_surname = forms.CharField(required=True,max_length=max_length,label="contact_surname")
	contact_email = forms.EmailField(required=True,label="contact_email")
	content = forms.CharField(required=False,widget=forms.Textarea,label="content")
	university = forms.CharField(required=True,max_length=max_length,label="university")
	department = forms.CharField(required=True,max_length=max_length,label="department")
	#module = forms.CharField(required=True,label="department")

class HireForm(HireFormBase):

	HIRE_CHOICES = [('Select','Select'),
									('Teaching','Teaching'),
									('Semester Assignment','Semester Assignment'),
									('Degree Dissertation','Degree Dissertation'),
									('MSc Assignment','MSc Assignment'),
									('MSc Dissertation','MSc Dissertation'),
									('Statistical Analysis','Statistical Analysis'),
									('Programming Assignment','Programming Assignment')]

	LANGUAGE_CHOICES = [('Select','Select'),('English','English'),('Greek','Greek')]
	
	hire_choices = forms.ChoiceField(choices=HIRE_CHOICES,label='hire_choices')
	language = forms.ChoiceField(choices=LANGUAGE_CHOICES,label='language')
	
	class Meta:
		fields=('contact_name','contact_surname', 'contact_email',
						'hire_choices', 'language','content','university','department')

	def is_valid(self):

		valid = super(HireForm,self).is_valid()
		hire_choice = self.cleaned_data['hire_choices']

		if hire_choice == 'Select':
			self.add_error('hire_choices', 'Please select a choice')
			valid = False

		language = self.cleaned_data['language']

		if language == 'Select':
			self.add_error('language', 'Please select a choice')
			valid = False
			
		return valid

	@staticmethod
	def get_failure_msg():
		return 'Message failed. The form has errors. Please correct the errors below.'

	
	
