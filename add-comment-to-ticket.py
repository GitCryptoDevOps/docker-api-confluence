import os
from pprint import pprint
from atlassian import Jira

import logging
logging.basicConfig(filename='add-comment-to-ticket.log',level=logging.DEBUG)

url = os.environ.get('URL')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
issue = os.environ.get('ISSUE')
comment_file = os.environ.get('COMMENT')

jira = Jira(
    url=url, 
    username=username, 
    password=password
)

with open("{}.md".format (comment_file), 'r') as file:
    comment = file.read()
response = jira.issue_add_comment(issue, comment)
print (response["updated"])
