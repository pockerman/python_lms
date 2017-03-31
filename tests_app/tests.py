#Django imports
from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#we need WebTest to test for form submisions
from django_webtest import WebTest

#local imports
from . import views

class TestsIndexPageTest(WebTest):
	
	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_root_url_resolves_to_library_index(self):
		"""
			Test: The root  url resolves to the correct view.
		"""
		found = resolve('/tests/')
		self.assertEqual(found.func,views.tests_index)

	def test_root_url_response_is_200(self):
		"""
			Test: The view returns 200 OK.
		"""
		response = self.client.get('/tests/')
		self.assertTemplateUsed(response,'tests/tests_index.html')
		self.assertEqual(response.status_code,200)
