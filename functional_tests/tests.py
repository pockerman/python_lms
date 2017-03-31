from xmlrunner import xmlrunner
import HtmlTestRunner
import unittest
import os
#from .urls_testing import URLTest

#from ecms_course_create_app.models import Subject
from .ustudy_tests_cases.urls_testing import URLTest
from .ustudy_tests_cases.newvisitor_testing import NewVisitorTest
#NewVisitorDevelopmentPageTest,\
#NewVisitorHostPageTest,NewVisitorCoursesPageTest,NewVisitorLibraryPageTest,NewVisitorTestsPageTest,\
#NewVisitorTutoringPageTest,NewVisitorContactPageTest

# get the directory path to output report file
dir = os.getcwd()

#create a the database before the tests are
#run
#Subject.objects.create(title="Test Subject",slug="test-subject").save()

# get all tests from SearchProductTest and HomePageTest class
#db_tests = unittest.TestLoader().loadTestsFromTestCase(UstudyTestBase)
url_tests = unittest.TestLoader().loadTestsFromTestCase(URLTest)
visitor_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorTest)
#development_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorDevelopmentPageTest) 
#host_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorHostPageTest)
#courses_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorCoursesPageTest)
#library_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorLibraryPageTest)
#tests_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorTestsPageTest)
#tutoring_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorTutoringPageTest)
#conatct_page_tests = unittest.TestLoader().loadTestsFromTestCase(NewVisitorContactPageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

smoke_tests = unittest.TestSuite([visitor_tests])

#smoke_tests = unittest.TestSuite([db_tests,url_tests,home_page_tests,development_page_tests,
#																	host_page_tests,courses_page_tests,library_page_tests,
#																	tests_page_tests,tutoring_page_tests,conatct_page_tests])

# open the report file
#outfile = open(dir + "\SmokeTestReport.html", "w")

# configure HTMLTestRunner options
#runner = HtmlTestRunner.HTMLTestRunner(stream=outfile,output='example_dir') #,title='Test Report',description='Smoke Tests')

# run the suite using HTMLTestRunner
#runner.run(smoke_tests)

# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)

# run the suite
#unittest.TextTestRunner(verbosity=2).run(smoke_tests)

		
		
#if __name__ == '__main__': 
#	unittest.main(warnings='ignore')
