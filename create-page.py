import os
import json
from atlassian import Confluence
from pprint import pprint

import logging
logging.basicConfig(filename='create-page.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
filename = os.environ.get('FILENAME')
title = os.environ.get("TITLE")
space = os.environ.get("SPACE")
parent = os.environ.get("PARENT")

confluence = Confluence(
    url=url, 
    username=username, 
    password=password
)

os.system("markdown {}.md > {}.html".format (filename, filename))
with open("{}.html".format (filename), 'r') as file:
    body = file.read()
try:
	page_exists = confluence.page_exists(space, title)
except Exception:
    pass
if (page_exists):
	current_page_id = confluence.get_page_id(space, title)
	response = confluence.update_page(
		current_page_id, 
		title, 
		body, 
		type='page', 
		representation='storage', 
		minor_edit=False
	)
	url_base = response['_links']['base']
	url_webui = response['_links']['webui']
	print ("{}{}".format (url_base, url_webui))
else:
	parent_page_id = confluence.get_page_id(space, parent)
	response = confluence.create_page(
	    space=space,
		parent_id=parent_page_id, 
	    title=title,
	    body=body
	)
	url_base = response['_links']['base']
	url_webui = response['_links']['webui']
	print ("{}{}".format (url_base, url_webui))
