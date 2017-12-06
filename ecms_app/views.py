from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

#local imports
from ecms_course_create_app.models import Course
from ecms_course_create_app.models import Subject
from ecms_course_create_app.models import Module
from ecms_course_create_app.models import Lesson
from ecms_course_create_app.models import LessonQuiz

from utils_app.utilities import get_errors_map_list
from utils_app.utilities import render_user_html_file
from utils_app.utilities import render_html_content
from ustdy.settings import COURSES_ROOT
from ustdy.settings import COURSES_URL
from ustdy.website_settings import site_full_name_team

from .forms import NotifyForm
from .forms import LessonQuizValidateForm

##general views
#========================

def get_subject_courses_count_list():
	subjects = Subject.objects.all()

	subject_courses_count_list=[]

	for subject in subjects:
		count = Course.published.filter(subject=subject).count()
		subject_courses_count_list.append((subject,count))
	return subject_courses_count_list

def get_meta_tags():
	return {"meta_author_content":site_full_name_team,
					"meta_description_content":"On-line university courses in C++ programming, Java programming, CFD with C++, rigid body dynamics simulation, machine learning with c++, artificial intelligence with c++, descriptive statistics with Python,statistical inference with Python, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ, C++ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ, JAVA ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ, ΜΗΧΑΝΙΚΗ ΜΑΘΗΣΗ ΜΕ C++, ΤΕΧΝΙΤΗ ΝΟΗΜΟΣΥΝΗ ΜΕ C++, ΠΕΡΙΓΡΑΦΙΚΗ ΣΤΑΤΙΣΤΙΚΗ ΜΕ Python, ΕΠΑΓΩΓΙΚΗ ΣΤΑΤΙΣΤΙΚΗ ΜΕ Python",
					"meta_keywords_content":"On-line university courses in C++ programming, Java programming, CFD with C++, rigid body dynamics simulation, machine learning with c++, artificial intelligence with c++, descriptive statistics with Python,statistical inference with Python, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ, C++ ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ, JAVA ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ, ΜΗΧΑΝΙΚΗ ΜΑΘΗΣΗ ΜΕ C++, ΤΕΧΝΙΤΗ ΝΟΗΜΟΣΥΝΗ ΜΕ C++, ΠΕΡΙΓΡΑΦΙΚΗ ΣΤΑΤΙΣΤΙΚΗ ΜΕ Python, ΕΠΑΓΩΓΙΚΗ ΣΤΑΤΙΣΤΙΚΗ ΜΕ Python"}

def ecms_courses_tmp_view(request,template="ecms/ecms_index.html"):

	page_data={"selecteducation":True,
				"selectcourses":True,
				 "meta_author_content":site_full_name_team,
				 "meta_description_content":
				 "upcoming courses UstudyNow,C++ programming, Java programmin, Introduction to HPC with C++, CFD with C++, Machine Learning with C++" }

	return render(request,template,page_data)

def courses_catalog_view(request,template="ecms/catalog_view.html"):
    """

    Renders the view serving the courses in the application
    """

    subjects = get_subject_courses_count_list()
    courses = Course.published.all()

    total_counter=0
    for subject in subjects:
        total_counter += subject[1]

    page_data={"meta_author_content":site_full_name_team,
               "selecteducation":True,
               "selectcourses":True,
               "subjects":subjects,
				       "total_counter":total_counter,
               "subject_title":"ALL",
               "courses":courses,"COURSES_URL":COURSES_URL}
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

def course_overview_view(request,course_slug,template='ecms/course_overview_view.html'):
    """
    Renders the view for the course overview
    """
    course = get_object_or_404(Course,slug=course_slug)
    meta_keywords = ""
    for tag in course.tags.all():
		    meta_keywords +=","+str(tag)

    module = get_object_or_404(Module,course=course,order_id=1)
    page_data={"module_slug":module.slug,
               "meta_author_content":course.meta_author,
						   "meta_description_content":course.meta_description,
						   "meta_keywords_content": meta_keywords}

    #let's render the syllabus files for the course
    syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"
    try:
        with open(COURSES_ROOT+'/'+course.slug+'/default_syllabus.html', 'r') as myfile:
            syllabus_html = render_user_html_file(myfile,{})
    except:
        syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"

    #this may not be true. the course.photo_file.name
    #should return only the file name
    img = course.photo_file.name
    img_split = img.split('/')
    img_name = img_split[len(img_split)-1]
    page_data.update({"course":course,"syllabus_html":syllabus_html,
																  "img_name":img_name,"selecteducation":True,"selectcourses":True,
																	"COURSES_URL":COURSES_URL})

    return render(request,template,page_data)

def module_overview_view(request,course_slug,module_slug,template='ecms/module_overview_view.html'):
    """
    Renders the view for viewing a module
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    page_data={"course":course,"mymodule":module,"COURSES_URL":COURSES_URL}
    return render(request,template,page_data)


def lesson_view(request,course_slug,module_slug,lesson_slug,template='ecms/lesson_view.html'):
    """
    Renders the view for a lesson
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    mylesson = get_object_or_404(Lesson,course=course,module=module,slug=lesson_slug)
    text_content = render_html_content(mylesson.text_content,{})
    page_data={"mylesson":mylesson,"text_content":text_content}
    return render(request,template,page_data)

def quiz_start_view(request,course_slug,module_slug,lesson_slug,quiz_id,template='ecms/quiz_start_view.html'):
    """
     Renders the view for starting a lesson quiz
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,course=course,module=module,slug=lesson_slug)
    myquiz = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)
    page_data={"myquiz":myquiz}
    return render(request,template,page_data)

def quiz_view(request,course_slug,module_slug,lesson_slug,quiz_id,template='ecms/quiz_view.html'):
    """
    If request is POST it renders the view for the quiz otherwise if checks the correctness
    of the results and reports back to the user
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,course=course,module=module,slug=lesson_slug)
    myquiz = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)
    page_data={"myquiz":myquiz}

    if request.method == 'POST':
        form = LessonQuizValidateForm(myquiz)
        result = form.validate(request)
        request.session['quiz_result'] = result
        return redirect('/courses/%s/modules/%s/lessons/%s/quizes/%s/results/'%(course_slug,module_slug,lesson_slug,quiz_id))
    return render(request,template,page_data)

def quiz_results_view(request,course_slug,module_slug,lesson_slug,quiz_id,template='ecms/quiz_results_view.html'):
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,course=course,module=module,slug=lesson_slug)
    myquiz = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)
    questions = myquiz.lesson_quiz_questions.all()
    page_data={"myquiz":myquiz}
    result = request.session['quiz_result']

    page_data['questions'] = []
    counter=1
    for q in questions:
        page_data['questions'].append({'question':q,'result':result['q'+str(counter)]})
        counter+=1

    return render(request,template,page_data)



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
