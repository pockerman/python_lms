from django.conf.urls import url
from . import views
urlpatterns = [

#########################
##### Course views #####

    url(r'^course/(?P<course_slug>[-\w]+)/start/$',
        views.course_view,
        name="course_view"),
	
	  url(r'^course/create/$',
			  views.course_create_view,
			  name='course_create_view'),

	  url(r'^course/(?P<course_slug>[-\w]+)/update/$',
			  views.course_update_view,
			  name='course_update_view'),

    url(r'^course/(?P<course_slug>[-\w]+)/delete/$',
        views.course_delete_view,
        name='course_delete_view'),

#########################
##### Module views #####

    url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/view/$',
        views.module_view,
        name="module_view"),

	url(r'^course/(?P<course_slug>[-\w]+)/modules/create/$', 
			views.module_create_view,
			name='module_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/update/$',
			views.module_update_view,
			name='module_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/delete/$',
			views.module_delete_view,
			name='module_delete_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/create/$',
	#		views.course_module_quiz_create_view,
	#		name='course_module_quiz_create_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/update/$',
	#		views.course_module_quiz_update_view,
	#		name='course_module_quiz_update_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/delete/$',
	#		views.course_module_quiz_delete_view,
	#		name='course_module_quiz_delete_view'),

#########################
##### Lesson views #####

    url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/view/$',
        views.lesson_view,
        name='lesson_view'),

    url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/lesson/create/$',
        views.lesson_create_view,
        name='lesson_create_view'),

	  url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/update/$',
			  views.lesson_update_view,
			  name='lesson_update_view'),

	  url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/delete/$',
			views.lesson_delete_view,
			name='lesson_delete_view'),

#########################
##### Lesson quiz views #####

    url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/quiz/create/$',
			  views.lesson_create_quiz_view,
			  name='lesson_create_quiz_view'),

    url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/quiz/(?P<quiz_id>[0-9]+)/update/$',
			  views.lesson_quiz_update_view,
			  name='lesson_quiz_update_view'),

    url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/quiz/(?P<quiz_id>[0-9]+)/questions/add/$',
			  views.lesson_quiz_add_new_question_view,
			  name='lesson_quiz_add_new_question_view'),


	  url(r'^course/(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/lessons/(?P<lesson_slug>[-\w]+)/quiz/(?P<quiz_id>[0-9]+)/delete/$',
			views.lesson_quiz_delete_view,
			name='lesson_quiz_delete_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/activity/(?P<activity_id>\d+)/update/$',
			views.course_module_section_activity_update_view,
			name='course_module_section_activity_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/activity/(?P<activity_id>\d+)/delete/$',
			views.course_module_section_activity_delete_view,
			name='course_module_section_activity_delete_view'),


		url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/quiz/create/$', 
			views.course_module_section_quiz_create_view, 
			name='course_module_section_quiz_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/update/$',
			views.course_module_section_quiz_update_view,
			name='course_module_section_quiz_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/delete/$',
			views.course_module_section_quiz_delete_view,
			name='course_module_section_quiz_delete_view'),

]
