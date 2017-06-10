#!/usr/bin/env python

import os

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


def check_query_string(environ):
  if environ['QUERY_STRING'] == 'lang=rus':
    constants.SELECTED_LANG = 'russian'
  elif environ['QUERY_STRING'] == 'lang=eng':
    constants.SELECTED_LANG = 'english'  