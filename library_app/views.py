import operator
import functools
#import itertools
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

#paginator is not used at the moment
#from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

#local imports
from ustdy.settings import LIBRARY_URL,LIBRARY_ROOT
from ustdy.website_settings import site_full_name_team

from .models import LibBook,LibSubject
from .forms import LibSearchForm

def get_subjects_with_count():
	subjects_all = LibSubject.objects.all()
	subjects=[]

	for sub in subjects_all:
		notes_count = LibBook.published.filter(subject=sub).count()
		subjects.append((sub,notes_count))
	return subjects

def get_meta_tags():
	return {"meta_author_content":site_full_name_team,
					"meta_description_content":"lecture notes for science, engineering and computational sciences,\
							ΣΗΜΕΙΩΣΕΙΣ ΓΙΑ ΠΑΝΕΠΙΣΤΗΜΙΟ ΚΑΙ ΠΟΛΥΤΕΧΝΕΙΟ","meta_keywords_content":"lecture notes,science,engineering,programming,ΣΗΜΕΙΩΣΕΙΣ,ΠΑΝΕΠΙΣΤΗΜΙΟ,ΠΟΛΥΤΕΧΝΕΙΟ",}
	

# Create your views here.
def library_index(request,template="library/library_index.html"):

	subjects=get_subjects_with_count()
	page_data = get_meta_tags()
	page_data.update({"selecteducation":True,"selectlibrary":True,"subjects":subjects})

	books=[]
	if 'query' in request.GET:
		form = LibSearchForm(request.GET)
		if form.is_valid():
			#get the query
			cd = form.cleaned_data
			query = request.GET.get('query')
			books = LibBook.published.all()
			query_list = query.split()
			
			results_title = LibBook.published.filter(functools.reduce(operator.or_,( Q(title__icontains=q) for q in query_list)) |
																							 functools.reduce(operator.or_,( Q(tags__name__in=query_list) for q in query_list))
																							)
			#get the distinct books
			books = results_title.distinct()
			page_data["books"] = books
			page_data["search_used"] = True
		
	return render(request,template,page_data)

def library_index_subject(request,subject_slug,template="library/library_index.html"):
	subject = get_object_or_404(LibSubject,slug=subject_slug)
	subjects=get_subjects_with_count()
	books = LibBook.published.all().filter(subject=subject)
	page_data = get_meta_tags()
	page_data.update({"selecteducation":True,"selectlibrary":True,
										"subjects":subjects,"subject_title":subject.title,"books":books,"search_used":True})
	return render(request,template,page_data)

def library_book_tag_search(request,tag_slug,template="library/library_index.html"):
	subjects=get_subjects_with_count()
	books = LibBook.published.filter(tags__slug__in=[tag_slug])
	page_data = get_meta_tags()
	page_data.update({"selecteducation":True,"selectlibrary":True,
										"subjects":subjects,"books":books,"search_used":True})
	return render(request,template,page_data)
	

def pdf_view(request,pk,doc_slug):
	doc = get_object_or_404(LibBook,id=pk,slug=doc_slug)

	docfile = doc.filename.url 
	filename = docfile.split('/')
	filename = filename[len(filename)-1]
	
	with open(LIBRARY_ROOT+doc.subject.slug+'/'+doc.slug+'/'+filename, 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition'] = 'filename='+filename 
		return response
	
	
	
