#python imports
import unittest

#Django imports
from django.test import LiveServerTestCase

#third party imports:Selenium
from selenium import webdriver

#application import
#from ustdy.website_settings import site_index_title

class URLTest(LiveServerTestCase):
	"""
		Test class for all URLs in Ustdy. This test
		class simply confirms that a user does not see
		a 404 page for a valid used url
	"""

	@classmethod
	def setUpClass(cls):
		super(URLTest, cls).setUpClass()
		cls.browser = webdriver.Firefox()
		cls.browser.delete_all_cookies()

	@classmethod
	def tearDownClass(cls):
		super(URLTest, cls).tearDownClass()
		cls.browser.quit()

	def page_title_is(self,url,name):
		"""
			Tests that the title of the page for the given url is the given name
		"""
		self.browser.get(self.live_server_url+url)
		#make sure that the title of the page is name
		self.assertEqual(name,self.browser.title)

	def test_can_access_root_page(self):
		"""
			Test: John can access the index page
		"""
		self.page_title_is('/','Ustudy Home')

#testing navigation URLS

	def test_can_access_development_page(self):
		"""
			Test: John can access the development page
		"""
		self.page_title_is('/services/development/','Ustudy Development')

	def test_can_access_host_page(self):
		"""
			Test: John can access the host page
		"""
		self.page_title_is('/services/host-courses/','Ustudy Host Courses')

	def test_can_access_courses_page(self):
		"""
			Test: John can access the courses page
		"""
		self.page_title_is('/courses/all/','Ustudy Courses')

	def test_can_access_library_page(self):
		"""
			Test: John can access the library page
		"""
		self.page_title_is('/library/','Ustudy Library')

	def test_can_access_test_and_flash_cards_page(self):
		"""
			Test: John can access the tests and flash cards page
		"""
		self.page_title_is('/tests/','Ustudy Tests & Flash Cards')

	def test_can_access_hire_tutor_page(self):
		"""
			Test: John can access the tests and flash cards page
		"""
		self.page_title_is('/contact/hire/','Ustudy Hire Tutor')
		
		
	def test_can_access_contact_page(self):
		"""
			Test: John can access the contact page
		"""
		self.page_title_is('/contact/','Ustudy Contact')


#testing footer URLS

	def test_can_access_about_page(self):
		"""
			Test: John can access the about page
		"""
		self.page_title_is('/about/','Ustudy About')

	def test_can_access_privacy_policy_page(self):
		"""
			Test: John can access the privacy-policy page
		"""
		self.page_title_is('/privacy/','Ustudy Privacy Policy')

	def test_can_access_careers_page(self):
		"""
			Test: John can access the careers page
		"""
		self.page_title_is('/jobs/','Ustudy Careers')

	
	
		
	
