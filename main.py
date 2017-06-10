#!/usr/bin/env python

import re

import tools
import constants
import templates


# Entry points.

def static(environ, start_response):
  file_path = environ['PATH_INFO'].strip('/')
  response_body = tools.readfile(file_path)

  content_type = 'application/octet-stream'
  if file_path.endswith('.html'):
    content_type = constants.TEXT_HTML
  elif file_path.endswith('.css'):
    content_type = constants.TEXT_CSS
  elif file_path.endswith('.jpg'):
    content_type = constants.IMAGE_JPEG

  start_response('200 OK', tools.get_content_headers(content_type))
  return [response_body if file_path.endswith('.jpg') else response_body.encode(constants.UTF8)]


def index(environ, start_response):
  response_body = tools.readfile('static/html/index.html')
  response_body = templates.apply('index', response_body)
  start_response('200 OK', tools.get_content_headers(constants.TEXT_HTML))
  return [response_body.encode(constants.UTF8)]


def not_found(environ, start_response):
  tools.check_query_string(environ)

  response_body = tools.readfile('static/html/not-found.html')
  response_body = templates.apply('not-found', response_body)
  start_response('200 OK', tools.get_content_headers(constants.TEXT_HTML))
  return [response_body.encode(constants.UTF8)]


def greeting(environ, start_response):
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0

  tools.check_query_string(environ)

  request_body = environ['wsgi.input'].read(request_body_size)
  if request_body:
    request_body = request_body.lower()
    constants.SELECTED_LANG = re.match(r'language=(\w+)', request_body).group(1)

  response_body = tools.readfile('static/html/greeting.html')
  response_body = templates.apply('greeting', response_body)

  start_response('200 OK', tools.get_content_headers(constants.TEXT_HTML))
  return [response_body.encode(constants.UTF8)]


regex_and_functions = [
  (r'/$', index),
  (r'/static.*', static),
  (r'/greeting$', greeting)
]


# Main function of WSGI app.

def application(environ, start_response):
  # response_body = ''
  # for key in environ:
  #   response_body += '{} -> {}\n'.format(key, str(environ[key]))

  # start_response('200 OK', tools.get_content_headers('text/plain'))
  # return [response_body.encode(constants.UTF8)]

  # if environ['REQUEST_METHOD'].lower() == 'post':
  #   return handle_post(environ, start_response)

  
  for regex_and_function in regex_and_functions:
    regex, function = regex_and_function[0], regex_and_function[1]
    if re.match(regex, environ['PATH_INFO']):
      return function(environ, start_response)
  return not_found(environ, start_response)