from django.conf.urls import url
from . import views

urlpatterns = [
	# post views
	url(r'^$',
			views.ustdy_index,
			name='ustdy_index'),

	#url(r'^privacy/$',
	#		views.privacy_policy_view,
	#		name='privacy_policy_view'),

	url(r'^about/$',
			views.about_view,
			name='about_view'),

	#url(r'^jobs/$',
	#		views.jobs_view,
	#		name='jobs_view'),

	url(r'^services/development/$',
			views.development_view,
			name='development_view'),

	url(r'^services/host-courses/$',
			views.host_your_courses_view,
			name='host_your_courses_view'),


]
