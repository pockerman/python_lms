from django.contrib import admin
from .models import Language, Level,DeliveryMode,SubtitlesLanguage

# Register your models here.
# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display = ['language', ]

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
	list_display = ['level', ]

@admin.register(DeliveryMode)
class DeliveryModeAdmin(admin.ModelAdmin):
	list_display = ['mode', ]

@admin.register(SubtitlesLanguage)
class SubtitlesLanguageAdmin(admin.ModelAdmin):
	list_display = ['language', ]
