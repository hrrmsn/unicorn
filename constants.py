#!/usr/bin/env python

import base64

TEXT_HTML = 'text/html'
TEXT_PLANE = 'text/plane'
TEXT_CSS = 'text/css'
IMAGE_JPEG = 'image/jpeg'

UTF8 = 'utf-8'

SELECTED_LANG = 'english'

STATUS_OK = '200 OK'
STATUS_NOT_FOUND = '400 NOT FOUND'

TEST_ANSWERS = {
  'first_question': ['two'],
  'second_question': ['three'],
  'third_question': ['one'],
  'fourth_question': ['three'],
  'fifth_question': ['three'],
  'sixth_question': ['two', 'three'],
  'seventh_question': ['two'],
  'eighth_question': ['three'],
  'ninth_question': ['three'],
  'tenth_question': ['three']
}

UNICORN_LICENSE_SCORE_LIMIT = 8

MY_EMAIL_ENCODED = 'aHJybXNuQHlhbmRleC5ydQ=='
MY_MAILGUN_DOMAIN_NAME_ENCODED = 'c2FuZGJveDk0OGJjMWJkNzQ5MjRkMjU5MGFiNzFlYzI5MTYzNTM5Lm1haWxndW4ub3Jn'
MY_MAILGUN_API_KEY_ENCODED = 'a2V5LTM0M2Y1MGYxZjAzOTNiOGUyYTA1NDAyMGQxZmIyNjI1'

MY_EMAIL = base64.b64decode(MY_EMAIL_ENCODED)
MY_MAILGUN_DOMAIN_NAME = base64.b64decode(MY_MAILGUN_DOMAIN_NAME_ENCODED)
MY_MAILGUN_API_KEY = base64.b64decode(MY_MAILGUN_API_KEY_ENCODED)

HAVE_UNICORNS_BEEN_INFORMED = False

IMAGE_NAMES_BY_CATIF_TYPE = {
  'catif-maybe': 'caticorn-crying',
  'catif-no': 'caticorn-sad',
  'catif-whois': 'who-are-the-caticorns'
}