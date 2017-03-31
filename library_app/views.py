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

from .models import LibBook,LibSubject
from .forms import LibSearchForm

def get_subjects_with_count():
	subjects_all = LibSubject.objects.all()
	subjects=[]

	for sub in subjects_all:
		notes_count = LibBook.published.filter(subject=sub).count()
		subjects.append((sub,notes_count))
	return subjects
	

# Create your views here.
def library_index(request,template="library/library_index.html"):

	subjects=get_subjects_with_count()
	page_data={"selecteducation":True,"selectlibrary":True,"subjects":subjects}

	books=[]
	if 'query' in request.GET:
		form = LibSearchForm(request.GET)
		if form.is_valid():
			#get the query
			cd = form.cleaned_data
			query = request.GET.get('query')
			books = LibBook.published.all()
			query_list = query.split()
			
			results_title = LibBook.published.filter(
																								functools.reduce(operator.or_,
																																	( Q(title__icontains=q) for q in query_list)) |
																								functools.reduce(operator.or_,
																																	( Q(tags__name__in=query_list) for q in query_list))
																							)
			#get the distinct books
			books = results_title.distinct()
			page_data["books"] = books
			page_data["search_used"] = True

	
	#paginator = Paginator(books, 7)
	#page = request.GET.get('page')
	#try:
	#	books_on_page = paginator.page(page)
	#except PageNotAnInteger:
		# If page is not an integer deliver the first page
	#	books_on_page = paginator.page(1)
	#except EmptyPage:
		# If page is out of range deliver last page of results
	#	books_on_page = paginator.page(paginator.num_pages)	

	#page_data['page'] = page	
			
	return render(request,template,page_data)

def library_index_subject(request,subject_slug,template="library/library_index.html"):
	subject = get_object_or_404(LibSubject,slug=subject_slug)
	subjects=get_subjects_with_count()
	books = LibBook.published.all().filter(subject=subject)
	return render(request,template,{"selecteducation":True,"selectlibrary":True,
																	"subjects":subjects,"subject_title":subject.title,"books":books,
																	"search_used":True})

def library_book_tag_search(request,tag_slug,template="library/library_index.html"):
	subjects=get_subjects_with_count()
	books = LibBook.published.filter(tags__slug__in=[tag_slug])
	return render(request,template,{"selecteducation":True,"selectlibrary":True,
																	"subjects":subjects,"books":books,"search_used":True})
	

def pdf_view(request,pk,doc_slug):
	doc = get_object_or_404(LibBook,id=pk,slug=doc_slug)

	docfile = doc.filename.url 
	filename = docfile.split('/')
	filename = filename[len(filename)-1]
	
	with open(LIBRARY_ROOT+doc.subject.slug+'/'+doc.slug+'/'+filename, 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		response['Content-Disposition'] = 'filename='+filename #some_file.pdf'
		return response
	
	
	
