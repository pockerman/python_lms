from django.shortcuts import render

from ustdy.website_settings import site_index_title,site_about_title

# Create your views here.
def ustdy_index(request,template="ustdy/index.html"):
	page_data = {"show_carousel":True,}
	return render(request,template,page_data)

def privacy_policy_view(request,template="ustdy/privacy.html"):
	page_data = {}
	return render(request,template,page_data)

def about_view(request,template="ustdy/about.html"):
	page_data = {}
	return render(request,template,page_data)

def jobs_view(request,template="ustdy/jobs.html"):
	page_data = {}
	return render(request,template,page_data)

def development_view(request,template="ustdy/lms_dev.html"):
	page_data = {"selectservices":True,"selectdevelopment":True}
	return render(request,template,page_data)

def host_your_courses_view(request,template="ustdy/host_your_courses.html"):
	page_data = {"selectservices":True,"selecthosting":True}
	return render(request,template,page_data)

def handle404(request,template="404.html"):
	return render(request,template,{})

def handle500(request,template="500.html"):
	return render(request,template,{})



