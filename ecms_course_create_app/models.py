
import os
import io

#Django
from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.files.storage import FileSystemStorage


#third party libraries
from taggit.managers import TaggableManager

#local imports
from ustdy.settings import COURSES_URL,COURSES_ROOT
from utils_app.models import ActiveMixin,UniqueTitleMixin,OverviewMixin,CreationModificationDateMixin,\
NonUniqueTitleMixin, Language, Level,ActiveManager,DeliveryMode,SubtitlesLanguage
from utils_app.models import QuestionType



def upload_course_syllabus(instance,filename):
    return COURSES_URL+instance.slug+'/'+filename


def upload_course_img(instance,filename):
    return COURSES_URL+instance.slug+'/'+filename


def upload_lesson_img(instance,filename):
    course_slug = instance.lesson.course.slug
    module_slug = instance.lesson.module.slug
    lesson_slug = instance.lesson.slug
    usr_id = instance.lesson.module.course.owner.id
    folder = COURSES_URL+'/'+str(usr_id)+'/'+course_slug+'/'+module_slug+'/'+lesson_slug+'/assets'
    return folder


class Subject(UniqueTitleMixin):
    """
		Class that represents an educational subject within u-study elearncms
    """

    class Meta:
        db_table = 'subject'
        ordering = ('title',)



class CourseInfoMixin(ActiveMixin):

    #the starting date of the course
    start_date = models.CharField(max_length=200,null=False)

    #effort paid by the student in h/per week
    effort = models.CharField(max_length=200,null=False)

    #number of weeks the course approximately will last
    duration = models.CharField(max_length=200,null=False)

    #meta description of what the course is about
    meta_description = models.CharField(max_length=200,null=False)

    #meta author of the course
    meta_author = models.CharField(max_length=200,null=False)

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


class Module(NonUniqueTitleMixin,OverviewMixin,CreationModificationDateMixin,ActiveMixin):
    """
        Class tha models a module or chapter of a given course
    """
    course = models.ForeignKey(Course,related_name='course_modules')

    #the default manager we need this since we have an ActiveManager
    objects = models.Manager()

    #manager for active also called published courses
    published = ActiveManager()

    #the starting date of the course
    order_id = models.IntegerField(null=False)

    class Meta:
        db_table='module'
        ordering=('order_id',)


    @staticmethod
    def is_unique_title(title,course):
        modules = Module.objects.all().filter(title=title,course=course)
        print(modules)
        if len(modules) == 0:
            return True
        return False

    @staticmethod
    def get_next_available_order_id(course):
        modules = Module.objects.all().filter(course=course).count()
        return modules+1

class Lesson(NonUniqueTitleMixin,CreationModificationDateMixin,ActiveMixin):
    """
    Class that models a specific lesson
    """

    #the course this lesson belongs to
    course = models.ForeignKey(Course,related_name='course_lessons',on_delete=models.CASCADE)

    #the module this lesson belongs to
    module = models.ForeignKey(Module,related_name='module_lessons',on_delete=models.CASCADE)

    #the default manager we need this since we have an ActiveManager
    objects = models.Manager()

    #manager for active also called published courses
    published = ActiveManager()

    #the starting date of the course
    order_id = models.IntegerField(null=False)

    #the content of the lesson
    text_content = models.TextField(null=False)

    #meta description of what the course is about
    meta_description = models.CharField(max_length=200,null=False)

    class Meta:
        db_table='lesson'
        ordering=('order_id',)


    def __str__(self):
        return self.course.title+"-"+self.module.title+"-"+self.title


    @staticmethod
    def is_unique_title(title,module):
        lessons = Lesson.objects.all().filter(title=title,module=module)

        if len(lessons) == 0:
            return True
        return False

    @staticmethod
    def get_next_available_order_id(module):
        lessons = Lesson.objects.all().filter(module=module).count()
        return lessons+1

    def get_next_order_id(self):
        return Lesson.get_next_available_order_id(self.module)



class LessonImg(CreationModificationDateMixin,ActiveMixin):
    """
    Class for storing any image files a Lesson object may have
    """

    lesson =  models.ForeignKey(Lesson,on_delete=models.CASCADE,null=True,related_name='lesson_file_imgs')
    file = models.ImageField(upload_to = upload_lesson_img, max_length=2000, null=True,blank=True)

    class Meta:
        db_table = 'lesson_file_imgs'



