from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.core.urlresolvers import reverse
from django.utils.text import force_text

from .models import  Subject
from .models import  Course
from .models import  Module
from .models import  Lesson
from .models import  LessonImg
from .models import  LessonQuiz
from .models import  LessonQuizQuestion
from .models import  LessonQuizQuestionOption
from .models import  LessonQuizQuestionImg


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['title', 'subject', 'created']
	list_filter = ['created', 'subject']
	search_fields = ['title', 'overview']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
	list_display = ['title', 'created']
	list_filter = ['created',]
	search_fields = ['title',]
	prepopulated_fields = {'slug': ('title',)}


@admin.register(LessonImg)
class LessonImgAdmin(admin.ModelAdmin):
    pass


class LessonImgInline(admin.TabularInline):
    model = LessonImg
    max_num=10
    fk_name = "lesson"



def get_quiz_preview(obj):
    if obj.pk:  # if object has already been saved and has a primary key, show picture preview
        return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
            src=obj.picture.url,
            title=obj.title,
        )
    return ("(choose a picture and save and continue editing to see the preview)")

get_quiz_preview.allow_tags = True
get_quiz_preview.short_description = ("Picture Preview")


class LessonQuizInline(admin.StackedInline):
    model = LessonQuiz
    show_change_link = True
    fields = ["get_edit_link",]
    readonly_fields = ["get_edit_link",]

    def get_edit_link(self, obj=None):

        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return """<a href="{url}">{text}</a>""".format(
                url=url,
                text=("Edit this %s separately") % obj._meta.verbose_name,
            )
        return ("(You need to first create a quiz save it and then continue editing to create a link)")

    get_edit_link.short_description = ("Edit link")
    get_edit_link.allow_tags = True

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'created','module','course']
    readonly_fields = ('available_order_id',)
    list_filter = ['created',]
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
    inlines=[LessonImgInline,LessonQuizInline,]

    def available_order_id(self, instance):
        if instance == None:
            return 0
        lessons = Lesson.objects.all().filter(module=instance.module).count()
        return lessons+1

class LessonQuizQuestionInline(admin.StackedInline):
    model = LessonQuizQuestion
    #fields = ["get_edit_link", get_quiz_preview]
    #readonly_fields = ["get_edit_link", get_quiz_preview]

@admin.register(LessonQuiz)
class LessonQuizAdmin(admin.ModelAdmin):
    list_display = ['course','module','lesson']
    inlines=[LessonQuizQuestionInline,]


@admin.register(LessonQuizQuestionImg)
class LessonQuizQuestionImgAdmin(admin.ModelAdmin):
    pass


class LessonQuizQuestionImgInline(admin.TabularInline):
    model = LessonQuizQuestionImg
    max_num=10
    #fk_name = "lesson"

@admin.register(LessonQuizQuestionOption)
class LessonQuizQuestionOptionAdmin(admin.ModelAdmin):
    pass

class LessonQuizQuestionOptionInline(admin.TabularInline):
    model = LessonQuizQuestionOption
    #max_num=10




@admin.register(LessonQuizQuestion)
class LessonQuizQuestionAdmin(admin.ModelAdmin):
    inlines=[LessonQuizQuestionImgInline, LessonQuizQuestionOptionInline,]

#@admin.register(LessonQuizQuestionImg)
#class LessonQuizImgAdmin(admin.ModelAdmin):
#    pass

#class LessonQuizQuestionImgInline(admin.TabularInline):
 #   model = LessonQuizQuestionImg
#    max_num=10
    #fk_name = "lesson"



#@admin.register(LessonQuizQuestion)
#class LessonQuizQuestionAdmin(admin.ModelAdmin):
#    inlines=[LessonQuizQuestionImgInline,]

#class LessonQuizQuestionInline(admin.TabularInline):
#    model = LessonQuizQuestion
 #   max_num=10
    #fk_name = "lesson"

#@admin.register(LessonQuiz)
#class LessonQuizAdmin(admin.ModelAdmin):
#    """
#    Class that handles the administration of quizes for a lesson
#    """
#    list_display = ['course','module','lesson']
#    inlines=[LessonQuizQuestionInline,]










#@admin.register(LessonQuizQuestion)
#class LessonQuizQuestionAdmin(admin.ModelAdmin):
#    list_display = ['lesson.title', 'created',]



