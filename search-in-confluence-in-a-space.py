import os
import json
from atlassian import Confluence
from pprint import pprint

import logging
logging.basicConfig(filename='search-in-confluence-in-a-space.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
space = os.environ.get('SPACE')
keyword = os.environ.get('KEYWORD')

confluence = Confluence(
    url=url, 
    username=username, 
    password=password
)

cql = "space.key={} and (text ~ {})".format(space, keyword)
results = confluence.cql(cql, expand='space,body.view')

print(json.dumps(results))
