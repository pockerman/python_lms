#python imports
import unittest

#Django imports
from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group

#third party imports:Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

#third party imports: django-taggit
from taggit.managers import TaggableManager

from ecms_course_create_app.models import Subject

#local imports
#from ustdy.website_settings import site_index_title

class NavigationTest(object):

	@staticmethod
	def test_navigation(browser,TestCase):
		#John browses the navigation elements
		logo = browser.find_element_by_id("ustdy-logo")
		TestCase.assertTrue(logo.is_displayed())
	
		service_link = browser.find_element_by_link_text('SERVICES')
		TestCase.assertTrue(service_link.is_displayed())

		education_link = browser.find_element_by_link_text('EDUCATION')
		TestCase.assertTrue(education_link.is_displayed())

		contact_link = browser.find_element_by_link_text('CONTACT')
		TestCase.assertTrue(contact_link.is_displayed())

class FooterTest(object):
	@staticmethod
	def test_footer(browser,TestCase):
		site_map_link = browser.find_element_by_link_text('SITE-MAP')
		TestCase.assertTrue(site_map_link.is_displayed())

		about_link = browser.find_element_by_link_text('ABOUT')
		TestCase.assertTrue(about_link.is_displayed())

		privacy_policy_link = browser.find_element_by_link_text('PRIVACY-POLICY')
		TestCase.assertTrue(privacy_policy_link.is_displayed())

		careers_link = browser.find_element_by_link_text('CAREERS')
		TestCase.assertTrue(careers_link.is_displayed())

#class UstudyTestBase(LiveServerTestCase):

	
#	def create_subjects(self):
#		self.subject = Subject.objects.create(title="Test Subject",slug="test-subject").save()

#	@classmethod
#	def setUpClass(cls):
#		super(UstudyTestBase, cls).setUpClass()
#		cls.create_subjects(cls)
#		cls.browser = webdriver.Firefox()
#		cls.browser.implicitly_wait(30)
#		cls.browser.delete_all_cookies()

#	@classmethod
#	def tearDownClass(cls):
#		super(UstudyTestBase, cls).tearDownClass()
#		cls.browser.quit()
#		cls.subject.delete()
		#cls.location.delete()
		#cls.superuser.delete()


#	def test_db(self):
#		"""
#			Test that the database is in correct state
#		"""
#		self.assertEquals(Subject.objects.all().count(),1)
		

