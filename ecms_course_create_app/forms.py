__author__ = 'david'
import os

from django import forms
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify

from ustdy.settings import COURSES_ROOT
from utils_app.models import QuestionType
from utils_app.models import Language
from utils_app.models import Level
from utils_app.models import DeliveryMode
from utils_app.models import SubtitlesLanguage

from .models import Subject
from .models import Course
from .models import Module
from .models import Lesson
from .models import LessonImg
from .models import LessonQuiz
from .models import LessonQuizQuestionOption

def get_all_subjects():
    return Subject.objects.all()




class CourseUpdateForm(forms.Form):

    subject =forms.ChoiceField(choices=get_all_subjects,label="subject")
    overview = forms.CharField(widget=forms.Textarea,label='overview',required=True)
    start_date = forms.CharField(max_length=200,label='startdate')
    effort = forms.CharField(max_length=200,label='effort')
    duration = forms.CharField(max_length=200,label="duration")
    fees = forms.FloatField(initial=0.0,label='fees', required=True)
    level = forms.ChoiceField(choices=Level.CHOICES,widget=forms.Select(),required=True)
    language = forms.ChoiceField(choices=Language.CHOICES,widget=forms.Select(),required=True)
    delivery_mode = forms.ChoiceField(choices=DeliveryMode.CHOICES,widget=forms.Select(),required=True)
    video_subs =forms.ChoiceField(choices=SubtitlesLanguage.CHOICES,label="videosubs")
    meta_author = forms.CharField(max_length=200,label='metaauthor')
    meta_description = forms.CharField(max_length=200,label='metadescription')
    active =forms.BooleanField(initial=True,label='active')




class ModuleCreateForm(ModelForm):
    """
    Class that handles the creation of a Model
    """
    title=forms.CharField(max_length=200)
    overview = forms.CharField(widget=forms.Textarea)

    class Meta:
        model=Module
        fields=['title','overview',]

    def save_updated_module(self,module):
        """
        Updates the given instance module
        """
        title = self.cleaned_data['title']
        overview = self.cleaned_data['overview']
        mtitle = module.title

        if title == mtitle:
            module.overview = overview
            module.save()
            return True
        else:
            if Module.is_unique_title(title,module.course):
                module.title = title
                module.slug = slugify(title)
                module.overview = overview
                module.save()
                return True
            return False

class LessonCreateForm(ModelForm):
    """
    Class that handles the creation of a lesson
    """
    title=forms.CharField(max_length=200,label="title",required=True)
    text_content = forms.CharField(widget=forms.Textarea,label="text_content",required=True)
    meta_description = forms.CharField(max_length=200,label="meta_description",required=True)

    class Meta:
        model=Lesson
        fields=['title','text_content','meta_description']






class LessonUpdateForm(ModelForm):
    """
    Class to update the contents of a lesson. Only, text content currently
    can be changed.
    """
    text_content = forms.CharField(widget=forms.Textarea)
    meta_description = forms.CharField(max_length=200)

    class Meta:
		    model=Lesson
		    fields=['text_content','meta_description']


def upload_lesson_file_images(request,course_slug,module_slug,lesson):
    """
    Upload images for the given lesson
    """
    imgs = request.FILES.getlist('img',None)

    if imgs != None:
        folder = str(request.user.id)+'/'+course_slug+'/'+module_slug+'/'+lesson.slug+'/assets'
        location = os.path.join(COURSES_ROOT, folder)
        fs = FileSystemStorage(location=location)
        try:
            os.makedirs(os.path.join(COURSES_ROOT, folder))
        except:
            print("Could not create folder")

        for img in imgs:
            file = img
            lesson_file_img = LessonImg(lesson=lesson)
            filename = fs.save(file.name, file)
            lesson_file_img.file=location+'/'+filename
            lesson_file_img.save()


