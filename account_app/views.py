from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger


from utils_app.utilities import get_errors_map_list

#local imports
from .forms import LoginForm,UserRegistrationForm,ProfileEditForm
from .models import Profile

# Create your views here.



#user login
def user_login(request,template='account/login.html'):
	page_data={"selectlogin":True}

	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'],password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					#after succesful login redirect to the user profile
					return HttpResponseRedirect('../profile/')
				else:
					return HttpResponse('This account is disabled.')
		else:
				messages.error(request, "Your username or password did not match. Please try again.")
				error_data = get_errors_map_list(form)
				page_data.update(error_data)
				#page_data['username_used'] = request.POST.get('username_used','')
				#page_data['pass_used'] = request.POST.get('pass_used','')
				return render(request,template,page_data)
	else:	
		return render(request, template , page_data)

@login_required
def user_logout(request,template="account/logout.html"):
	"""
		Log out the user given by the request by calling auth_views.logout.
		It redirects the user to the /account/login/ URL.
	"""
	auth_views.logout(request)
	messages.success(request,"You have been successfully logged out.")
	return redirect('/account/login/')
	#return render(request,template,{'not_main_page': True})

def user_register(request,template='account/register.html'):
	"""
			Register a user within Ustdy
	"""

	page_data={"selectlogin":True}

	if request.method=='POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = form.save(commit=False)
			# Set the chosen password
			new_user.set_password(form.cleaned_data['password'])

			# Save the User object
			new_user.save()

			#add a new student in the students group
			students = get_object_or_404(Group, name="Students") #Group.objects.get(name="Students")
			students.user_set.add(new_user)

			#create a new profile
			profile = Profile.objects.create(user=new_user)
			profile.save()

			#create a new student
			#student = Student.objects.create(user=new_user)
			#student.save()
			return redirect('/account/success_register/%s/'%new_user.first_name)
		else:
			messages.error(request, 'Registration failed. The form has errors. Please correct the errors below.')
			errors_map = get_errors_map_list(form)
			
			#we want to show what the user has entered
			errors_map['first_name_val'] = request.POST.get('first_name','')
			errors_map['last_name_val'] = request.POST.get('last_name','')
			errors_map['username_val'] = request.POST.get('username','')
			errors_map['email_val'] = request.POST.get('email','')

			#we don't return these as it is unsafe
			#errors_map['password_val'] = request.POST.get('password','')
			#errors_map['password2_val'] = request.POST.get('password2','')
			
			return render(request,template,errors_map)

	return render(request,template,page_data)

def success_registration(request,first_name,template='account/register_done.html'):
	"""
		Handles the view upon successful registration
	"""
	return render(request,template,{'first_name':first_name})

def instructor_profile(request,template='account/instructor_profile.html'):
	#find all the courses of the instructor
	mycourses = Course.objects.all().filter(owner_id = request.user.id)
	print("number of courses: "+str(len(mycourses)))
	return render(request,template,
								{'section': 'dashboard','not_main_page': True,"mycourses":mycourses,"selectmyprofile":True})

def student_profile(request,template='account/profile.html'):

	student = Student.objects.get(user_id=request.user.id)
	mycourses = student.courses.all()
	paginator = Paginator(mycourses, 4)
	page = request.GET.get('page')

	try:
		courses_on_page = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer deliver the first page
		courses_on_page = paginator.page(1)
	except EmptyPage:
		# If page is out of range deliver last page of results
		courses_on_page = paginator.page(paginator.num_pages)

	#print(mycourses)
	page_data={"selectmyprofile":True}
	page_data['mycourses'] = courses_on_page
	page_data['page'] = page
	page_data['numpages'] = paginator.num_pages
	
	return render(request,template,page_data)

@login_required
def user_profile(request):

	user = User.objects.get(username=request.user)

	if user.groups.filter(name='Instructors').exists():
		return instructor_profile(request)

	if user.groups.filter(name='Students').exists():
		return student_profile(request)

@login_required
def user_profile_edit(request,template='account/edit.html'):
	"""
		Handles the view for editing the user profile
	"""

	if request.method == 'POST':

		#the user canceled the editing
		if 'cancel' in request.POST:
			return redirect('/account/profile/')

		#the user deleted the profile image
		if 'delete-img' in request.POST:
			profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
			profile = profile_form.save(commit=False)
			profile.photo = None
			profile.save()
			messages.success(request, 'Successfully deleted profile photo.')
			return redirect('/account/profile/')
			

		user_form = UserEditForm(instance=request.user,data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

		if user_form.is_valid() and profile_form.is_valid():

			user_form.save()
			profile = profile_form.save(commit=False)

			#check if we have a photo file
			file = request.FILES.get('photo',None)
			if file != None:
				location = profile_form.upload_photo_file(request)
				profile.photo = location

			profile.save()

			messages.success(request, 'Profile updated successfully')
			return redirect('/account/profile/')
		else:
			#print(user_form.errors)
			#print("Profile errors")
			#print(profile_form.errors)
			messages.error(request, 'Error updating your profile. Form has errors. Please correct the errors')
			errors_map = get_errors_map_list(user_form) 
			profile_errors = get_errors_map_list(profile_form) 
			errors_map.update(profile_errors)
			return render(request,template,errors_map)
			
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		
		data={}
		data['name'] = request.user.first_name

	return render(request,template,{'user_form': user_form,'profile_form': profile_form,'not_main_page': True})

#def my_password_change(request,template='account/password_change_form.html'):
#	return auth_views.password_change(request,template_name=template,post_change_redirect='/account/password/change/done/')

#def my_password_change_done(request,template='account/password_change_done.html'):
#	return auth_views.password_change_done(request,template_name=template)


def my_password_change_done(request,template='account/password_change_done.html'):
	return auth_views.password_change_done(request,template_name=template)

def my_password_change(request,template='account/password_change_form.html'):
	return auth_views.password_change(request,template_name=template,post_change_redirect='/account/password/change/done/')

def my_password_reset_done(request,template='account/password_reset_done.html'):
	return auth_views.password_reset_done(request,template)

def my_password_reset(request,template='account/password_reset_form.html'):

	if request.method=='POST':
		if 'cancel'  in request.POST:
			#if the user canceled it return to the main page
			return redirect('/')

	return auth_views.password_reset(request,template_name=template,
												email_template_name='account/password_reset_email.html',
												post_reset_redirect='/account/password-reset/done/')

def my_password_reset_confirm(request,uidb64,token,template='account/password_reset_confirm.html'):
	return auth_views.password_reset_confirm(request,
																uidb64=uidb64,token=token,
																post_reset_redirect='/account/password-reset/complete/',template_name=template)

def my_password_reset_complete(request,template='account/password_reset_complete.html'):
	return auth_views.password_reset_complete(request,template_name=template)