class NewVisitorTest(LiveServerTestCase):


	def create_subjects(self):
		self.subject = Subject.objects.create(title="Test Subject",slug="test-subject")
		self.subject.save()

		#self.assertEquals(Subject.objects.all().count(),1)

	def delete_subjects(self):
		self.subject.delete()

	@classmethod
	def setUpClass(cls):
		super(NewVisitorTest, cls).setUpClass()
		#cls.subject = Subject.objects.create(title="Test Subject",slug="test-subject")
		cls.create_subjects(cls)
		cls.browser = webdriver.Firefox()
		cls.browser.implicitly_wait(30)
		cls.browser.delete_all_cookies()

	@classmethod
	def tearDownClass(cls):
		super(NewVisitorTest, cls).tearDownClass()
		cls.browser.quit()
		cls.delete_subjects(cls)
		#cls.location.delete()
		#cls.superuser.delete()


	def test_db(self):
		"""
			Test that the database is in correct state
		"""
		self.assertEquals(Subject.objects.all().count(),1)

	
	def test_can_browse_index_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. 
		"""	
		#the Ustudy index page
		self.browser.get(self.live_server_url+'/')

		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Home',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		#John scrolls down the index page and browses the content
		#he should be able to see the following items
		hire_tutor_link = self.browser.find_element_by_link_text('Hire A Tutor')
		self.assertTrue(hire_tutor_link.is_displayed())

		find_lecture_notes_link = self.browser.find_element_by_link_text('Find Lecture Notes')
		self.assertTrue(find_lecture_notes_link.is_displayed())

		#wait unitl this element becomes visible
		#WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Development')))

		development_link = self.browser.find_element_by_link_text('Development')
		self.assertTrue(development_link.is_displayed())

		online_courses_link = self.browser.find_element_by_link_text('Online Courses')
		self.assertTrue(online_courses_link.is_displayed())

		flash_cards_link = self.browser.find_element_by_link_text('Online Tests & Flash Cards')
		self.assertTrue(flash_cards_link.is_displayed())
		
		host_courses_link = self.browser.find_element_by_link_text('Host Your Courses')
		self.assertTrue(host_courses_link.is_displayed())	

		#John can view the links but we must also have images
		#for those links. We first get all the col-md-4 col-sm-6
		#elements in the page then collect the img tags 
		pic_elements_list = self.browser.find_elements_by_class_name("col-md-4")

		#we must have six
		self.assertEqual(len(pic_elements_list),6)

		img_counter = 0

		for elem in pic_elements_list:
			img_tag = elem.find_elements_by_tag_name("img")
			self.assertNotEqual(img_tag,None)
			if img_tag != None:
				img_counter +=1

		#we must have six img tags
		#img_list = pic_elements_list.find_elements_by_tag_name("img")
		self.assertEqual(img_counter,6)

		#John continues checking the index page he 
		#finds the Tell Me More button
		button = self.browser.find_element_by_link_text("Tell Me More")
		self.assertTrue(button.is_displayed())
		
#class NewVisitorDevelopmentPageTest(UstudyTestBase):

	def test_can_browse_development_page_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Development link 
			and goes to the development page
		"""
		page = self.browser.get(self.live_server_url+"/services/development/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Development',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		#there should be an image there
		img_tag = self.browser.find_element_by_tag_name("img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"cubes_pic_lms_view.jpg")
		
		#there should be a Contact Us link on the page
		contact_us_link = self.browser.find_element_by_link_text('Contact Us')
		self.assertTrue(contact_us_link.is_displayed())

		

#class NewVisitorHostPageTest(UstudyTestBase):
	def test_can_browse_host_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Host-Courses link 
			and goes to the host-courses page
		"""
		page = self.browser.get(self.live_server_url+"/services/host-courses/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Host Courses',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		#there should be an image there
		img_tag = self.browser.find_element_by_tag_name("img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"cloud_pic_host_view.jpeg")

		#there should be a Contact Us link on the page
		contact_us_link = self.browser.find_element_by_link_text('Contact Us')
		self.assertTrue(contact_us_link.is_displayed())

#class NewVisitorCoursesPageTest(UstudyTestBase):
	def test_can_browse_courses_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Courses link 
			and goes to the courses page
		"""
		page = self.browser.get(self.live_server_url+"/courses/all/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Courses',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		img_tag = self.browser.find_element_by_id("header-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"uni_pic_I.jpg")

		#John should be able to see the courses
		course_1 = self.browser.find_element_by_link_text('CFD With C++')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-1-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"cfd_pic_I.jpg")

		course_1 = self.browser.find_element_by_link_text('Descriptive Statistics With Python')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-2-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"stats_pic_I.png")

		course_1 = self.browser.find_element_by_link_text('Statistical Inference With Python')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-3-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"stats_pic_II.png")

		course_1 = self.browser.find_element_by_link_text('Introduction To Supercomputing With C++')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-4-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"hpc_pic.jpeg")


		course_1 = self.browser.find_element_by_link_text('Machine Learning With C++')
		self.assertTrue(course_1.is_displayed())
		img_tag = self.browser.find_element_by_id("course-5-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"ml_pic.jpg")

		course_1 = self.browser.find_element_by_link_text('AI With C++')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-6-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"ai_pic.jpg")

		course_1 = self.browser.find_element_by_link_text('Rigid Body Dynamics Simulation')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-7-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"rgbd_sim_pic.jpg")

		course_1 = self.browser.find_element_by_link_text('C++ Programming')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-8-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"cpp_pic.jpg")

		course_1 = self.browser.find_element_by_link_text('Java Programming')
		self.assertTrue(course_1.is_displayed())
		self.assertTrue(course_1.is_enabled())
		img_tag = self.browser.find_element_by_id("course-9-img")
		img_url = img_tag.get_attribute("src")
		img_file_list = img_url.split("/")
		self.assertEqual(img_file_list[len(img_file_list)-1],"java_pic.jpg")

		

