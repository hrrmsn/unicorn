#!/usr/bin/env python

import os

# Helper functions.

def get_content_headers(content_type):
  return [('Content-type', content_type)]


def readfile(filepath):
  file_content = 'Error when reading from the file: \'{}\'.'.format(filepath)
  if os.path.exists(filepath):
    with open(filepath, 'r') as f:
      file_content = f.read()
  return file_content