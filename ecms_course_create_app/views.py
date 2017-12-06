from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from utils_app.utilities import get_errors_map_list
from utils_app.utilities import render_html_content
from utils_app.utilities import render_user_html_file
from ustdy.settings import COURSES_URL
from ustdy.settings import  COURSES_ROOT

from .models import Course
from .models import Module
from .models import Lesson
from .models import LessonQuiz
from .models import LessonQuizQuestion
from .forms import ModuleCreateForm
from .forms import LessonCreateForm
from .forms import LessonUpdateForm
from .forms import upload_lesson_file_images
from .forms import update_lesson_file_images
from .forms import LessonQuizAddQuestionForm
from .forms import LessonQuizCreateForm
from .forms import CourseUpdateForm

@login_required
def course_view(request,course_slug,template='ecms_course_create_app/course_start_view.html'):
    """
    Simply serves the overview or start page of a course
    """
    course = get_object_or_404(Course,slug=course_slug)

    #let's render the syllabus files for the course
    syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"
    try:
        with open(COURSES_ROOT+'/'+course.slug+'/default_syllabus.html', 'r') as myfile:
            syllabus_html = render_user_html_file(myfile,{})
    except:
		    syllabus_html = "NO SYLLABUS HAS BEEN UPLOADED"

    page_data={'course':course,"COURSES_URL":COURSES_URL,"syllabus_html":syllabus_html}

    return render(request,template,page_data)

@login_required
def course_create_view(request,template='ecms_course_create_app/course_create_form_view.html'):
    """
        Handles the view for creating a course
    """
    return render(request,template)

@login_required
def course_update_view(request,course_slug,template='ecms_course_create_app/course_update_form_view.html'):
    """
    Serves the view for updating a course
    """
    course = get_object_or_404(Course,slug=course_slug)
    page_data={'course':course}

    if request.method=='POST':
        #handle the possible cancel
        if "cancel" in request.POST:
            return redirect('/account/profile/instructor/')


    form =CourseUpdateForm()
    page_data['form']=form
    return render(request,template,page_data)

@login_required
def course_delete_view(request,course_slug,template='ecms_course_create_app/course_delete_view.html'):

    """
    Deletes the course from the database when the request is POST otherwise
    simply serves the confirmation page
    """

    course = get_object_or_404(Course,slug=course_slug)
    page_data={'course':course}

    if request.method=='POST':
        #handle the possible cancel
        if "cancel" in request.POST:
            return redirect('/account/profile/instructor/')

        try:
            title = course.title
            course.delete()
            messages.success(request, 'Successfully deleted course %s.'%title)
            return redirect('/account/profile/instructor/')
        except:
            messages.success(request, 'Could not delete course %s. Something went wrong.'%title)
            return redirect('/account/profile/instructor/')

    return render(request,template,page_data)


#########################
##### Module views #####

@login_required
def module_view(request,course_slug,module_slug,template='ecms_course_create_app/module_view.html'):
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,slug=module_slug,course=course)
    page_data={'module':module}
    return render(request,template,page_data)

@login_required
def module_create_view(request,course_slug,template='ecms_course_create_app/module_create_form.html'):

     #get the course
    course = get_object_or_404(Course,slug=course_slug)
    page_data={'course':course}

    if request.method=='POST':
        #handle the possible cancel
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/update/'%course_slug)
        else:
            #proper submission of the form
            form = ModuleCreateForm(request.POST)
            if form.is_valid():
                module = form.save(commit=False)
                module.course = course

                #get the title from the form
                title = form.cleaned_data['title']
                overview = form.cleaned_data['overview']

                #find if the module has a unique title
                #for the modules of this course
                if Module.is_unique_title(title,course):
                    module.slug = slugify(title)
                    module.order_id = Module.get_next_available_order_id(course)
                    module.save()
                    messages.success(request, 'Successfully created module %s.'%title)
                    return redirect('/courses/course/%s/update/'%course_slug)
                else:
                    messages.error(request, 'Course %s already has a module with name %s'%(course.title,title))
                    page_data['title_used']=title
                    page_data['overview_used']=overview
                    page_data['title']=["Title is already used by the course",]
                    return render(request,template,page_data)
            else:
                messages.error(request, 'The form has errors.')
                error_data = get_errors_map_list(form)
                print(error_data)
                page_data.update(error_data)
                return render(request,template,page_data)
    return render(request,template,page_data)



