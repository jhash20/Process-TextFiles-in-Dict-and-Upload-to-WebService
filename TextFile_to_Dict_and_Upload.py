#!/usr/bin/env python3

import os
import requests
import json

directory = '/data/feedback/'
feedback_dict = {}

# return a list of all files and directories in specified directory
for entry in os.listdir(directory):
  path = str(directory) + str(entry)
  #check if entry is a file
  if os.path.isfile(path):
    with open(path) as input:
      input_line = input.read().splitlines()
      feedback_dict['title'] = input_line[0].strip()
      feedback_dict['name'] = input_line[1].strip()
      feedback_dict['date'] = input_line[2].strip()
      feedback_dict['feedback'] = input_line[3].strip()
      # makes a POST request to post the dictionary to company website
      response = requests.post("http://<corpweb-external-IP>/feedback/", json=feedback_dict)
      print(response.status_code)
  else:
    # prints error message that did not process entry since it wasn't a file
    print("Error: Did not process; entry is not a file: " + str(entry))

