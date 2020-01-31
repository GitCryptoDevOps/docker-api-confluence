import os
import json
from atlassian import Confluence
from pprint import pprint

import logging
logging.basicConfig(filename='search-in-confluence.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
keyword = os.environ.get('KEYWORD')

confluence = Confluence(
    url=url, 
    username=username, 
    password=password
)

cql = "siteSearch ~ {} order by created".format(keyword)
results = confluence.cql(cql)
print(json.dumps(results))