def update_lesson_file_images(request,course_slug,module_slug,lesson):
    """
    Update the image files of the given lesson object
    """
    replace_img =  request.FILES.getlist('replace_img',None)

    if replace_img != None:
        folder = str(request.user.id)+'/'+course_slug+'/'+module_slug+'/'+lesson.slug+'/assets'
        location = os.path.join(COURSES_ROOT, folder)
        fs = FileSystemStorage(location=location)

        #try to create the directory if it doesn't exist
        try:
            os.makedirs(os.path.join(COURSES_ROOT, folder))
        except:
            print("Could not create folder")

        #get all the  images for this lesson
        lesson_file_imgs =lesson.lesson_file_imgs.all()

        #if we have less images then update the len(section_file_imgs)
        #and then create new images
        if len(lesson_file_imgs) < len(replace_img):

            #update only the first len(section_file_imgs)
            for imgidx in range(len(lesson_file_imgs)):
                dbfile = lesson_file_imgs[imgidx]
                img = replace_img[imgidx]
                filename = fs.save(img.name, img)
                dbfile.file = location+'/'+filename
                dbfile.save()

            #create new images
            counter = 0
            for newimg	in replace_img:
                if counter >= len(lesson_file_imgs):
                    file=newimg
                    new_section_file_img = LessonImg(lesson=lesson)
                    filename = fs.save(file.name, file)
                    new_section_file_img.file=location+'/'+filename
                    new_section_file_img.save()
                counter=counter+1

        elif len(lesson_file_imgs) == len(replace_img):
            #update all section_file_imgs
            for imgidx in range(len(lesson_file_imgs)):
                dbfile = lesson_file_imgs[imgidx]
                img = replace_img[imgidx]
                filename = fs.save(img.name, img)
                dbfile.file = location+'/'+filename
                dbfile.save()
        else:
            #update only the first len(request.FILES.getlist('replace_img'))
            for imgidx in range(len(replace_img)):
                dbfile = lesson_file_imgs[imgidx]
                img = replace_img[imgidx]
                filename = fs.save(img.name, img)
                dbfile.file = location+'/'+filename
                dbfile.save()


class LessonQuizQuestionFormBase(forms.Form):
    """
    Base class for handling creation of quizes
    """

    #number of questions the quiz may have
    NQ = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

    #the choices of the questions
    QCHOICES = [("none-q-type","Select question type"),("radio","Radio"),("checkbox","Checkbox")]

    #number of options for Radio and checkbox questions
    NOPTS=[(1,1),(2,2),(3,3),(4,4),(5,5)]


    #number of options if checkbox or radio question
    q1nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q1typeopts-1',choices=NOPTS)

	  #question1: A quiz must have at least one question
    q1type = forms.ChoiceField(widget=forms.Select,required=True,label='q1type',choices=QCHOICES)

	  #the question that is asked
    q1 = forms.CharField(widget=forms.Textarea,label='q1',required=True)

	  #the correct answer
    caq1 = forms.CharField(max_length=200,label='caq1',required=True)

	  #explanation for the question. This is not a required field
    explq1 = forms.CharField(widget=forms.Textarea,label='explq1',required=False)

	  #flag indicating if the question is active
    active1 = forms.BooleanField(initial=True,label='active1',required=True)

	  #a photo
    photo1 = forms.ImageField(required=False,label='photo1')


    def save_question(self,request,question_object,qidx):
        """
        Save the question in the database
        """

        qidx_str = str(qidx+1)
        question_type = self.cleaned_data['q'+qidx_str+'type']
        q = self.cleaned_data['q'+qidx_str]
        option='None'
        option_list=[]
        errors={}
        if question_type=='radio' or question_type=='checkbox':

            #we have options find out how many
            if 'q'+qidx_str+'typeopts-'+qidx_str in self.cleaned_data.keys():
                nopts = self.cleaned_data['q'+qidx_str+'typeopts-'+qidx_str]
            else:
                nopts = request.POST['q'+qidx_str+'typeopts-'+qidx_str]

            for optidx in range(int(nopts)):
                optidx_str = str( optidx+1)
                print("For option: %s context is: %s"%(optidx_str,request.POST['opt-'+optidx_str+'-q-'+qidx_str]))
                option_list.append(request.POST['opt-'+optidx_str+'-q-'+qidx_str])
        else:
            errors['question_type'] = "No question type have been selected"

        expl='No explanation'
        #check if we have an explanation
        if 'explq'+qidx_str in self.cleaned_data.keys():
            expl = self.cleaned_data['explq'+qidx_str]

        if question_type=='radio':
            type = get_object_or_404(QuestionType,type='Radio')
            question_object.qtype = type
        elif question_type=='checkbox':
            type =get_object_or_404(QuestionType,type='CheckBox')
            question_object.qtype = type


        #whether the question is active
        active = self.cleaned_data['active'+qidx_str]
        correct_answer = self.cleaned_data['caq'+qidx_str]

        #now we add the question

        question_object.question=q
        question_object.explanation=expl
        question_object.correct_answer=correct_answer
        question_object.active=active
        question_object.choices = len(option_list)
        question_object.save()

        #now that we have saved the question
        #we create the options
        for option in option_list:
            print("Adding option: ",option)
            option_object = LessonQuizQuestionOption(lesson_quiz_question=question_object,context=option)
            order_id = LessonQuizQuestionOption.get_next_valid_order_id(option_object)
            print("Order id is: ",order_id)
            option_object.order_id = order_id
            option_object.save()




