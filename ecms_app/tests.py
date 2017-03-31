
from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#we need WebTest to test for form submisions
from django_webtest import WebTest

from . import views

class TestOnlineCourses(WebTest):
	"""
		Temporary Unit tests for the index page. This
		test class should be deactivated when Ustdy is fully 
		released.
	"""
	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_online_courses_url_resolves_to_ecms_courses_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/all/')
		self.assertEqual(found.func,views.ecms_courses_tmp_view)

	def test_root_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/courses/all/')
		self.assertTemplateUsed(response,'ecms/tmp/ecms_index.html')
		self.assertEqual(response.status_code,200)

class TestOnlineCoursesCatalog(WebTest):
	"""
		Unit test for the courses catalog
	"""
	def setUp(self):
		# Every test needs a client.
		self.client = Client()

	def test_online_courses_catalog_url_resolves_to_ecms_courses_catalog_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/catalog/')
		self.assertEqual(found.func,views.ecms_courses_catalog_view)

	def test_ecms_courses_catalog_view_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/courses/catalog/')
		self.assertTemplateUsed(response,'ecms/tmp/ecms_catalog.html')
		self.assertEqual(response.status_code,200)

	def test_online_courses_catalog_subject_url_resolves_to_ecms_courses_catalog_subject_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/catalog/subject/test-subject/')
		self.assertEqual(found.func,views.ecms_courses_catalog_subject_view)

	def test_ecms_courses_catalog_subject_view_url_response_is_200(self):
		"""
			Test: the url view returns 200 OK.
		"""
		response = self.client.get('/courses/catalog/subject/test-subject/')
		self.assertTemplateUsed(response,'ecms/tmp/ecms_catalog.html')
		self.assertEqual(response.status_code,200)


		
	

# Create your tests here.
#class TestIndexPage(WebTest):
#	"""
#		Unit tests for index page 
#	"""

	#def setUp(self):
		# Every test needs a client.
	#	self.client = Client()

	#def test_root_url_resolves_to_ecms_index(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/all/')
	#	self.assertEqual(found.func,views.ecms_index)

	#def test_ecms_index_subject_url_resolves_to_ecms_index_subject(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/subject/subject_slug/all/')
	#	self.assertEqual(found.func,views.ecms_index_subject)

	#def test_course_overview_url_resolves_to_course_overview(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/overview/')
	#	self.assertEqual(found.func,views.course_overview)

	#def test_course_module_view_url_resolves_to_course_module_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/')
	#	self.assertEqual(found.func,views.course_module_view)

	#def test_course_module_section_view_url_resolves_to_course_module_section_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/')
	#	self.assertEqual(found.func,views.course_module_section_view)

	#def test_course_module_quiz_start_view_url_resolves_to_course_module_quiz_start_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/quiz/1/start/')
	#	self.assertEqual(found.func,views.course_module_quiz_start_view)

	#def test_course_module_quiz_do_view_url_resolves_to_course_module_quiz_do_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/quiz/1/do/')
	#	self.assertEqual(found.func,views.course_module_quiz_do_view)

	#def test_course_module_section_quiz_start_view_url_resolves_to_course_module_section_quiz_start_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/start/')
	#	self.assertEqual(found.func,views.course_module_section_quiz_start_view)

	#def test_course_module_section_quiz_do_view_url_resolves_to_course_module_section_quiz_do_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/do/')
	#	self.assertEqual(found.func,views.course_module_section_quiz_do_view)

	#def test_course_module_section_activity_view_url_resolves_to_course_module_section_activity_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/activity/')
	#	self.assertEqual(found.func,views.course_module_section_activity_view)

	#def test_course_resourses_view_url_resolves_to_course_resourses_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/resourses/')
	#	self.assertEqual(found.func,views.course_resourses_view)

	#def test_course_student_progress_view_url_resolves_to_course_student_progress_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/student/1/progress/')
	#	self.assertEqual(found.func,views.course_student_progress_view)

	#def test_course_syllabus_view_url_resolves_to_course_syllabus_view(self):
	#	"""
	#		Test: the url view  resolves to the correct view function.
	#	"""
	#	found = resolve('/courses/course/course_slug/syllabus/')
	#	self.assertEqual(found.func,views.course_syllabus_view)


	

	
		
	
