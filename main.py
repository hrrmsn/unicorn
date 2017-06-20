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


def make_response(environ, start_response, not_found=False):
  parsed_qs = tools.check_post_request(environ)

  answer_type = 'index'
  if not_found:
    answer_type = 'not-found'
  elif 'answer' in parsed_qs:
    answer_type = parsed_qs['answer'].pop()
  
  response_template = 'static/html/catification/{}.html' if 'catif' in answer_type else 'static/html/{}.html'
  status = constants.STATUS_NOT_FOUND if not_found else constants.STATUS_OK

  response_body = tools.readfile(response_template.format(answer_type))
  response_body = templates.apply(answer_type, response_body)

  start_response(status, tools.get_content_headers(constants.TEXT_HTML))
  return [response_body.encode(constants.UTF8)]


def result(environ, start_response):
  parsed_qs = tools.check_post_request(environ)
  score = int(parsed_qs['score'].pop()) if 'score' in parsed_qs else 0

  for question in parsed_qs:
    answer = parsed_qs[question].pop() if parsed_qs[question] else ''
    if question in constants.TEST_ANSWERS and answer in constants.TEST_ANSWERS[question]:
      score += 1

  test_result = 'result-good' if score >= constants.UNICORN_LICENSE_SCORE_LIMIT else 'result-bad'

  response_body = tools.readfile('static/html/result.html')
  response_body = templates.apply(test_result, response_body)
  response_body = response_body.format(**{'score': score})

  start_response(constants.STATUS_OK, tools.get_content_headers(constants.TEXT_HTML))
  return [response_body.encode(constants.UTF8)]


regex_and_functions = [
  (r'/static', static),
  (r'(/$)|(/greeting$)|(/catification$)|(/test$)', make_response),
  (r'/result$', result)
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
  return make_response(environ, start_response, not_found=True)