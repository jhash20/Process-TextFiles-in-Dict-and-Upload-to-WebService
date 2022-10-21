#!/usr/bin/env python3

"""Script that processes text files and uploads to a web service endpoing
by converting text files information (feedback) into a Python dictionary 
and then uploading to a running Django Web service by making a POST request.
Also, prints a response status code.
"""

import os
import requests
import json


directory = "/data/feedback/"
feedback_dict = {}

# iterates through entries in directory
for entry in os.listdir(directory):
  path = str(directory) + str(entry)
  # ensures that entry being iterated is a file
  if os.path.isfile(path):
    with open(path) as input:
      # splits by line and then adds the lines as values in dictionary
      input_line = input.read().split("\n")
      feedback_dict['title'] = input_line[0].strip()
      feedback_dict['name'] = input_line[1].strip()
      feedback_dict['date'] = input_line[2].strip()
      feedback_dict['feedback'] = input_line[3].strip()

      response = requests.post("http://<corpweb-external-IP>/feedback/", json=feedback_dict)
      print(response.status_code)
  else:
    print("Error: Did not process; entry is not a file: " + str(entry))

