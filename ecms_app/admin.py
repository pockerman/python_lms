from django.contrib import admin
from .models import NotifyCourseStart

@admin.register(NotifyCourseStart)
class NotifyCourseStartAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'course','active']
	
