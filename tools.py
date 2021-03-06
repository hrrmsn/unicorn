#!/usr/bin/env python

import os
import urlparse
import requests

import constants


# Helper functions.

def get_content_headers(content_type):
  return [('Content-type', content_type)]


def readfile(filepath):
  file_content = 'Error when reading from the file: \'{}\'.'.format(filepath)
  if os.path.exists(filepath):
    with open(filepath, 'r') as f:
      file_content = f.read() if filepath.endswith('.jpg') else f.read().decode(constants.UTF8)
  return file_content


def check_post_request(environ):
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0

  request_body = environ['wsgi.input'].read(request_body_size)
  request_body = request_body.lower()

  parsed_qs = urlparse.parse_qs(request_body)
  if 'language' in parsed_qs:
    constants.SELECTED_LANG = parsed_qs['language'].pop()
  return parsed_qs


def send_email_to_me(subject, text):
  return requests.post(
    'https://api.mailgun.net/v3/{}/messages'.format(constants.MY_MAILGUN_DOMAIN_NAME),
    auth=('api', constants.MY_MAILGUN_API_KEY),
    data={'from': 'Mailgun API <mailgun@{}>'.format(constants.MY_MAILGUN_DOMAIN_NAME),
          'to': [constants.MY_EMAIL],
          'subject': subject,
          'text': text})
