from django.test import TestCase,Client
from django.core.urlresolvers import resolve

#we need WebTest to test for form submisions
from django_webtest import WebTest

from . import views

class TestCRUDBase(WebTest):
	def setUp(self):
		# Every test needs a client.
		self.client = Client()




class TestCRUDCourseView(TestCRUDBase):
	"""
		Test the create,update,delete course views
	"""
	

	def test_course_create_url_resolves_to_course_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		view = resolve('/courses/course/create/')
		self.assertEqual(view.func,views.course_create_view)

	def test_course_create_url_response_200(self):
		"""
			Test: the url view response is 200 Ok
		"""
		response = self.client.get('/courses/course/create/')
		#self.assertTemplateUsed(response,'account/login.html')
		self.assertEqual(response.status_code,200)

	def test_update_url_resolves_to_course_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		view = resolve('/courses/course/course_slug/update/')
		self.assertEqual(view.func,views.course_update_view)

	def test_delete_url_resolves_to_course_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		view = resolve('/courses/course/course_slug/delete/')
		self.assertEqual(view.func,views.course_delete_view)







class TestCRUDCourseModuleView(TestCRUDBase):
	"""
		Test the create,update,delete course module views
	"""
	

	def test_root_url_resolves_to_course_modules_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/modules/create/')
		self.assertEqual(found.func,views.course_modules_create_view)

	def test_update_url_resolves_to_course_module_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/update/')
		self.assertEqual(found.func,views.course_module_update_view)

	def test_delete_url_resolves_to_course_module_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/delete/')
		self.assertEqual(found.func,views.course_module_delete_view)








class TestCRUDCourseModuleQuizView(TestCRUDBase):
	"""
		Test the create,update,delete course-module-quiz views
	"""

	def test_root_url_resolves_to_course_module_quiz_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/quiz/create/')
		self.assertEqual(found.func,views.course_module_quiz_create_view)

	def test_update_url_resolves_to_course_module_quiz_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/quiz/1/update/')
		self.assertEqual(found.func,views.course_module_quiz_update_view)


	def test_delete_url_resolves_to_course_module_quiz_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/quiz/1/delete/')
		self.assertEqual(found.func,views.course_module_quiz_delete_view)




class TestCRUDCourseModuleSectionView(TestCRUDBase):
	"""
		Test the create,update,delete course-module-section views
	"""

	def test_root_url_resolves_to_course_module_section_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/sections/create/')
		self.assertEqual(found.func,views.course_module_section_create_view)

	def test_update_url_resolves_to_course_module_section_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/update/')
		self.assertEqual(found.func,views.course_module_section_update_view)

	def test_delete_url_resolves_to_course_module_section_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/delete/')
		self.assertEqual(found.func,views.course_module_section_delete_view)



class TestCRUDCourseModuleSectionActivityView(TestCRUDBase):
	"""
		Test the create,update,delete course-module-section-activity views
	"""

	def test_root_url_resolves_to_course_module_section_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/activity/create/')
		self.assertEqual(found.func,views.course_module_section_activity_create_view)

	def test_update_url_resolves_to_course_module_section_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/activity/1/update/')
		self.assertEqual(found.func,views.course_module_section_activity_update_view)

	def test_delete_url_resolves_to_course_module_section_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/activity/1/delete/')
		self.assertEqual(found.func,views.course_module_section_activity_delete_view)




class TestCRUDCourseModuleSectionQuizView(TestCRUDBase):
	"""
		Test the create,update,delete course-module-section-quiz views
	"""

	def test_root_url_resolves_to_course_module_section_create_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/quiz/create/')
		self.assertEqual(found.func,views.course_module_section_quiz_create_view)

	def test_update_url_resolves_to_course_module_section_update_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/update/')
		self.assertEqual(found.func,views.course_module_section_quiz_update_view)

	def test_delete_url_resolves_to_course_module_section_delete_view(self):
		"""
			Test: the url view  resolves to the correct view function.
		"""
		found = resolve('/courses/course/course_slug/module/module_slug/section/section_slug/quiz/1/delete/')
		self.assertEqual(found.func,views.course_module_section_quiz_delete_view)

	










