from django.conf.urls import url
from . import views

urlpatterns = [
	# post views
	url(r'^$', 
			views.contact_index, 
			name='contact_index'),

	url(r'^success/$',
			views.contact_success,
			name='contact_success'),

	url(r'^hire/$',
			views.contact_hire,
			name='contact_hire'),

	url(r'^hire-success/$',
			views.contact_hire_success,
			name='contact_hire_success'),

]
