from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template import Context
from django.template.loader import get_template

from ustdy.website_settings import site_full_name_team
from utils_app.utilities import get_errors_map_list

from .forms import ContactForm,HireForm

# Create your views here.

def handle_contact_form(request,redirect_ulr,page_data,template):
	"""
		Process the data passed by the user in the contact form. If the data
		is ok and no error is found it redirects the user to the view handled
		by contact_success
	"""

	form = ContactForm(data=request.POST)
	if form.is_valid():
		name = form.cleaned_data['contact_name']
		email = form.cleaned_data['contact_email']
		subject = form.cleaned_data['subject']
		form_content = form.cleaned_data['content']

		# Email the profile with the contact information
		template = get_template('contact/contact_email.txt')
		content = template.render({'contact_name': name,
                				 			 'contact_email': email,
                				       'form_content': form_content,})

		email = EmailMessage("New contact form submission",content,
                					"Your website" +'',['youremail@gmail.com'],headers = {'Reply-To':email })
		email.send()
		return redirect(redirect_ulr)
	else:
		messages.error(request, 'Message failed. The form has errors. Please correct the errors below.')
		error_data = get_errors_map_list(form)
		page_data.update(error_data)
		page_data['contact_name_used'] = request.POST.get('contact_name','')
		page_data['contact_emal_used'] = request.POST.get('contact_email','')
		page_data['content_used'] = request.POST.get('content','')
		return render(request,template,page_data)
	
	

def contact_index(request,template="contact/contact.html"):
	"""
		Handles the view for contact
	"""
	page_data={"meta_author_content":site_full_name_team,
						 "meta_description_content":"Contact "+ site_full_name_team+", Hire a tutor for science, engineering and programming courses, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ,ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΦΟΙΤΗΤΕΣ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟ, ΕΠΙΣΤΗΜΕΣ, ΠΟΛΥΤΕΧΝΙΚΕΣ ΣΧΟΛΕΣ",
						 "meta_keywords_content":"University tutors, engineering tutors, programming tutors, ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΦΟΙΤΗΤΕΣ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟ, ΠΑΝΕΠΙΣΤΗΜΙΑΚΑ ΜΑΘΗΜΑΤΑ",
						 "selectcontact":True,"max_length":ContactForm.max_length}

	if request.method == 'POST':
		return handle_contact_form(request,'/contact/success/',page_data,template)
	return render(request,template,page_data)

def contact_success(request,template="contact/contact_success.html"):
	"""
		Handles the view after a successfuly submitting a contact form.
	"""
	page_data={"meta_author_content":site_full_name_team,}
	return render(request,template,page_data)
	


def handle_contact_hire(request,redirect_url,form,page_data,template):

	"""
		Processes the data passed by the user in the hire tutor form. If the data
		is ok and no error is found it redirects the user to the view handled
		by contact_hire_success.
	"""
	if form.is_valid():
		name = form.cleaned_data['contact_name']
		surname = form.cleaned_data['contact_surname']
		email = form.cleaned_data['contact_email']
		hire_option = form.cleaned_data['hire_choices']
		language = form.cleaned_data['language']
		comments = form.cleaned_data['content']
		university = form.cleaned_data['university']
		department = form.cleaned_data['department']
		#module = form.cleaned_data['module']
		template = get_template('contact/contact_hire_email.txt')
		content = template.render({'contact_name': name,
												 'contact_surname':surname,
                				 'contact_email': email,
												 'hire_option':hire_option,
												 'language':language,
												 'university':university,
												 'department':department,
												 #'module':module,
                				 'form_content': comments,})

		email = EmailMessage("New tutor hire form submission",content,
                					"Your website" +'',['youremail@gmail.com'],headers = {'Reply-To':email })
		email.send()
		return redirect(redirect_url)
	else:
		messages.error(request, form.get_failure_msg())
		error_data = get_errors_map_list(form)
		print(error_data)
		page_data.update(error_data)
		page_data['form']= form
		return render(request,template,page_data)	

def contact_hire(request,template="contact/contact_hire.html"):
	"""
		Handles the view for hiring a tutor
	"""

	page_data={"meta_author_content":site_full_name_team,
						"meta_description_content":"Contact "+ site_full_name_team+", Hire a tutor for science, engineering and programming courses, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ,ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΦΟΙΤΗΤΕΣ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟ, ΕΠΙΣΤΗΜΕΣ, ΠΟΛΥΤΕΧΝΙΚΕΣ ΣΧΟΛΕΣ",
						 "meta_keywords_content":"University tutors, engineering tutors, programming tutors, ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΦΟΙΤΗΤΕΣ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ ΓΙΑ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟ, ΠΑΝΕΠΙΣΤΗΜΙΑΚΑ ΜΑΘΗΜΑΤΑ",
						 "selecteducation":True,"selecttutoring":True,
						 "max_length":HireForm.max_length}

	if request.method=='POST':
		form = HireForm(request.POST)
		return handle_contact_hire(request,'/contact/hire-success/',form,page_data,template)
	form = HireForm()
	page_data['form']=form
	return render(request,template,page_data)


def contact_hire_success(request,template="contact/contact_hire_success.html"):
	"""
		Handles the view after a successfuly submitting a hire form.
	"""
	return render(request,template,{"meta_author_content":site_full_name_team,})


