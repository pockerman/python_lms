from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from opensim_elearncms.models import Course



class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	photo = models.ImageField(upload_to='users',null=True)
	about = models.TextField(null=True)

	class Meta:
		db_table='user_account_profile'

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
