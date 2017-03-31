from django.conf.urls import url
from ustdy.settings import ECMS_TMP
from . import views

urlpatterns = []

if ECMS_TMP == True:

	urlpatterns=[ url(r'^all/$',
												 views.ecms_courses_tmp_view, 
													name='ecms_courses_tmp_view'),
								
								url(r'^catalog/$',
										views.ecms_courses_catalog_view,
										name='ecms_courses_catalog_view'),

								url(r'^catalog/subject/(?P<subject_slug>[-\w]+)/$',
										views.ecms_courses_catalog_subject_view,
										name='ecms_courses_catalog_subject_view'),


								url(r'^course/(?P<course_slug>[-\w]+)/overview/$',
										views.course_overview,
										name='course_overview'),

								url(r'^course/(?P<course_slug>[-\w]+)/notify-me/$',
										views.notify_me_course_start,
										name='notify_me_course_start'),

								url(r'^course/(?P<course_slug>[-\w]+)/notify-me/success/$',
										views.notify_me_course_start_success,
										name='notify_me_course_start_success'),
	
	]

else:

	urlpatterns = [

#general views
	url(r'^all/$', 
			views.ecms_courses_tmp_view, 
			name='ecms_courses_tmp_view'),

	url(r'^all/$', 
			views.ecms_index, 
			name='ecms_index'),

	url(r'^subject/(?P<subject_slug>[-\w]+)/all/$',
			views.ecms_index_subject,
			name='ecms_index_subject'),

	url(r'^course/(?P<course_slug>[-\w]+)/overview/$',
			views.course_overview,
			name='course_overview'),

	url(r'^course/(?P<course_slug>[-\w]+)/resourses/$',
			views.course_resourses_view,
			name='course_resourses_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/syllabus/$',
			views.course_syllabus_view,
			name='course_syllabus_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/$',
			views.course_module_view,
			name='course_module_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/$',
			views.course_module_section_view,
			name='course_module_section_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/start/$',
			views.course_module_quiz_start_view,
			name='course_module_quiz_start_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/do/$',
			views.course_module_quiz_do_view,
			name='course_module_quiz_do_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/start/$',
			views.course_module_section_quiz_start_view,
			name='course_module_section_quiz_start_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/quiz/(?P<quiz_id>\d+)/do/$',
			views.course_module_section_quiz_do_view,
			name='course_module_section_quiz_do_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_slug>[-\w]+)/section/(?P<section_slug>[-\w]+)/activity/$',
			views.course_module_section_activity_view,
			name='course_module_section_activity_view'),

	url(r'^course/(?P<course_slug>[-\w]+)/student/(?P<student_id>\d+)/progress/$',
			views.course_student_progress_view,
			name='course_student_progress_view'),

	#url(r'^search/$',
	#		views.search_view,
	#		name='search_view'),

#create views

	#url(r'^course/create/$',
	#	 	views.course_create_view,
	#		name='course_create_view'),

	#url(r'^course/edit/(?P<course_slug>[-\w]+)/$',
	#		views.course_edit_view,
	#		name='course_edit_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/$',
	#		views.course_module_update_view,
	#		name='course_module_update_view'),

	#url(r'^(?P<pk>\d+)/delete/$',
	#		views.CourseDeleteView.as_view(),
	#		name='course_delete_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/update/$',
	#		views.module_content_list_view,
	#		name='module_content_list_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/edit_overview_and_title/$',
	#		views.module_edit_overview_and_title,
	#		name='module_edit_overview_and_title'),
	
	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/add_section/$',
	#		views.module_add_section_view,
	#		name='module_add_section_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/section/(?P<section_id>\d+)/edit_section/$', 
	#		views.module_edit_section_view,
	#		name='module_edit_section_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/section/(?P<section_id>\d+)/preview_section/$', 	
	#		views.module_section_preview,
	#		name='module_section_preview'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/create_quiz/$',
	#		views.module_add_quiz_view,
	#		name='module_add_quiz_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/quiz/(?P<quiz_id>\d+)/update/$',
	#		views.module_update_quiz_view,
	#		name='module_update_quiz_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/quiz/(?P<quiz_id>\d+)/preview/$',
	#		views.module_quiz_preview_view,
	#		name='module_quiz_preview_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/quiz/(?P<quiz_id>\d+)/start_preview/$',
	#		views.module_quiz_start_preview_view,
	#		name='module_quiz_start_preview_view'),

	#student views

	#url(r'^enroll-course/(?P<pk>\d+)/$',
	#		views.enroll_student_to_course,
	#		name='enroll_student_to_course'),

	#url(r'^course/(?P<course_slug>[-\w]+)/start/$',
	#		views.student_course_view,
	#		name='student_course_view'),

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/$',
	#		views.student_course_detail_module_view,
	#		name='student_course_detail_module_view'),

	#url(r'^course/(?P<pk>\d+)/resources/$',
	#		views.course_resources_view,
	#		name='course_resources_view'),

	

	#url(r'^course/(?P<course_slug>[-\w]+)/module/(?P<module_id>\d+)/quiz_start/(?P<quiz_id>\d+)/$',
	#		views.student_course_module_quiz_start_view,
	#		name='student_course_module_quiz_start_view'),

	

	#url(r'^course/(?P<course_slug>[-\w]+)/student_delete/$',
	#		views.delete_student_from_course_view,
	#		name='delete_student_from_course_view'),

	]
