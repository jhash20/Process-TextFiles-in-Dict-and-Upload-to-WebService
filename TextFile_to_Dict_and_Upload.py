#!/usr/bin/env python3

import os
import requests

directory = '/data/feedback/'
feedback_dict = {}

# return a list of all files and directories in specified directory
for entry in os.listdir(directory):
  #check if entry is a file
  if os.path.isfile(entry):
    with open(str(directory) + str(entry)) as input:
      input_line = input.read().split('/n')
      feedback_dict['title'] = input_line[0]
      feedback_dict['name'] = input_line[1]
      feedback_dict['date'] = input_line[2]
      feedback_dict['date'] = input_line[2:]
  else:
    # prints error message that did not process entry since it wasn't a file
    print("Error: Did not process; entry is not a file: " + str(entry))
# makes a POST request to post the dictionary to company website
requests.post(http://<corpweb-external-IP>/feedback, data=feedback_dict)