class LessonQuiz(CreationModificationDateMixin,ActiveMixin):
    """
    Class that handles the quiz for a Lesson
    """
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,related_name='course_module_lesson_quizes')
    module = models.ForeignKey(Module,on_delete=models.CASCADE,null=True,related_name='module_lesson_quizes')
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,null=True,related_name='lesson_quizes')

    #the id of the quiz local to the lesson based on
    #the number of quizes the lesson has
    quiz_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Lesson Quiz"
        verbose_name_plural = "Lesson Quizes"
        db_table = 'lesson_quizes'
        ordering=['quiz_id',]


    def get_n_questions(self):
        return LessonQuizQuestion.objects.all().filter(quiz=self).count()

    @staticmethod
    def get_next_valid_quiz_id(lesson):
        return (LessonQuiz.objects.all().filter(course=lesson.course,module=lesson.module,lesson=lesson).count()+1)



class QuizQuestionMixin(CreationModificationDateMixin,ActiveMixin):
    """
    Abstract class (i.e. a table is not created for this model) for modelling
    a quiz question
    """

    CHOICES=[(1,1),(2,2),(3,3),(4,4),(5,5)]
    choices = models.IntegerField(choices=CHOICES,null=False)

    #the question
    question = models.TextField(null=False)

    #the explanation. There may  not be an explanation
    explanation = models.TextField(null=True)

    #the correct answer. This may be a list of comma separated integers
	  #or simply an input.
    correct_answer = models.CharField(max_length=500,null=False)

    class Meta:
        abstract=True

class LessonQuizQuestion(QuizQuestionMixin):

    """
    Class that models a quiz question
    """

    quiz = models.ForeignKey(LessonQuiz,on_delete=models.CASCADE,null=False,related_name='lesson_quiz_questions')
    qtype = models.ForeignKey(QuestionType,on_delete=models.CASCADE,null=False)

    #the default manager we need this since we have an ActiveManager
    objects = models.Manager()

    #manager for active quizes
    published = ActiveManager()

    #the id of the question local to the quiz
    order_id = models.IntegerField(null=False)

    class Meta:
        verbose_name = "Lesson Quiz Question"
        verbose_name_plural = "Lesson Quiz Questions"
        db_table = "lesson_quiz_questions"
        ordering = ('order_id',)


    def is_radio_type(self):
        if self.qtype.type == 'Radio' :
            print("Type is radio")
            return True
        return False


class LessonQuizQuestionOption(CreationModificationDateMixin,ActiveMixin):

    #the quiz question the option belongs to
    lesson_quiz_question=models.ForeignKey(LessonQuizQuestion,on_delete=models.CASCADE,null=False,related_name='lesson_quiz_question_options')


    #the question
    context = models.CharField(max_length=500,null=False)

    #the id of the quiz local to the lesson based on
    #the number of quizes the lesson has
    order_id = models.IntegerField(null=False)


    #the default manager we need this since we have an ActiveManager
    objects = models.Manager()

    #manager for active quizes
    published = ActiveManager()

    class Meta:
        verbose_name = "Lesson Quiz Question Option"
        verbose_name_plural = "Lesson Quiz Questions Options"
        db_table = "lesson_quiz_question_options"
        ordering=('order_id',)

    @staticmethod
    def get_next_valid_order_id(option):
        return (LessonQuizQuestionOption.objects.all().filter(lesson_quiz_question=option.lesson_quiz_question).count()+1)

class LessonQuizQuestionImg(CreationModificationDateMixin,ActiveMixin):
    """
    Class for storing any image files for a quiz question of  Lesson object
    """

    question =  models.ForeignKey(LessonQuizQuestion,on_delete=models.CASCADE,null=True,
                                  related_name='lesson_quiz_question_file_imgs')
    quiz = models.ForeignKey(LessonQuiz,on_delete=models.CASCADE,null=False)
    file = models.ImageField(upload_to = upload_lesson_img, max_length=2000, null=True,blank=True)

    class Meta:
        verbose_name = "Lesson Quiz Question Image"
        db_table = 'lesson_quiz_question_file_imgs'







