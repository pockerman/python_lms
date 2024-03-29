from django.shortcuts import render
from ustdy.website_settings import site_full_name_team


# Create your views here.
def ustdy_index(request,template="ustdy/index.html"):
	page_data = {"show_carousel":True,
							 "meta_description_content":"online science engineering and computational sciences courses, lecture notes, programming, online courses development and hosting, ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ,ΦΟΙΤΗΤΙΚA ΜΑΘΗΜΑΤΑ, ΕΚΠΟΝΗΣΗ ΕΡΓΑΣΙΩΝ",
							 "meta_author_content":site_full_name_team,
							 "meta_keywords_content":"on-line courses, lecture notes, \
                                        programming,assignements,ΦΟΙΤΗΤΙΚΟ ΦΡΟΝΤΙΣΤΗΡΙΟ,ΦΟΙΤΗΤΙΚA ΜΑΘΗΜΑΤΑ, ΕΚΠΟΝΗΣΗ ΕΡΓΑΣΙΩΝ, ΠΡΟΓΡΑΜΜΑΤΙΣΜΟΣ"}


	return render(request,template,page_data)

def privacy_policy_view(request,template="ustdy/privacy.html"):
	page_data = {"meta_author_content":site_full_name_team,
							 "meta_description_content":site_full_name_team+" Privacy Policy",
							 "meta_keywords_content":"privacy, policy"}
	return render(request,template,page_data)

def about_view(request,template="ustdy/about.html"):
	page_data = {"meta_author_content":site_full_name_team,
							 "meta_description_content":"About "+site_full_name_team,
							 "meta_keywords_content":"about, "+site_full_name_team}

	return render(request,template,page_data)

def jobs_view(request,template="ustdy/jobs.html"):
	page_data = {"meta_author_content":site_full_name_team,
							 "meta_description_content":site_full_name_team+" Carreers",
							 "meta_keywords_content":"carrers, jobs, "+site_full_name_team}

	return render(request,template,page_data)

def development_view(request,template="ustdy/lms_dev.html"):
	page_data = {"meta_author_content":site_full_name_team,
							 "meta_description_content":site_full_name_team+" LMS development, serious games development",
							 "meta_keywords_content":"LMS development, serious game development",
							 "selectservices":True,"selectdevelopment":True}
	return render(request,template,page_data)

def host_your_courses_view(request,template="ustdy/host_your_courses.html"):
	page_data = {"meta_author_content":site_full_name_team,
							 "meta_description_content":"On-line courses hosting, science and engineering courses hosting",
							 "meta_keywords_content":"on-line courses hosting, science courses hosting",
							 "selectservices":True,"selecthosting":True}

	return render(request,template,page_data)

def handle404(request,template="404.html"):
	return render(request,template,{})

def handle500(request,template="500.html"):
	return render(request,template,{})