#class NewVisitorLibraryPageTest(UstudyTestBase):
	def test_can_browse_library_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Library link 
			and goes to the library page
		"""
		page = self.browser.get(self.live_server_url+"/library/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Library',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		#John should be able to see a search form
		search_field = self.browser.find_element_by_id("srch-term")

		placeholder = search_field.get_property("placeholder")
		self.assertEqual(placeholder,"Search for lecture notes")

		max_length = search_field.get_property("maxlength")
		self.assertEqual(max_length,"128")

		#John should be able to see the subjects

		#John should be able to see the external links
		link_1 = self.browser.find_element_by_link_text('All IT eBooks')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		link_1 = self.browser.find_element_by_link_text('IT EBOOKS')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		link_1 = self.browser.find_element_by_link_text('Free PDF Books')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		link_1 = self.browser.find_element_by_link_text('NASA Technical Documents')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		link_1 = self.browser.find_element_by_link_text('HATHI TRUST')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		link_1 = self.browser.find_element_by_link_text('Greek National Archive Of PhD Thesis')
		self.assertTrue(link_1.is_displayed())
		self.assertTrue(link_1.is_enabled())

		

#class NewVisitorTestsPageTest(UstudyTestBase):
	def test_can_browse_tests_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Courses link 
			and goes to the courses page
		"""
		page = self.browser.get(self.live_server_url+"/tests/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Tests & Flash Cards',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		
		

#class NewVisitorTutoringPageTest(UstudyTestBase):
	def test_can_browse_tutoring_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Courses link 
			and goes to the courses page
		"""
		page = self.browser.get(self.live_server_url+"/contact/hire/")

		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Hire Tutor',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		form = self.browser.find_element_by_id('hireForm')

		#make sure we have the following elements in the form
		name_in = form.find_element_by_name('contact_name')
		self.assertTrue(name_in.is_enabled())

		max_length = name_in.get_property("maxlength")

		#for some reason this we get None
		#meaning that the property does not exist
		self.assertEqual(max_length,"100")

		surname_in = form.find_element_by_name('contact_surname')
		self.assertTrue(surname_in.is_enabled())
		max_length = surname_in.get_property("maxlength")
		self.assertEqual(max_length,"200")

		email_in = form.find_element_by_name('contact_email')
		self.assertTrue(email_in.is_enabled())

		#list of expected values in hire option dropdown
		exp_select_hire_opts=['Select','Teaching','Semester Assignment',
													'Degree Dissertation','MSc Assignment','MSc Dissertation',
													'Statistical Analysis','Programming Assignment']

		# empty list for capturing actual options displayed
		# in the dropdown
		act_select_hire_opts = []

		select_hire_options = Select(self.driver.find_element_by_id("id_hire_choices"))

		self.assertEqual(len(select_hire_options.options),len(exp_select_hire_opts))

		# get options in a list
		for option in select_hire_options.options:
			act_select_hire_opts.append(option.text)

		# check expected options list with actual options list
		self.assertListEqual(exp_select_hire_opts, act_select_hire_opts)

		# check default selected option is Select
		self.assertEqual("Select", select_hire_options.first_selected_option.text)

		#list of expected values in hire option dropdown
		exp_select_languag_opts=['Select','Teaching','English','Greek']

		# empty list for capturing actual options displayed
		# in the dropdown
		act_select_language_opts = []

		select_language_options = Select(self.driver.find_element_by_id("id_language"))

		self.assertEqual(len(select_language_options.options),len(exp_select_languag_opts))

		# get options in a list
		for option in select_language_options.options:
			act_select_language_opts.append(option.text)

		# check expected options list with actual options list
		self.assertListEqual(exp_select_language_opts, act_select_language_opts)

		# check default selected option is Select
		self.assertEqual("Select", select_language_options.first_selected_option.text)

		university_in = self.browser.find_element_by_name('university')
		self.assertTrue(university_in.is_enabled())
		max_length = university_in.get_property("maxlength")
		self.assertEqual(max_length,"200")

		department_in = self.browser.find_element_by_name('department')
		self.assertTrue(department_in.is_enabled())
		max_length = department_in.get_property("maxlength")
		self.assertEqual(max_length,"200")

		content_in = self.browser.find_element_by_name('content')
		self.assertTrue(content_in.is_enabled())

		#submit_button = self.browser.find_element_by_tag_name("button")
		submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		self.assertTrue(submit_button.is_enabled())

		#Now John wants to send a message to Ustduy to hire a tutor
		name_in.send_keys("Alexandros")
		surname_in.send_keys("Giavaras")
		email_in.send_keys("test_mail@gmail.com")
		select_hire_options.select_by_value("Teaching")
		select_language_options.select_by_value("English")
		university_in.send_keys("Test University")
		department_in.send_keys("Test Department")
		content_in.send_keys("This is a test message")
		submit_button.click()

		#wait unitl we get the response from the server
		WebDriverWait(self.browser, 10).until(expected_conditions.title_is("Ustudy Contact Success Hire"))

		#John should be redirected to the success page
		self.assertEqual(self.browser.current_url,self.live_server_url + '/contact/hire-success/')
		self.assertEqual('Ustudy Contact Success Hire',self.browser.title)

#class NewVisitorContactPageTest(UstudyTestBase):

	def test_can_browse_contact_page(self):
		"""
			Test: John is a studen that wants to find on-line courses.
			He searched the internet and found Ustdy. He clicks the google link
			and lands at Ustdy index page. He then clicks on the Contact link 
			and goes to the contact page
		"""
		page = self.browser.get(self.live_server_url+"/contact/")
		#John knows that he is in the right place because he can
		#view the title of the index page
		self.assertEqual('Ustudy Contact',self.browser.title)

		#test the navigation links
		NavigationTest.test_navigation(self.browser,self)

		#test the footer links
		FooterTest.test_footer(self.browser,self)

		#make sure we have the following elements in the form
		name_in = self.browser.find_element_by_name('contact_name')
		self.assertTrue(name_in.is_enabled())
		max_length = name_in.get_property("maxlength")
		self.assertEqual(max_length,"200")
		
		subject = self.browser.find_element_by_name('subject')
		self.assertTrue(subject.is_enabled())
		max_length = subject.get_property("maxlength")
		self.assertEqual(max_length,"200")

		email = self.browser.find_element_by_name('contact_email')
		self.assertTrue(email.is_enabled())

		content = self.browser.find_element_by_name('content')
		self.assertTrue(content.is_enabled())

		#submit_button = self.browser.find_element_by_tag_name("button")
		submit_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		self.assertTrue(submit_button.is_enabled())

		#Now  John wants to send a message to Ustudy
		name_in.send_keys("Alexandros Giavaras")
		subject.send_keys("Test Subject")
		email.send_keys("test_mail@gmail.com")
		content.send_keys("This is a test message")
		submit_button.click()

		#wait unitl we get the response from the server
		WebDriverWait(self.browser, 10).until(expected_conditions.title_is("Ustudy Contact Success"))

		#John should be redirected to the success page
		self.assertEqual(self.browser.current_url,self.live_server_url + '/contact/success/')
		self.assertEqual('Ustudy Contact Success',self.browser.title)

	
	

	


	

	


	
		
		
		
		
