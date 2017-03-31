#Django imports
from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#local imports
from . import views

class UstudyAppTestBase(TestCase):
	"""
		Base class for unit testing of ustudy_app
	"""

	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def url_resolves(self,url,name):
		found = resolve(url)
		self.assertEqual(found.func,name)

	def response_is_200(self,url,template):
		response = self.client.get(url)
		self.assertTemplateUsed(response,template)
		self.assertEqual(response.status_code,200)	
	
#=======================================================================
#=======================================================================
class IndexPageTest(UstudyAppTestBase):

	def test_root_url_resolves_to_ustdy_index(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/',views.ustdy_index)
		

	def test_root_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/','ustdy/index.html')
		
#=======================================================================
#=======================================================================
class PolicyPrivacyTest(UstudyAppTestBase):

	def test_policy_url_resolves_to_privacy_policy_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/privacy/',views.privacy_policy_view)
		

	def test_policy_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/privacy/','ustdy/privacy.html')
		
#=======================================================================
#=======================================================================
class AboutTest(UstudyAppTestBase):

	def test_about_url_resolves_to_about_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/about/',views.about_view)
		

	def test_about_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/about/','ustdy/about.html')

#=======================================================================
#=======================================================================	
	
class JobsTest(UstudyAppTestBase):

	def test_jobs_url_resolves_to_about_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/jobs/',views.jobs_view)
		

	def test_jobs_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/jobs/','ustdy/jobs.html')

#=======================================================================
#=======================================================================

class ServicesDevelopmentTest(UstudyAppTestBase):		

	def test_services_lms_development_url_resolves_to_lms_development_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/services/development/',views.development_view)
		

	def test_services_lms_development_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/services/development/','ustdy/lms_dev.html')

#=======================================================================
#=======================================================================
		
class ServicesHostTest(UstudyAppTestBase):

	def test_host_your_courses_url_resolves_to_host_your_courses_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		self.url_resolves('/services/host-courses/',views.host_your_courses_view)
		

	def test_host_your_courses_url_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		self.response_is_200('/services/host-courses/','ustdy/host_your_courses.html')
		

	
