#Django imports
from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#we need WebTest to test for form submisions
from django_webtest import WebTest

#local imports
from . import views
from . forms import ContactForm

# Create your tests here.
class ContactPageTest(WebTest):

	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_root_url_resolves_to_contact_index(self):
		"""
			Test that the root of the site resolves to the correct view function.
		"""
		found = resolve('/contact/')
		self.assertEqual(found.func,views.contact_index)

	def test_root_url_response_is_200(self):
		"""
			Test that the index view returns 200 OK and that.
		"""
		response = self.client.get('/contact/')
		self.assertTemplateUsed(response,'contact/contact.html')
		self.assertEqual(response.status_code,200)

	def test_valid_contact_title(self):
		"""
			Test: The contact page has a title
		"""
		response = self.client.get('/contact/') 
		self.assertIn(b'<title>Ustdy-Contact</title>',response.content)

	def test_empty_contact_form_error(self):
		"""
			Test: An invalid form is submmited
		"""
		page = self.app.get('/contact/')
		
		page = page.forms[1].submit()
		self.assertContains(page, "Message failed. The form has errors. Please correct the errors below.")

	def test_valid_contact_form(self):
		"""
			Test: A valid contact form is valid.
		"""
		form = ContactForm({'contact_name':"Alex",'contact_email':"s@sth.com",'content':"This is content"})
		self.assertTrue(form.is_valid())

	def test_invalid_contact_form(self):
		"""
			Test: An empty contact form is invalid.
		"""
		form = ContactForm({})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors, {
        						 'contact_name': ['This field is required.'],
        						 'contact_email': ['This field is required.'],
          					 'content': ['This field is required.'],})

	def test_valid_contact_form(self):
		"""
			Test: A valid contact form should submit and redirect the user
			to /contact/success/
		"""
		#ge the page
		#page = self.app.get('/contact/')
		response = self.client.post("/contact/", {'contact_name':'something',
																							'contact_email':'s@s.com',
																							'content':'This is content'})
		self.assertRedirects(response, expected_url='/contact/success/',status_code=302)


class ContactHirePageTest(WebTest):

	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_hire_url_resolves_to_contact_hire(self):
		"""
			Test: The url  resolves to the correct view function.
		"""
		found = resolve('/contact/hire/')
		self.assertEqual(found.func,views.contact_hire)

	def test_hire_url_response_is_200(self):
		"""
			Test: The url view returns 200 OK.
		"""
		response = self.client.get('/contact/hire/')
		self.assertTemplateUsed(response,'contact/contact_hire.html')
		self.assertEqual(response.status_code,200)

	def test_hire_success_url_resolves_to_contact_hire_success(self):
		"""
			Test: The url  resolves to the correct view function.
		"""
		found = resolve('/contact/hire-success/')
		self.assertEqual(found.func,views.contact_hire_success)

	def test_hire_success_url_response_is_200(self):
		"""
			Test: The url view returns 200 OK.
		"""
		response = self.client.get('/contact/hire-success/')
		self.assertTemplateUsed(response,'contact/contact_hire_success.html')
		self.assertEqual(response.status_code,200)
		
	
		


	
