from django.conf.urls import url
from . import views
urlpatterns = [

#general views
	
	url(r'^course/create/$', 
			views.course_create_view, 
			name='course_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/update/$',
			views.course_update_view,
			name='course_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/delete/$',
			views.course_delete_view,
			name='course_delete_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/modules/create/$', 
			views.course_modules_create_view, 
			name='course_modules_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/update/$',
			views.course_module_update_view,
			name='course_module_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/delete/$',
			views.course_module_delete_view,
			name='course_module_delete_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/create/$',
			views.course_module_quiz_create_view,
			name='course_module_quiz_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/update/$',
			views.course_module_quiz_update_view,
			name='course_module_quiz_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/delete/$',
			views.course_module_quiz_delete_view,
			name='course_module_quiz_delete_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/sections/create/$', 
			views.course_module_section_create_view, 
			name='course_module_section_create_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/update/$',
			views.course_module_section_update_view,
			name='course_module_section_update_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/delete/$',
			views.course_module_section_delete_view,
			name='course_module_section_delete_view'),


	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/activity/create/$', 
			views.course_module_section_activity_create_view, 
			name='course_module_section_activity_create_view'),

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






	#url(r'^course/(?P<course_slug>[-\w]+)/overview/$',
	#		views.course_overview,
	#		name='course_overview'),

	#url(r'^course/(?P<course_slug>[-\w]+)/resourses/$',
	#		views.course_resourses_view,
	#		name='course_resourses_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/syllabus/$',
	#		views.course_syllabus_view,
	#		name='course_syllabus_view'),
]
