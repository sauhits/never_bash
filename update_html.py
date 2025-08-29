import sys

template_file_path = './site/template.html'
html_file_path ='./site/index.html'

insert_something_value = str(sys.argv[1])

with open(template_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

updated_html_content = html_content.replace('{insert_something}', insert_something_value)

with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_html_content)