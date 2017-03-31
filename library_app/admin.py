from django.contrib import admin
from .models import LibSubject, LibBook

# Register your models here.

@admin.register(LibSubject)
class LibSubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}

@admin.register(LibBook)
class LibBookAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}
	#inlines = [ModuleInline]
