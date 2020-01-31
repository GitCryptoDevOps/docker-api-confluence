import os
import json
from pprint import pprint
from atlassian import Jira

import logging
logging.basicConfig(filename='run-request-in-jira.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
jql_file = os.environ.get("JQL")

jira = Jira(
    url=url, 
    username=username, 
    password=password
)

with open("{}.jql".format (jql_file), 'r') as file:
    jql = file.read()
results = jira.jql(jql)
print(json.dumps(results))