class LessonQuizAddQuestionForm(LessonQuizQuestionFormBase):
    """
    Class that handles the creation of a new question in a given
    lesson quiz
    """
    pass



class LessonQuizCreateForm(LessonQuizQuestionFormBase):
    """
    Class that handles the creation of quiz for a lesson
    """

    nquestions = forms.ChoiceField(widget=forms.Select,required=True,label='nquestions',choices=LessonQuizQuestionFormBase.NQ)

    #========================================================================
    #optional fields

    q2type = forms.ChoiceField(widget=forms.Select,required=False,label='q2type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q12nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q2typeopts-2',choices=LessonQuizQuestionFormBase.NOPTS)
    q2 = forms.CharField(widget=forms.Textarea,label='q2',required=False)
    caq2 = forms.CharField(max_length=200,label='caq2',required=False)
    explq2 = forms.CharField(widget=forms.Textarea,label='explq2',required=False)
    active2 = forms.BooleanField(initial=True,label='active2',required=False)
    photo2 = forms.ImageField(required=False,label='photo2')

    q3type = forms.ChoiceField(widget=forms.Select,required=False,label='q3type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q3nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q3typeopts-3',choices=LessonQuizQuestionFormBase.NOPTS)
    q3 = forms.CharField(widget=forms.Textarea,label='q3',required=False)
    caq3 = forms.CharField(max_length=200,label='caq3',required=False)
    explq3 = forms.CharField(widget=forms.Textarea,label='explq3',required=False)
    active3 = forms.BooleanField(initial=True,label='active3',required=False)
    photo3 = forms.ImageField(required=False,label='photo3')

    q4type = forms.ChoiceField(widget=forms.Select,required=False,label='q4type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q4nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q4typeopts-4',choices=LessonQuizQuestionFormBase.NOPTS)
    q4 = forms.CharField(widget=forms.Textarea,label='q4',required=False)
    caq4 = forms.CharField(max_length=200,label='caq4',required=False)
    explq4 = forms.CharField(widget=forms.Textarea,label='explq4',required=False)
    active4 = forms.BooleanField(initial=True,label='active4',required=False)
    photo4 = forms.ImageField(required=False,label='photo4')

    q5type = forms.ChoiceField(widget=forms.Select,required=False,label='q5type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q5nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q5typeopts-5',choices=LessonQuizQuestionFormBase.NOPTS)
    q5 = forms.CharField(widget=forms.Textarea,label='q5',required=False)
    caq5 = forms.CharField(max_length=200,label='caq5',required=False)
    explq5 = forms.CharField(widget=forms.Textarea,label='explq5',required=False)
    active5 = forms.BooleanField(initial=True,label='active5',required=False)
    photo5 = forms.ImageField(required=False,label='photo5')

    q6type = forms.ChoiceField(widget=forms.Select,required=False,label='q6type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q6nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q6typeopts-6',choices=LessonQuizQuestionFormBase.NOPTS)
    q6 = forms.CharField(widget=forms.Textarea,label='q6',required=False)
    caq6 = forms.CharField(max_length=200,label='caq6',required=False)
    explq6 = forms.CharField(widget=forms.Textarea,label='explq6',required=False)
    active6 = forms.BooleanField(initial=True,label='active6',required=False)
    photo6 = forms.ImageField(required=False,label='photo6')

    q7type = forms.ChoiceField(widget=forms.Select,required=False,label='q7type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q7nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q7typeopts-7',choices=LessonQuizQuestionFormBase.NOPTS)
    q7 = forms.CharField(widget=forms.Textarea,label='q7',required=False)
    caq7 = forms.CharField(max_length=200,label='caq7',required=False)
    explq7 = forms.CharField(widget=forms.Textarea,label='explq7',required=False)
    active7 = forms.BooleanField(initial=True,label='active7',required=False)
    photo7 = forms.ImageField(required=False,label='photo7')

    q8type = forms.ChoiceField(widget=forms.Select,required=False,label='q8type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q8nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q8typeopts-8',choices=LessonQuizQuestionFormBase.NOPTS)
    q8 = forms.CharField(widget=forms.Textarea,label='q8',required=False)
    caq8 = forms.CharField(max_length=200,label='caq8',required=False)
    explq8 = forms.CharField(widget=forms.Textarea,label='explq8',required=False)
    active8 = forms.BooleanField(initial=True,label='active8',required=False)
    photo8 = forms.ImageField(required=False,label='photo8')

    q9type = forms.ChoiceField(widget=forms.Select,required=False,label='q9type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q9nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q9typeopts-9',choices=LessonQuizQuestionFormBase.NOPTS)
    q9 = forms.CharField(widget=forms.Textarea,label='q9',required=False)
    caq9 = forms.CharField(max_length=200,label='caq9',required=False)
    explq9 = forms.CharField(widget=forms.Textarea,label='explq9',required=False)
    active9 = forms.BooleanField(initial=True,label='active9',required=False)
    photo9 = forms.ImageField(required=False,label='photo9')

    q10type = forms.ChoiceField(widget=forms.Select,required=False,label='q10type',choices=LessonQuizQuestionFormBase.QCHOICES)
    q10nopts = forms.ChoiceField(widget=forms.Select,required=False,label='q10typeopts-10',choices=LessonQuizQuestionFormBase.NOPTS)
    q10 = forms.CharField(widget=forms.Textarea,label='q10',required=False)
    caq10 = forms.CharField(max_length=200,label='caq10',required=False)
    explq10 = forms.CharField(widget=forms.Textarea,label='explq10',required=False)
    active10 = forms.BooleanField(initial=True,label='active10',required=False)
    photo10 = forms.ImageField(required=False,label='photo10')

    #def save_question(self,request,question_object,qidx):

     #   qidx_str = str(qidx+1)
     #   question_type = self.cleaned_data['q'+qidx_str+'type']
     #   q = self.cleaned_data['q'+qidx_str]
     #   option='None'
     #   option_list=[]
     #   errors={}
     #   if question_type=='radio' or question_type=='checkbox':

            #we have options find out how many
     #       if 'q'+qidx_str+'typeopts-'+qidx_str in self.cleaned_data.keys():
    #            nopts = self.cleaned_data['q'+qidx_str+'typeopts-'+qidx_str]
    #        else:
    #            nopts = request.POST['q'+qidx_str+'typeopts-'+qidx_str]

    #        for optidx in range(int(nopts)):
    #            optidx_str = str( optidx+1)
    #            option_list.append(request.POST['opt-'+optidx_str+'-q-'+qidx_str])
    #    else:
    #        errors['question_type'] = "No question type have been selected"

    #    expl='No explanation'
        #check if we have an explanation
    #    if 'explq'+qidx_str in self.cleaned_data.keys():
    #        expl = self.cleaned_data['explq'+qidx_str]

    #    if question_type=='radio':
    #        type = get_object_or_404(QuestionType,type='Radio')
    #        question_object.qtype = type
    #    elif question_type=='checkbox':
    #        type =get_object_or_404(QuestionType,type='CheckBox')
    #        question_object.qtype = type


        #whether the question is active
    #    active = self.cleaned_data['active'+qidx_str]
     #   correct_answer = self.cleaned_data['caq'+qidx_str]

        #now we add the question

    #    question_object.question=q
    #    question_object.explanation=expl
    #    question_object.correct_answer=correct_answer
     #   question_object.active=active
    #    question_object.choices = len(option_list)
     #   question_object.save()

        #now that we have saved the question
        #we create the options
    #    for option in option_list:
     #       option_object = LessonQuizQuestionOption(lesson_quiz_question=question_object,context=option)
    #        option_object.save()


        #save any images related to the question



