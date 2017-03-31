
import os
import io

#Django
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage

#third party libraries
from taggit.managers import TaggableManager

#local imports
from ustdy.settings import COURSES_URL,COURSES_ROOT
from utils_app.models import ActiveMixin,UniqueTitleMixin,OverviewMixin,CreationModificationDateMixin,\
NonUniqueTitleMixin, Language, Level,ActiveManager,DeliveryMode,SubtitlesLanguage

#from utils_app.utilities import upload_section_file

def upload_course_syllabus(instance,filename):
	return COURSES_URL+instance.slug+'/'+filename

	#return COURSES_URL+instance.slug+'/'+filename 

def upload_course_img(instance,filename):
	return COURSES_URL+instance.slug+'/'+filename


class Subject(UniqueTitleMixin):
	"""
		Class that represents an educational subject within u-study elearncms
	"""

	class Meta:
		db_table = 'subject'
		ordering = ('title',)

class CourseInfoMixin(ActiveMixin):

	#he starting date of the course 
	start_date = models.CharField(max_length=200,null=False)

	#effort paid by the student in h/per week
	effort = models.CharField(max_length=200,null=False)

	#number of weeks the course approximately will last
	duration = models.CharField(max_length=200,null=False)

	#the fees for the course
	fees = models.FloatField(null=False,default=0.0)

	#syllabus for the course
	syllabus_file = models.FileField(upload_to=upload_course_syllabus, max_length=2000,null=True)

	#photo for the course
	photo_file = models.ImageField(upload_to = upload_course_img, max_length=2000,null=True)

	#the name+extension of the photo_file
	photo_file_name = models.CharField(max_length=200,null=False)

	class Meta:
		abstract=True

class Course(UniqueTitleMixin,CreationModificationDateMixin,OverviewMixin,CourseInfoMixin):

	#the owner of the course
	owner = models.ForeignKey(User,on_delete=models.CASCADE)

	#the subject id
	subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

	#the language of the course
	language = models.ForeignKey(Language,on_delete=models.CASCADE)

	#the level of the course
	level = models.ForeignKey(Level,on_delete=models.CASCADE)

	#the delivery mode of the course
	delivery_mode = models.ForeignKey(DeliveryMode,on_delete=models.CASCADE)

	#the video subtitles
	video_subs =models.ForeignKey(SubtitlesLanguage,on_delete=models.CASCADE)

	#tags for the course
	tags = TaggableManager()

	#the default manager we need this since we have an ActiveManager
	objects = models.Manager()

	#manager for active also called published courses
	published = ActiveManager()

	class Meta:
		db_table='course'
		ordering=('title',)

	#the absolute url leads to the
	#overview of the course
	def get_absolute_url(self):
		return reverse('ecms_course_create_app:course_overview',args=[self.slug])
