from django.conf.urls import url
from . import views
urlpatterns = [

#general views
	
	url(r'^$', 
			views.tests_index, 
			name='tests_index'),
]
