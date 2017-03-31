from django.db import models

from utils_app.models import ActiveMixin
from ecms_course_create_app.models import Course

# Create your models here.
class NotifyCourseStart(ActiveMixin):

	email = models.EmailField(null=False)
	name = models.CharField(max_length=200, null=False)
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