@login_required
def module_update_view(request,course_slug,module_slug,template='ecms_course_create_app/module_update_form_view.html'):
    """
    Updates a module on the database if request is POST. Otherwise serves the
    updating form
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    mtitle = module.title
    page_data={'module':module,"title_used":mtitle}
    page_data['overview_used']= module.overview

    if request.method=='POST':
        #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/update/'%(course_slug))

        #proper submission of the form
        form = ModuleCreateForm(request.POST,request.FILES)
        if form.is_valid():

            success = form.save_updated_module(module)
            if success:
                messages.success(request, 'Successfully updated module %s.'%module.title)
            else:
                messages.error(request, 'Could not updat module %s.'%module.title)
            return redirect('/courses/course/%s/update/'%(course_slug))
        else:
            messages.error(request, 'The form has errors.')
            error_data = get_errors_map_list(form)
            print(error_data)
            page_data['title_used']=request.POST.get('title','')
            page_data['overview_used']=request.POST.get('overview','')
            page_data.update(error_data)
            return render(request,template,page_data)

    return render(request,template,page_data)

@login_required
def module_delete_view(request,course_slug,module_slug,template='ecms_course_create_app/module_delete_view.html'):
    """
    Deletes the module from the database when the request is POST otherwise
    simply serves the confirmation page
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)

    page_data={"module":module}

    if request.method=='POST':
        #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/update/'%(course_slug))

        try:
            title = module.title
            module.delete()
            messages.success(request, 'Successfully deleted module %s from course.'%title)
            return redirect('/courses/course/%s/update/'%(course_slug))
        except:
            messages.success(request, 'Could not delete module from course. Something went wrong.')
            return redirect('/courses/course/%s/update/'%(course_slug))

    return render(request,template,page_data)

#@login_required
#def course_module_quiz_create_view(request,course_slug,module_slug,
	#														template='ecms_course_creator/course_module_quiz_create_form.html'):
	#return HttpResponse('course_module_quiz_create response')

#@login_required
#def course_module_quiz_update_view(request,course_slug,module_slug,quiz_id,
	#														template='ecms_course_creator/course_module_quiz_update_form.html'):
#	return HttpResponse('course_module_quiz_update response')

#@login_required
#def course_module_quiz_delete_view(request,course_slug,module_slug,quiz_id,
	#														template='ecms_course_creator/course_module_quiz_delete_form.html'):
#	return HttpResponse('course_module_quiz_delete response')

#########################
##### Lessons views #####

@login_required
def lesson_view(request,course_slug,module_slug,lesson_slug,
								template='ecms_course_create_app/lesson_view.html'):

    #course = get_object_or_404(Course,slug=course_slug)
    lesson = get_object_or_404(Lesson,slug=lesson_slug)
    text_content = render_html_content(lesson.text_content,{})
    page_data={"lesson":lesson,"text_content":text_content}
    return render(request,template,page_data)


@login_required
def lesson_create_view(request,course_slug,module_slug,
																			template='ecms_course_create_app/lesson_create_form_view.html'):
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    page_data={"module":module}
    if request.method=='POST':
        #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))
        else:
            #proper submission of the form
            form = LessonCreateForm(request.POST,request.FILES)
            if form.is_valid():

                title = form.cleaned_data['title']
                text_content = form.cleaned_data['text_content']
                meta_description = form.cleaned_data['meta_description']

                #find if the lesson has a unique title
                #for the lessons of this module
                if Lesson.is_unique_title(title,module):
                    lesson = form.save(commit=False)
                    lesson.course = course
                    lesson.module = module
                    lesson.slug = slugify(title)
                    lesson.order_id = Lesson.get_next_available_order_id(module)
                    lesson.meta_description = meta_description
                    lesson.save()
                    upload_lesson_file_images(request,course.slug,module.slug,lesson)
                    messages.success(request, 'Successfully created lesson %s.'%title)
                    return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))
                else:
                    messages.error(request, 'Module %s already has a lesson with name %s'%(module.title,title))
                    page_data['title_used']=title
                    page_data['text_content_used']=text_content
                    page_data['title']=["Title is already used by the module",]
                    return render(request,template,page_data)
            else:
                messages.error(request, 'The form has errors.')
                error_data = get_errors_map_list(form)
                print(error_data)
                page_data['title_used'] = request.POST.get('title_used','')
                page_data['text_content_used'] = request.POST.get('text_content_used','')
                page_data['meta_description_used'] = request.POST.get('meta_description','')
                page_data.update(error_data)
                return render(request,template,page_data)

    return render(request,template,page_data)




