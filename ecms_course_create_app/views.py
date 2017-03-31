from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def course_create_view(request,template='ecms_course_creator/create_course_form.html'):
	return HttpResponse('course_create_view response')

@login_required
def course_update_view(request,course_slug,template='ecms_course_creator/update_course_form.html'):
	return HttpResponse('course_update_view response')

@login_required
def course_delete_view(request,course_slug,template='ecms_course_creator/delete_course_form.html'):
	return HttpResponse('course_delete_view response')

@login_required
def course_modules_create_view(request,course_slug,template='ecms_course_creator/course_modules_create_form.html'):
	return HttpResponse('course_modules_create_view response')

@login_required
def course_module_update_view(request,course_slug,module_slug,template='ecms_course_creator/course_module_update_form.html'):
	return HttpResponse('course_module_update_view response')

@login_required
def course_module_delete_view(request,course_slug,module_slug,template='ecms_course_creator/course_module_delete_form.html'):
	return HttpResponse('course_module_delete_view response')

@login_required
def course_module_quiz_create_view(request,course_slug,module_slug,
															template='ecms_course_creator/course_module_quiz_create_form.html'):
	return HttpResponse('course_module_quiz_create response')

@login_required
def course_module_quiz_update_view(request,course_slug,module_slug,quiz_id,
															template='ecms_course_creator/course_module_quiz_update_form.html'):
	return HttpResponse('course_module_quiz_update response')

@login_required
def course_module_quiz_delete_view(request,course_slug,module_slug,quiz_id,
															template='ecms_course_creator/course_module_quiz_delete_form.html'):
	return HttpResponse('course_module_quiz_delete response')


@login_required
def course_module_section_create_view(request,course_slug,module_slug,
																			template='ecms_course_creator/course_module_sections_create_form.html'):
	return HttpResponse('course_modules_create_view response')

@login_required
def course_module_section_update_view(request,course_slug,module_slug,section_slug,
															template='ecms_course_creator/course_module_section_update_form.html'):
	return HttpResponse('course_module_section_update_view response')

@login_required
def course_module_section_delete_view(request,course_slug,module_slug,
																			template='ecms_course_creator/course_module_section_delete_form.html'):
	return HttpResponse('course_module_section_delete_view response')



@login_required
def course_module_section_activity_create_view(request,course_slug,module_slug,section_slug,
																					template='ecms_course_creator/course_module_section_activity_create_form.html'):
	return HttpResponse('course_module_section_activity_create response')

@login_required
def course_module_section_activity_update_view(request,course_slug,module_slug,section_slug,activity_id,
																					template='ecms_course_creator/course_module_section_activity_update_form.html'):
	return HttpResponse('course_module_section_activity_update response')

@login_required
def course_module_section_activity_delete_view(request,course_slug,module_slug,section_slug,activity_id,
																					template='ecms_course_creator/course_module_section_activity_delete_form.html'):
	return HttpResponse('course_module_section_activity_delete response')


@login_required
def course_module_section_quiz_create_view(request,course_slug,module_slug,section_slug,
																					template='ecms_course_creator/course_module_section_quiz_create_form.html'):
	return HttpResponse('course_module_section_quiz_create response')

@login_required
def course_module_section_quiz_update_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms_course_creator/course_module_section_quiz_update_form.html'):
	return HttpResponse('course_module_section_quiz_update response')

@login_required
def course_module_section_quiz_delete_view(request,course_slug,module_slug,section_slug,quiz_id,
																					template='ecms_course_creator/course_module_section_quiz_delete_form.html'):
	return HttpResponse('course_module_section_quiz_delete response')
























