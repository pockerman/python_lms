from django.contrib import admin
from .models import Language
from .models import Level
from .models import DeliveryMode
from .models import SubtitlesLanguage
from .models import QuestionType

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

@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
	list_display = ['type', ]
