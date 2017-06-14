#!/usr/bin/env python
# -*- coding: utf-8 -*-

import constants


#  Create dictionary with multilingual data.

page_to_words = {}


# Multilingual data for the 'not-found' page.

page_to_words['not-found'] = {
  'english': {
    'title': """Oops!""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph_first': """Unicorns are sad because this page doesn't exist!""",
    'paragraph_second': """You can return to the <a href="/">start</a> page.""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Ой!""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph_first': """Единороги грустны, потому что такой страницы не существует!""",
    'paragraph_second': """Вы можете вернуться в <a href="/">начало</a>.""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }  
}


# Multilingual data for the 'index' page.

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


# Multilingual data for the 'greeting' page.

page_to_words['greeting'] = {
  'english': {
    'title': """A simple check.""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph_first': """First of all, we need to sure that you're a real caticorn. So are you the caticorn?""",
    'paragraph_second': """Please say only true! (We have a special polygraph for the caticorns.)""",
    'radio_button_first': """I'm a real caticorn. (Meow!)""",
    'radio_button_second': """Maybe I'm a caticorn. I don't know exactly. (What's going on?)""",
    'radio_button_third': """No. I'm a usual person. (I use subway. I sleep and eat every day.)""",
    'radio_button_fourth': """Who is a caticorn? (You guys are crazy.)""",
    'button_title': """send""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Простая проверка.""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph_first': """Прежде всего, нам бы хотелось убедиться, что вы настоящий единокот.<br>Итак, вы точно 
      единокот? Пожалуйста, говорите только правду!""",
    'paragraph_second': """(Мы располагаем специальным полиграфом для единокотов.)""",
    'radio_button_first': """Да, я единокот. (Мяу!)""",
    'radio_button_second': """Возможно, я единокот. Я точно не знаю. (Я не понимаю, что происходит.)""",
    'radio_button_third': """Нет, я обыкновенный человек. (Езжу в метро. Ем. Сплю.)""",
    'radio_button_fourth': """Кто такой единокот? (Вы, ребята, совсем сумасшедшие.)""",
    'button_title': """клик""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


# Multilingual data for the 'catification/whois' page.

page_to_words['catif-whois'] = {
  'english': {
    'title': """Who are the caticorns?""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph': """Caticorns are the magic cute creatures. They live in Catiland.<br>They like chocolate, milk and 
      psychology.<br>(And also they like the unicorns. And the unicorns like caticorns.)""",
    'button_title': """back""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Кто такие единокоты?""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """Единокоты это милые волшебные существа. Они живут в Котоландии и любят шоколад, молоко, 
      психологию.<br>(И единорогов. А единороги - их.)""",
    'button_title': """назад""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


# Multilingual data for the 'catification/no' page.

page_to_words['catif-no'] = {
  'english': {
    'title': """Sorry, the unicorns don't like usual people.""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph': """Oh, it's so sad that you're an usual person! Unfortunately, you should leave this place. You should 
      do your usual human chores.""",
    'button_title': """back""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Единороги не любят обычных людей.""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """О, это так грустно, что вы обычный человек! К сожалению, вы должны покинуть это место. Вам 
      необходимо заняться обыкновенными человеческими делами.""",
    'button_title': """назад""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


# Multilingual data for the 'catification/maybe' page.

page_to_words['catif-maybe'] = {
  'english': {
    'title': """You don't know who are you?""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph': """You need to be more opinionated. It's very important. Believe me!""",
    'button_title': """back""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Вы не знаете, кто вы?""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """Вам надо быть более уверенным человеком.<br>Это важно, поверьте мне!""",
    'button_title': """назад""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


# Multilingual data for the 'catification/yes' page.

page_to_words['catif-yes'] = {
  'english': {
    'title': """Yay! Maybe you're a real caticorn!""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph': """We would suggest you pass a simple test to sure that you know enough about the unicorns.<br>(No one 
      unicorn was hurt during this test creation.)""",
    'button_title_first': """back""",
    'button_title_second': """start""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Ура! Наконец-то здесь потенциальный единокот!""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """Мы предлагаем вам пройти тест на знание единорогов.<br>(При подготовке данного теста ни один 
      единорог не пострадал.)""",
    'button_title_first': """назад""",
    'button_title_second': """начать""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


def apply(page_name, page_html):
  page_dictionary = page_to_words[page_name]
  in_specified_lang = page_dictionary[constants.SELECTED_LANG]
  if constants.SELECTED_LANG == 'russian':
    in_specified_lang = {key: value.decode(constants.UTF8) for key, value in in_specified_lang.items()}
  return page_html.format(**in_specified_lang)