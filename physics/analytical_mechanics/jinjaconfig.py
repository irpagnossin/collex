import jinja2
import os

def create_tex(filename, options, variation='A'):

	latex_jinja_env = jinja2.Environment(
		block_start_string = '\BLOCK{',
		block_end_string = '}',
		variable_start_string = '\VAR{',
		variable_end_string = '}',
		comment_start_string = '\#{',
		comment_end_string = '}',
		line_statement_prefix = '%%',
		line_comment_prefix = '%#',
		trim_blocks = True,
		autoescape = False,
		loader = jinja2.FileSystemLoader(os.path.abspath('.'))
	)

	basename = os.path.splitext(os.path.basename(filename))[0]
	template_name = '{}.tex.jinja'.format(basename)
	output_filename = '{}({}).tex'.format(basename, variation)
	template = latex_jinja_env.get_template(template_name)


	with open(output_filename, "w") as file:
	    file.write(template.render(**options))