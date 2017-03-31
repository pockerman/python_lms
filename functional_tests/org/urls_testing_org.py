#python imports
import unittest

#Django imports
from django.test import LiveServerTestCase

#third party imports:Selenium
from selenium import webdriver

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
		self.assertIn(name,self.browser.title)

	def test_can_access_root(self):
		"""
			Test: John can access the index page
		"""
		self.page_title_is('/','U-study')
		#self.browser.get(self.live_server_url+'/')
		#make sure that the title of the page is not Ustdy-404
		#self.assertNotIn('Ustudy-404',self.browser.title)

	def test_can_navigate_courses_subject_catalog(self):
		"""
			Test: John wants to browse the available courses for a particular 
			subject
		"""
		self.browser.get(self.live_server_url+'/courses/subject/subject_slug/all/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_course_overview(self):
		"""
			Test: John wants to browse the overview of a particular course 
			in order to decide if he wants to enroll to the course	
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/overview/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_module(self):
		"""
			Test: John wants to study a certain module but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/')
		
		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section(self):
		"""
			Test: John wants to study a certain module's section but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/')
		#print(self.browser.title)
		#import pdb;pdb.set_trace()

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_quiz_start(self):
		"""
			Test: John wants to take a certain module's quiz but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/quiz/1/start/')

			#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_quiz_do(self):
		"""
			Test: John wants to take a certain module's quiz but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/quiz/1/do/')

			#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_quiz_start(self):
		
		"""
			Test: John wants to take a certain section's quiz but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/start/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_quiz_do(self):
		
		"""
			Test: John wants to take a certain section's quiz but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/do/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_activity(self):
		
		"""
			Test: John wants to check a certain section's activity but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/activity/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_course_resourses(self):
		
		"""
			Test: John wants to check the resources of a given course but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/resourses/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)


	def test_can_navigate_course_syllabus(self):
		
		"""
			Test: John wants to check the syllabus of a given course but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/syllabus/')

			#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_course_progress(self):
		
		"""
			Test: John wants to check the progress of a given course but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/student/1/progress/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)


	def test_can_navigate_create_course(self):
		"""
			Test: John wants to create a course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_update_course(self):
		"""
			Test: John wants to update a course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)


	def test_can_navigate_delete_course(self):
		"""
			Test: John wants to delete a course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_modules_create(self):
		"""
			Test: John wants to create a module for a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/modules/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_update(self):
		"""
			Test: John wants to update a module for a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_delete(self):
		"""
			Test: John wants to delete a module for a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_section_create(self):
		"""
			Test: John wants to create a section for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_section_update(self):
		"""
			Test: John wants to update a section for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_section_delete(self):
		"""
			Test: John wants to delete a section for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_quiz_create(self):
		"""
			Test: John wants to create a quiz for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/quiz/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_quiz_update(self):
		"""
			Test: John wants to update a quiz for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/quiz/1/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_quiz_delete(self):
		"""
			Test: John wants to delete a quiz for a given module of a given  course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/quiz/1/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)


	def test_can_navigate_module_section_quiz_create(self):
		"""
			Test: John wants to create a quiz for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/quiz/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_quiz_update(self):
		"""
			Test: John wants to update a quiz for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_quiz_delete(self):
		"""
			Test: John wants to delete a quiz for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_activity_create(self):
		"""
			Test: John wants to create an activity for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/activity/create/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_activity_update(self):
		"""
			Test: John wants to update an activity for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/activity/1/update/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_module_section_activity_delete(self):
		"""
			Test: John wants to delete an activity for a given section of given module of a given course but he is neither logged in nor
						an instauctor
		"""
		self.browser.get(self.live_server_url+'/courses/course/course_slug/module/module_slug/section/section_slug/activity/1/delete/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	








	def test_can_navigate_faq(self):
		"""
			Test: John is still wondering about Ustdy so he clicks
		 	on the FAQ link to find out more 
		"""
		self.browser.get(self.live_server_url+'/faqs/')
			#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_privacy_policy(self):
		"""
			Test: John is very anxious about the privacy of Ustdy
			so he clicks on the privacy-policy link
		"""
		self.browser.get(self.live_server_url+'/privacy/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_about_page(self):
		"""
			Test: John wants to more about Ustdy so he clicks the about link
		"""
		self.browser.get(self.live_server_url+'/about/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_jobs_page(self):
		"""
			Test: John wants to work for Ustdy so he clicks the jobs link
		"""
		self.browser.get(self.live_server_url+'/jobs/')

		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)



	def test_can_navigate_contact(self):
		"""
			Test: John wants to contact Ustdy
		"""
		self.browser.get(self.live_server_url+'/contact/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_contact_hire(self):
		"""
			Test: John wants to hire an instaructor from Ustdy
		"""
		self.browser.get(self.live_server_url+'/contact/hire/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)



	def test_can_access_profile(self):
		"""
				Test: John wants to access his profile but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/account/profile/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_edit_profile(self):
		"""
				Test: John wants to access his profile but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/account/profile/edit/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)

	def test_can_navigate_login(self):
		"""
			Test: John wants to login Ustdy
		"""
		self.browser.get(self.live_server_url+'/account/login/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_logout(self):
		"""
			Test: John wants to logout from Ustdy but he is not logged in
		"""
		self.browser.get(self.live_server_url+'/account/logout/')

		#...found the URL
		self.assertNotIn('Ustdy-404',self.browser.title)

		#...redirected to login page 
		self.assertIn('Ustdy Log In',self.browser.title)
		

	def test_can_navigate_signup(self):
		"""
			Test: John wants to signup Ustdy
		"""
		self.browser.get(self.live_server_url+'/account/register/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_reset_password(self):
		"""
			Test: John wants to reset his password in Ustdy
		"""
		self.browser.get(self.live_server_url+'/account/password-reset/')
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_library(self):
		"""
			Test: John wants to check what's in the library
		"""
		self.browser.get(self.live_server_url+'/library/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_tests(self):
		"""
			Test: John wants to check what's in the tests
		"""
		self.browser.get(self.live_server_url+'/tests/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_lms_development(self):
		"""
			Test: John wants to check what's in the LMS development
		"""
		self.browser.get(self.live_server_url+'/services/lms-development/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)

	def test_can_navigate_host_courses(self):
		"""
			Test: John wants to check what's in the Host courses
		"""
		self.browser.get(self.live_server_url+'/services/host-courses/')
		#make sure that the title of the page is not Ustdy-404
		#John must be able to navigate
		self.assertNotIn('Ustdy-404',self.browser.title)
		
		




