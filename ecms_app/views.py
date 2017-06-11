from django.shortcuts import render,get_object_or_404,redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

#local imports
from ecms_course_create_app.models import Course,Subject
from utils_app.utilities import get_errors_map_list,render_user_html_file
from ustdy.settings import COURSES_ROOT,COURSES_URL
from ustdy.website_settings import site_full_name_team
from .forms import NotifyForm

##general views
#========================

def get_subject_courses_count_list():
	subjects = Subject.objects.all()

	subject_courses_count_list=[]

	for subject in subjects:
		count = Course.published.filter(subject=subject).count()
		subject_courses_count_list.append((subject,count))
	return subject_courses_count_list

def ecms_courses_tmp_view(request,template="ecms/tmp/ecms_index.html"):
	page_data={"selecteducation":True,
						 "selectcourses":True,
						 "meta_author_content":site_full_name_team,
						 "meta_description_content":
						"upcoming courses UstudyNow,C++ programming, Java programmin, Introduction to HPC with C++, CFD with C++, Machine Learning with C++" }
	return render(request,template,page_data)

def ecms_courses_catalog_view(request,template="ecms/tmp/ecms_catalog.html"):
	subjects = get_subject_courses_count_list()
	courses = Course.published.all()
	
	total_counter=0
	for subject in subjects:
		total_counter += subject[1]

	page_data={"meta_author_content":site_full_name_team,"selecteducation":True,"selectcourses":True,"subjects":subjects,
						 "total_counter":total_counter,"subject_title":"ALL","courses":courses,"COURSES_URL":COURSES_URL}
	return render(request,template,page_data)

def ecms_courses_catalog_subject_view(request,subject_slug,template="ecms/tmp/ecms_catalog.html"):

	subjects = get_subject_courses_count_list()
	subject_req = get_object_or_404(Subject,slug=subject_slug)
	courses = Course.published.all().filter(subject=subject_req)

	total_counter=0
	for subject in subjects:
		total_counter += subject[1]

	page_data={"selecteducation":True,"selectcourses":True,"subjects":subjects,
						 "total_counter":total_counter,
							"subject_title":subject_req.title,
							"courses":courses,
							"COURSES_URL":COURSES_URL}
	return render(request,template,page_data)
	


def ecms_index_subject(request,subject_slug,template="ecms/ecms_index.html"):
	return HttpResponse('ecms index response with subject slug')

def ecms_index(request,template="ecms/ecms_index.html"):
	return HttpResponse('ecms index response') 

def course_overview(request,course_slug,template='ecms/tmp/ecms_course_overview.html'):
	course = get_object_or_404(Course,slug=course_slug)

	#let's render the syllabus files for the course
	syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"
	#print(course.syllabus_file.file)
	#print(COURSES_ROOT)
	try:
		with open(COURSES_ROOT+'/'+course.slug+'/default_syllabus.html', 'r') as myfile:
			syllabus_html = render_user_html_file(myfile,{})
	except:
		syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"
		

	#this may not be true. the course.photo_file.name
	#should return only the file name
	img = course.photo_file.name
	#print(img)
	img_split = img.split('/')
	img_name = img_split[len(img_split)-1]

	return render(request,template,{"course":course,"syllabus_html":syllabus_html,
																  "img_name":img_name,"selecteducation":True,"selectcourses":True,
																	"COURSES_URL":COURSES_URL})
	

def notify_me_course_start(request,course_slug,template='ecms/tmp/notify_user_course_start_form.html'):
	course = get_object_or_404(Course,slug=course_slug)
	if request.method=="POST":
		form = NotifyForm(request.POST)
		if form.is_valid():
			model = form.save(commit=False)
			model.course=course
			model.save()
			return redirect('/courses/course/%s/notify-me/success/'%(course_slug))
		else:
			messages.error(request, 'Registration failed. The form has errors. Please correct the errors below.')
			errors_map = get_errors_map_list(form)
			errors_map['course']=course
			#we want to show what the user has entered
			errors_map['first_name_val'] = request.POST.get('first_name','')
			
			return render(request,template,errors_map)
			
	return render(request,template,{"course":course})

def notify_me_course_start_success(request,course_slug,template='ecms/tmp/notify_user_course_start_success.html'):
	course = get_object_or_404(Course,slug=course_slug)
	return render(request,template,{"course":course})

	

@login_required
def course_module_view(request,course_slug,module_slug,template='ecms/ecms_course_module.html'):
	return HttpResponse('ecms course_module_view response')

@login_required
def course_module_section_view(request,course_slug,module_slug,section_slug,template='ecms/ecms_course_module_section_view.html'):
	return HttpResponse('ecms course_module_section_view response')

@login_required
def course_module_quiz_start_view(request,course_slug,module_slug,quiz_id,template='ecms/ecms_course_module_quiz_start.html'):
	return HttpResponse('course_module_quiz_start response')

@login_required
def course_module_quiz_do_view(request,course_slug,module_slug,quiz_id,template='ecms/ecms_course_module_quiz_do.html'):
	return HttpResponse('course_module_quiz_do_view response')

@login_required
def course_module_section_quiz_start_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms/ecms_course_module_section_quiz_start.html'):
	return HttpResponse('course_module_section_quiz_start_view response')

@login_required
def course_module_section_quiz_do_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms/ecms_course_module_section_quiz_do.html'):
	return HttpResponse('course_module_section_quiz_do_view response')

@login_required
def course_module_section_activity_view(request,course_slug,module_slug,section_slug,
																				template='ecms/ecms_course_module_section_activity.html'):
	return HttpResponse('course_module_section_activity_view response')

@login_required
def course_resourses_view(request,course_slug,template='ecms/ecms_course_resourses.html'):
	return HttpResponse('course_resourses_view response')

@login_required
def course_student_progress_view(request,course_slug,student_id,template='ecms/ecms_course_progress.html'):
	return HttpResponse('course_student_progress response')

@login_required
def course_syllabus_view(request,course_slug,template='ecms/course_syllabus.html'):
	return HttpResponse('course_syllabus_view response')



