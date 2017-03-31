
from unittest import skip

#Django imports
from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#we need WebTest to test for form submisions
from django_webtest import WebTest

#local imports
from . import views
from . forms import LoginForm,UserRegistrationForm

class AccoutAppTestBase(WebTest):
	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def page_title(self,title,url):
		response = self.client.get(url) 
		self.assertIn(title,response.content)
		

class LogInPageTest(AccoutAppTestBase):
	
	"""
		Test the login page
	"""
	
	def test_root_url_resolves_to_account_index(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/login/')
		self.assertEqual(found.func,views.user_login)

	def test_root_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/login/')
		self.assertTemplateUsed(response,'account/login.html')
		self.assertEqual(response.status_code,200)

	def test_valid_title(self):
		"""
			Test: The page has a title
		"""
		self.page_title(b'<title>Ustdy Log In</title>','/account/login/')
		

	def test_valid_login_form(self):
		"""
			Test: A valid login form is valid.
		"""
		form = LoginForm({'username':"Alex",'password':"sthcool"})
		self.assertTrue(form.is_valid())
		

	def test_invalid_login_form(self):
		"""
			Test: An empty login form is invalid.
		"""
		form = LoginForm({})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors, {
        						 'username': ['This field is required.'],
        						 'password': ['This field is required.'],})

	
	def test_empty_login_form_error(self):
		"""
			Test: An invalid form is submmited
		"""
		page = self.app.get('/account/login/')
		page = page.forms[1].submit()
		#self.fail("Finish the test. We should have a message here saying that the user credentials are invalid")
		self.assertContains(page, "Your username or password did not match. Please try again.")

class LogOutPageTest(AccoutAppTestBase):
	"""
		Unit tests for log out page
	"""

	def test_user_logout_url_resolves_to_user_logout(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/logout/')
		self.assertEqual(found.func,views.user_logout)

	def test_user_logout_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/logout/')

		#we don't have a user logged in so we redirect to login page
		#self.assertTemplateUsed(response,'account/login.html')
		self.assertEqual(response.status_code,302)
	

class RegisterPageTest(AccoutAppTestBase):
	"""
		Unit tests for registration page
	"""

	def test_register_url_resolves_to_account_register(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/register/')
		self.assertEqual(found.func,views.user_register)

	

	def test_register_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/register/')
		self.assertTemplateUsed(response,'account/register.html')
		self.assertEqual(response.status_code,200)

	def test_valid_page_title(self):
		"""
			Test: The page has a title
		"""
		self.page_title(b'<title>Ustdy-SignUp</title>','/account/register/')
	
	
	def test_valid_registration_form(self):
		"""
			Test: A valid login form is valid.
		"""
		form = UserRegistrationForm({'password2':'123','password':'123','username':'Alex'})
		self.assertTrue(form.is_valid())

	
	def test_invalid_registration_form(self):
		"""
			Test: An empty login form is invalid.
		"""
		form = UserRegistrationForm({})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors, {
        						 'password2': ['This field is required.'],
       						   'username': ['This field is required.'],
										 'password': ['This field is required.'],})
		self.fail("This test must also check that first_name, last_name,email fields are supplied by the user")

	def test_empty_form_error(self):
		"""
			Test: An invalid form is submmited
		"""
		page = self.app.get('/account/register/')
		page = page.forms[1].submit()
		self.assertContains(page, "Registration failed. The form has errors. Please correct the errors below.")

	def test_success_register_url_resolves_to_success_registration(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/success_register/Alex/')
		self.assertEqual(found.func,views.success_registration)

	def test_register_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/success_register/Alex/')
		self.assertTemplateUsed(response,'account/register_done.html')
		self.assertEqual(response.status_code,200)

class TestChangeResetPasswordPage(AccoutAppTestBase):

	"""
		Unit tests for change/reset password
	"""

	def test_reset_password_url_resolves_to_my_password_reset(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/password-reset/')
		self.assertEqual(found.func,views.my_password_reset)

	def test_resert_password_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/password-reset/')
		self.assertTemplateUsed(response,'account/password_reset_form.html')
		self.assertEqual(response.status_code,200)

	def test_change_password_url_resolves_to_my_password_change(self):		
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/password/change/')
		self.assertEqual(found.func,views.my_password_change)

	def test_change_password_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/account/password/change/')
		self.fail("Finish The Test")
		#I think this test needs a logged in user
		#self.assertTemplateUsed(response,'account/password_change_form.html')
		#self.assertEqual(response.status_code,200)


class TestAccountProfile(AccoutAppTestBase):
	"""
		Unit tests for profile access and edit
	"""

	def test_profile_url_resolves_to_user_profile(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/profile/')
		self.assertEqual(found.func,views.user_profile)

	def test_profile_edit_url_resolves_to_user_profile_edit(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/account/profile/edit/')
		self.assertEqual(found.func,views.user_profile_edit)
	



	
		
	



