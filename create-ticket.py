import os
from pprint import pprint
from atlassian import Jira

import logging
logging.basicConfig(filename='create-ticket.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
project = os.environ.get("PROJECT")
issue_type = os.environ.get("ISSUE_TYPE")
summary = os.environ.get("SUMMARY")
description_file = os.environ.get('DESCRIPTION')

jira = Jira(
    url=url, 
    username=username, 
    password=password
)

with open("{}.md".format (description_file), 'r') as file:
    description = file.read()
response = jira.issue_create(fields={
    'project': {'key': project},
    'issuetype': {
        "name": issue_type
    },
    'summary': summary,
    'description': description,
})
issue_id = response['key']
print (issue_id)
