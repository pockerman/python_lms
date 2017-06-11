from django.shortcuts import render
from ustdy.website_settings import site_full_name_team


# Create your views here.
def tests_index(request,template="tests/tests_index.html"):
	page_data= {"meta_author_content":site_full_name_team,
							"meta_description_content":" online techinical tests on various scientific fields",
							"meta_keywords_content":"online  tests, c++ programming test, java programming test, statistics test, algorithms test",
							"selecteducation":True,"selecttests":True}
	return render(request,template,page_data)
