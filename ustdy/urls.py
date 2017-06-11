"""ustdy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler500


from ustdy_app import views as main_views
from .settings import ACCOUNT_TMP


#the handler for 404 pages 
handler404 = main_views.handle404
handler500 = main_views.handle500

urlpatterns = [
    url(r'^my-private-admin/', admin.site.urls),
		
		url(r'^',
				include('ustdy_app.urls',
								 namespace='ustdy_app',
								 app_name='ustdy_app')),

		url(r'^contact/',
				include('contact_app.urls',
								 namespace='contact_app',
								 app_name='contact_app')),

		url(r'^courses/',
				include('ecms_app.urls',
								namespace='ecms_app',
								app_name='ecms_app')),

		url(r'^courses/',
				include('ecms_course_create_app.urls',
								namespace='ecms_course_create_app',
								app_name='ecms_course_create_app')),		

		url(r'^library/',
				include('library_app.urls',
								namespace='library_app',
								app_name='library_app')),

		url(r'^tests/',
				include('tests_app.urls',
								namespace='tests_app',
								app_name='tests_app')),

]

if ACCOUNT_TMP==False:
	#the account_app is properly used
		urlpatterns.append(url(r'^account/',
													include('account_app.urls',
													namespace='account_app',
													app_name='account_app')),)

urlpatterns += static(settings.STATIC_URL)#,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.COURSES_URL,document_root=settings.COURSES_ROOT)
