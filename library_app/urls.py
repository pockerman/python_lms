from django.conf.urls import url
from . import views
urlpatterns = [

#general views
	
	url(r'^$', 
			views.library_index, 
			name='library_index'),

	url(r'^subject/(?P<subject_slug>[-\w]+)/$',
										views.library_index_subject,
										name='library_index_subject'),

	url(r'^(?P<pk>\d+)/(?P<doc_slug>[-\w]+)/$',
			views.pdf_view,
			name='pdf_view'),

	url(r'^(?P<tag_slug>[-\w]+)/$',
			views.library_book_tag_search,
			name='library_book_tag_search'),

]