@login_required
def lesson_update_view(request,course_slug,module_slug,lesson_slug,
															        template='ecms_course_create_app/lesson_update_form_view.html'):

    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    page_data={"lesson":lesson,"title_used":lesson.title}
    page_data['meta_description_used']=lesson.meta_description
    page_data['text_content_used']=lesson.text_content

    if request.method=='POST':
        #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))

        #proper submission of the form
        form = LessonUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            lesson.text_content = form.cleaned_data['text_content']
            lesson.meta_description = form.cleaned_data['meta_description']
            lesson.save()
            update_lesson_file_images(request,course.slug,module.slug,lesson)
            upload_lesson_file_images(request,course.slug,module.slug,lesson)
            messages.success(request, 'Successfully updated lesson %s.'%lesson.title)
            return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))
        else:
            messages.error(request, 'The form has errors.')
            error_data = get_errors_map_list(form)
            print(error_data)
            page_data['meta_description_used']=request.POST.get('meta_description','')
            page_data['text_content_used']=request.POST.get('text_content','')
            page_data.update(error_data)
            return render(request,template,page_data)

    return render(request,template,page_data)



@login_required
def lesson_delete_view(request,course_slug,module_slug,lesson_slug,
																			template='ecms_course_create_app/lesson_delete_view.html'):
    """
    Deletes the lesson from the database when the request is POST otherwise
    simply serves the confirmation page
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    title = lesson.title
    page_data={"lesson":lesson}

    if request.method=='POST':
         #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))

        try:
            title = lesson.title
            lesson.delete()
            messages.success(request, 'Successfully deleted lesson %s from module.'%title)
            return redirect('/courses/course/%s/modules/%s/update/'%(course_slug,module_slug))
        except:
            messages.success(request, 'Could not delete lesson from module. Something went wrong.')
            return redirect('/courses/course/%s/modules/%s/lessons/%s/update/'%(course_slug,module_slug))

    return render(request,template,page_data)



@login_required
def lesson_create_quiz_view(request,course_slug,module_slug,
                            lesson_slug,template='ecms_course_create_app/lesson_quiz_create_form_view.html'):


    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    page_data={"lesson":lesson}

    if request.method=='POST':
         #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))

        #the form
        form = LessonQuizCreateForm(request.POST,request.FILES)
        if form.is_valid():
            #once the form is valid we can get the data
			      #from the cleaned_data dictionary

			      #number of questions the quiz has
            nquestions = form.cleaned_data['nquestions']

            #try to update the database
			      #create a quiz
            lesson_quiz = LessonQuiz(course=course,module=module,lesson=lesson)

            #we need to find how many quizes the lesson has
            lesson_quiz.quiz_id = LessonQuiz.get_next_valid_quiz_id(lesson)

            #save the lesson quiz
            lesson_quiz.save()

            errors=None
            has_errors = False
            for qidx in range(int(nquestions)):
                question = LessonQuizQuestion(quiz=lesson_quiz)
                errors = form.save_question(request,question,qidx)

                if errors != None:
                    page_data.update(errors)
                    has_errors=True

            if has_errors == True:
                messages.error(request, 'The form has errors.')
                return render(request,template,page_data)

            messages.success(request, 'Successfully created Lesson Quiz.')
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))


        else:
            messages.error(request, 'The form has errors.')
            error_data = get_errors_map_list(form)
            page_data.update(error_data)
            return render(request,template,page_data)

    else:
        form = LessonQuizCreateForm()
        page_data['form']= form
        return render(request,template,page_data)

@login_required
def lesson_quiz_update_view(request,course_slug,module_slug,
                            lesson_slug,quiz_id,template='ecms_course_create_app/lesson_quiz_update_form_view.html'):

    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    quiz   = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)

    if request.method=='POST':
         #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/lesson/%s/edit/'%(course_slug,module_slug,lesson_slug))


    page_data={"quiz":quiz,"lesson":lesson}
    return render(request,template,page_data)

@login_required
def lesson_quiz_add_new_question_view(request,course_slug,module_slug,
                                      lesson_slug,quiz_id,
                                      template='ecms_course_create_app/lesson_quiz_add_new_question_form_view.html'):
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    quiz   = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)
    page_data={"quiz":quiz,"lesson":lesson}

    if request.method=='POST':
         #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))

        form = LessonQuizAddQuestionForm(request.POST,request.FILES)
        if form.is_valid():
            #create a new question
            question = LessonQuizQuestion(quiz=quiz)
            errors = form.save_question(request,question,0)
            has_errors = False
            if errors:
                messages.error(request, 'The form has errors.')
                return render(request,template,page_data)

            messages.success(request, 'Successfully added new question to Lesson Quiz.')
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))

        else:
            messages.error(request, 'The form has errors.')
            error_data = get_errors_map_list(form)
            page_data.update(error_data)
            return render(request,template,page_data)

    return render(request,template,page_data)

@login_required
def lesson_quiz_delete_view(request,course_slug,module_slug,
                            lesson_slug,quiz_id,
                            template='ecms_course_create_app/lesson_quiz_delete_view.html'):
    """

    Deletes the quiz from the database when the request is POST otherwise
    simply serves the confirmation page
    """
    course = get_object_or_404(Course,slug=course_slug)
    module = get_object_or_404(Module,course=course,slug=module_slug)
    lesson = get_object_or_404(Lesson,module=module,slug=lesson_slug)
    quiz   = get_object_or_404(LessonQuiz,course=course,module=module,lesson=lesson,quiz_id=quiz_id)
    page_data={"quiz":quiz,"lesson":lesson}

    if request.method=='POST':
         #handle the possible cancel we redirect to the module view
        if "cancel" in request.POST:
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))

        try:
            quiz.delete()
            messages.success(request, 'Successfully deleted lesson quiz.')
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))
        except:
            messages.success(request, 'Could not delete lesson quiz. Something went wrong.')
            return redirect('/courses/course/%s/modules/%s/lessons/%s/view/'%(course_slug,module_slug,lesson_slug))

    return render(request,template,page_data)


@login_required
def course_module_section_activity_create_view(request,course_slug,module_slug,section_slug,
																					template='ecms_course_creator/course_module_section_activity_create_form.html'):
	return HttpResponse('course_module_section_activity_create response')

@login_required
def course_module_section_activity_update_view(request,course_slug,module_slug,section_slug,activity_id,
																					template='ecms_course_creator/course_module_section_activity_update_form.html'):
	return HttpResponse('course_module_section_activity_update response')

@login_required
def course_module_section_activity_delete_view(request,course_slug,module_slug,section_slug,activity_id,
																					template='ecms_course_creator/course_module_section_activity_delete_form.html'):
	return HttpResponse('course_module_section_activity_delete response')


@login_required
def course_module_section_quiz_create_view(request,course_slug,module_slug,section_slug,
																					template='ecms_course_creator/course_module_section_quiz_create_form.html'):
	return HttpResponse('course_module_section_quiz_create response')

@login_required
def course_module_section_quiz_update_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms_course_creator/course_module_section_quiz_update_form.html'):
	return HttpResponse('course_module_section_quiz_update response')

@login_required
def course_module_section_quiz_delete_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms_course_creator/course_module_section_quiz_delete_form.html'):
	return HttpResponse('course_module_section_quiz_delete response')
























