from django.conf.urls import url
#from django.contrib.auth.views import password_change_done
from . import views

urlpatterns = [

	url(r'^login/$', 
			views.user_login, 
			name='user_login'),

	#url(r'^instructor_login/$',
	#		views.instructor_user_login,
	#		name='instructor_user_login'),

	url(r'^register/$', 
			views.user_register, 
			name='user_register'),

	url(r'^success_register/(?P<first_name>\w+)/$',
			views.success_registration,
			name='success_registration'),

	#url(r'^instructor_register/$',
	#		views.instructor_register,
	#		name='instructor_register'),

	url(r'^logout/$',
			views.user_logout,
			name='user_logout'),

	url(r'^profile/edit/$', 
			views.user_profile_edit, 
			name='user_profile_edit'),

	url(r'^profile/$',
			views.user_profile,
			name='user_profile'),

	

	# change password urls
	url(r'^password/change/$',
			views.my_password_change,
			name='my_password_change'),

	url(r'^password/change/done/$',
			views.my_password_change_done, 
			name='my_password_change_done'),

	# restore password urls
	url(r'^password-reset/$',
			views.my_password_reset,
			name='my_password_reset'),

	url(r'^password-reset/done/$',
			views.my_password_reset_done,
			name='my_password_reset_done'),

	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
			views.my_password_reset_confirm,
			name='my_password_reset_confirm'),

	url(r'^password-reset/complete/$',
			views.my_password_reset_complete,
			name='my_password_reset_complete'),

]
