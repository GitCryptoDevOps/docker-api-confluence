import os
import json
from atlassian import Confluence
from pprint import pprint

import logging
logging.basicConfig(filename='run-request-in-confluence.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
cql_file = os.environ.get('CQL')

confluence = Confluence(
    url=url, 
    username=username, 
    password=password
)

with open(cql_file, 'r') as file:
    cql = file.read()
results = confluence.cql(cql)
print(json.dumps(results))
