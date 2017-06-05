#!/usr/bin/env python
# -*- coding: utf-8 -*-

import constants

page_to_words = {}

page_to_words['not-found'] = {
  'english': {
    'title': """Oops!""",
    'paragraph_first': """Unicorns are sad because this page doesn't exist!""",
    'paragraph_second': """You can return to the <a href="/">start</a> page.""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Ой!""",
    'paragraph_first': """Единороги грустны, потому что такой страницы не существует!""",
    'paragraph_second': """Вы можете вернуться в <a href="/">начало</a>.""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }  
}

page_to_words['index'] = {
  'english': {
    'title': """Hi, Kotolina! :)""",
    'paragraph_first': """Please select preferable language.""",
    'input_first': """english""",
    'input_second': """russian""",
    'button_title': """send""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Привет, Котолина! :)""",
    'paragraph_first': """Пожалуйста, выберите предпочтительный язык.""",
    'input_first': """английский""",
    'input_second': """русский""",
    'button_title': """клик""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}

def apply(page_name, page_html, selected_language):
  page_dictionary = page_to_words[page_name]
  in_specified_lang = page_dictionary[selected_language]
  if selected_language == 'russian':
    in_specified_lang = {key: value.decode(constants.UTF8) for key, value in in_specified_lang.items()}
  return page_html.format(**in_specified_lang)