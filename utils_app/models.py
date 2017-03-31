from django.db import models
from django.utils.timezone import now as timezone_now

# Create your models here.
class CreationModificationDateMixin(models.Model):
	"""
		abstarct base class that provides  creation and modification date and time
		fields to derived models
	"""

	#when the instance of the model was created
	created = models.DateTimeField(auto_now_add=True,editable=False,)

	#when the instance of the model was updated
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class UniqueTitleMixin(models.Model):
	"""
		Abstract base class for models with a unique title
	"""

	title = models.CharField(max_length=200,unique=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class NonUniqueTitleMixin(models.Model):

	"""
		Abstact base class for models with non-unique title
	"""
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=False,default="non")

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class OverviewMixin(models.Model):
	"""
		Abstract base class for models requiring an overview
	"""
	#the overview of the course
	overview = models.TextField(null=False)

	class Meta:
		abstract=True

class ActiveMixin(models.Model):
	"""
		Abstract base class for models that require an active field
	"""
	#flag indicating if the  model is active. Default is True
	active =models.BooleanField(default=True)

	class Meta:
		abstract=True

	def is_active(self):

		if self.active==1:
			return True
		return False

class Language(models.Model):
	"""
		class that models the languages supported by u-study
	"""
	CHOICES=[('English','English'),('Greek','Greek'),('English/Greek','English/Greek')]
	language=models.CharField(max_length=100,choices=CHOICES,null=False,unique=True)

	class Meta:
		db_table='languages'

	def __str__(self):
		return self.language

class Level(models.Model):
	"""
		class that models the level of a course
	"""
	CHOICES=[('Introductory','Introductory'),('Intermediate','Intermediate'),('Advanced','Advanced')]
	level=models.CharField(max_length=100,choices=CHOICES,null=False,unique=True)
	class Meta:
		db_table='course_level'

	def __str__(self):
		return self.level

class DeliveryMode(models.Model):
	"""
		class that models how a course is delivered
	"""
	CHOICES=[('Text','Text'),('Video','Video'),('Video/Text','Video/Text')]
	mode=models.CharField(max_length=100,choices=CHOICES,null=False,unique=True)
	class Meta:
		db_table='delivery_mode'

	def __str__(self):
		return self.mode

class SubtitlesLanguage(models.Model):
	"""
		class that models subtitles
	"""
	CHOICES=[('No','No'),('English','English'),('Greek','Greek'),('English/Greek','English/Greek')] 
	language=models.CharField(max_length=100,choices=CHOICES,null=False,unique=True)
	class Meta:
		db_table='subtitles_languages'

	def __str__(self):
		return self.language
	
	

class ActiveManager(models.Manager):
	"""
	class for models an active manager
	"""
	def get_queryset(self):
		return super(ActiveManager, self).get_queryset().filter(active=True)
