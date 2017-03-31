from django.db import models

#third party imports
from taggit.managers import TaggableManager

#local imports
from utils_app.models import ActiveMixin,NonUniqueTitleMixin,CreationModificationDateMixin,Language,\
UniqueTitleMixin,ActiveManager

from ustdy.settings import LIBRARY_URL,LIBRARY_ROOT

# Create your models here.

def upload_library_book(instance,filename):
	return LIBRARY_URL+instance.subject.slug+'/'+instance.slug+'/'+filename

class LibSubject(UniqueTitleMixin):
	"""
		Class that represents an educational subject within u-study library
	"""
	class Meta:
		db_table = 'lib_subject'
		ordering = ('title',)

class LibBook(ActiveMixin,NonUniqueTitleMixin,CreationModificationDateMixin):

	#syllabus for the course
	filename = models.FileField(upload_to=upload_library_book, max_length=2000,null=True)

	#the subject id
	subject = models.ForeignKey(LibSubject,on_delete=models.CASCADE)

	#the language of the course
	language = models.ForeignKey(Language,on_delete=models.CASCADE)

	#tags for the course
	tags = TaggableManager()

	#the default manager we need this since we have an ActiveManager
	objects = models.Manager()

	#manager for active also called published courses
	published = ActiveManager()

	class Meta:
		db_table='lib_books'
		ordering=('title',)
