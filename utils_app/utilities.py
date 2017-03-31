from django.template import Context, Template

RATING_CHOICES = [(1, "*"),(2, "**"),(3, "***"),
									(4, "****"),(5, "*****"),]

def INVLALID_LOCATION():
	return "INVALID_LOCATION"

def upload_section_file(root,instance, filename):
	username = instance.section.owner.username
	course_id = instance.section.course.id
	module_id = instance.section.module.id
	section_id = instance.section.id
	return "{}/{}/{}/{}/{}".format(root,username,course_id,module_id,section_id,filename)


def convert_and_replace_word(word,convert_to='L',replace=(' ','_')):

		new_word = word
		if convert_to == 'L':
			new_word = word.lower()
		elif convert_to == 'U':
			new_word = word.upper()
			
		if replace != None:
			new_word = new_word.replace(replace[0],replace[1])
		return new_word

def get_errors_map_list(form):
	errors_map={}
	for field,errors in form.errors.items():
		if field in errors_map.keys():
			continue
		else:
			errors_map[field]=""
			for error in errors:
				errors_map[field] += error+','
			
	for key in errors_map.keys():
		errors = errors_map[key]
		errors_map[key] = errors.split(',')
	return errors_map

def render_user_html_file(file,context):
	data = file.read().replace('\n', '')
	t = Template(data)
	c = Context(context)
	return t.render(c)


	
	
