from django.shortcuts import render

# Create your views here.
# Create your views here.
def tests_index(request,template="tests/tmp/tests_index.html"):
	page_data= {"selecteducation":True,"selecttests":True}
	return render(request,template,page_data)


