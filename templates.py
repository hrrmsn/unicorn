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
    'paragraph': """We would suggest you pass a simple test to sure that you know enough about the unicorns. (No one 
      unicorn was hurt during this test creation. Probably. We don't sure.)""",
    'button_title_first': """back""",
    'button_title_second': """start""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Ура! Наконец-то здесь потенциальный единокот!""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """Мы предлагаем вам пройти тест на знание единорогов. (При подготовке данного теста ни один 
      единорог не пострадал. Наверное. Мы не уверены.)""",
    'button_title_first': """назад""",
    'button_title_second': """начать""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  }
}


# Multilingual data for the 'test' page.

page_to_words['test'] = {
  'english': {
    'title': """Show me how well you know the unicorns!""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'paragraph': """Please be careful and attentive! The result of this test is very important. (We will give you a 
      special unicorn's license if your score will be more than 8/10. Good luck!)""",

    'first_question_label': """1. Who are the unicorns?""",
    'first_question_option_one': """I don't know.""",
    'first_question_option_two': """It's the most beautiful creatures around the world.""",
    'first_question_option_three': """Kind of fruits.""",

    'second_question_label': """2. What is a favourite color of the unicorns?""",
    'second_question_option_one': """They have no the favourite color. (Poor creatures!)""",
    'second_question_option_two': """What is the color mean? (I'm five years old baby.)""",
    'second_question_option_three': """Dark blue.""",

    'third_question_label': """3. How old are the unicorns?""",
    'third_question_option_one': """Twenty six years old.""",
    'third_question_option_two': """Twenty six thousands years old.""",
    'third_question_option_three': """Infinity.""",

    'fourth_question_label': """4. Do unicorns love caticorns?""",
    'fourth_question_option_one': """Yes. (Quietly and hesitantly.)""",
    'fourth_question_option_two': """Of course. (Muffled.)""",
    'fourth_question_option_three': """Definetly yes! Oh my god, the unicorns love caticorns so much! (Very loudly 
      and expressively.)""",

    'fifth_question_label': """5. What kind of music do unicorns prefer?""",
    'fifth_question_option_one': """They like music of Stanislav Mikhaylov.""",
    'fifth_question_option_two': """They don't like music. (It's not helpful for ears!)""",
    'fifth_question_option_three': """Something like <a href="https://fazerdaze.bandcamp.com/track/take-it-slow">
      this</a>.""",

    'sixth_question_label': """6. Do unicorns like to cook?""",
    'sixth_question_option_one': """No, they don't. (There are a lot of super markets with prepared food.)""",
    'sixth_question_option_two': """They cook every day! (Oh, the cooking is happiness.)""",
    'sixth_question_option_three': """The caticorns will cook for unicorns. <span class="red-heart">&hearts;</span>""",

    'seventh_question_label': """7. The unicorns are perfect pilots of the space ships, aren't they?""",
    'seventh_question_option_one': """Maybe. (I have some doubts.)""",
    'seventh_question_option_two': """Yes!""",
    'seventh_question_option_three': """No.""",

    'eighth_question_label': """8. What flows through the veins of unicorns?""",
    'eighth_question_option_one': """A red blood.""",
    'eighth_question_option_two': """A blue blood.""",
    'eighth_question_option_three': """Chocolate! (Hush, it's a secret!)""",

    'ninth_question_label': """9. Are unicorns cute?""",
    'ninth_question_option_one': """No! (I hate unicorns.)""",
    'ninth_question_option_two': """Maybe they are cute. (But most likely that they are usual.)""",
    'ninth_question_option_three': """Yeah! (Unicorns are so nice!)""",

    'tenth_question_label': """10. The unicorn entered to a room and he is smiling. Why?""",
    'tenth_question_option_one': """He gone crazy!""",
    'tenth_question_option_two': """Just for fun.""",
    'tenth_question_option_three': """The caticorn is inside this room. <span class="red-heart">&hearts;</span>""",    

    'button_title': """check""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Покажите мне, насколько хорошо вы знаете единорогов!""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'paragraph': """Пожалуйста, будьте внимательны и осторожны! Результаты данного теста крайне важны. (Мы выдадим вам 
      специальную лицензию единорогов только, если вы наберете не менее 8/10 очков. Удачи!)""",

    'first_question_label': """1. Кто такие единороги?""",
    'first_question_option_one': """Я не знаю.""",
    'first_question_option_two': """Это самые прекрасные существа во всем мире.""",
    'first_question_option_three': """Вид фруктов.""",

    'second_question_label': """2. Какой любимый цвет у единорогов?""",
    'second_question_option_one': """У них нет любимого цвета. (Бедные существа!)""",
    'second_question_option_two': """Что такое цвет? (Я пятилетний ребенок.)""",
    'second_question_option_three': """Темно-синий.""",

    'third_question_label': """3. Сколько лет единорогам?""",
    'third_question_option_one': """Двадцать шесть лет.""",
    'third_question_option_two': """Двадцать шесть тысяч лет.""",
    'third_question_option_three': """Бесконечность.""",

    'fourth_question_label': """4. Любят ли единороги единокотов?""",
    'fourth_question_option_one': """Да. (Тихо и неуверенно.)""",
    'fourth_question_option_two': """Конечно. (Приглушенно.)""",
    'fourth_question_option_three': """Определенно, да! О боже мой, как сильно единороги любят единокотиков! (Очень 
      громко и экспрессивно.)""",

    'fifth_question_label': """5. Какую музыку предпочитают единороги?""",
    'fifth_question_option_one': """Им нравится Станислав Михайлов.""",
    'fifth_question_option_two': """Они не любят музыку. (Это вредно для ушей!)""",
    'fifth_question_option_three': """Что-нибудь вроде <a href="https://fazerdaze.bandcamp.com/track/take-it-slow">
      этого</a>.""",

    'sixth_question_label': """6. Любят ли единороги готовить?""",
    'sixth_question_option_one': """Нет, не любят. (Ведь так много магазинов с готовой едой!)""",
    'sixth_question_option_two': """Они готовят каждый день! (О, кулинария это счастье.)""",
    'sixth_question_option_three': """Единокотики станут готовить для единорогов. <span class="red-heart">&hearts;
      </span>""",

    'seventh_question_label': """7. Единороги отличные пилоты космических кораблей, не так ли?""",
    'seventh_question_option_one': """Возможно. (У меня есть сомнения.)""",
    'seventh_question_option_two': """Да!""",
    'seventh_question_option_three': """Нет.""",

    'eighth_question_label': """8. Что течет по венам единорогов?""",
    'eighth_question_option_one': """Красная кровь.""",
    'eighth_question_option_two': """Голубая кровь.""",
    'eighth_question_option_three': """Шоколад! (Тсс! Это секрет.)""",

    'ninth_question_label': """9. Единороги милые?""",
    'ninth_question_option_one': """Нет! (Я ненавижу единорогов.)""",
    'ninth_question_option_two': """Может быть, они милые. (Но скорее всего, они обычные.)""",
    'ninth_question_option_three': """Ага! (Единороги такие хорошенькие!)""",

    'tenth_question_label': """10. Единорог вошел в комнату и улыбается. Почему?""",
    'tenth_question_option_one': """Он сошел с ума!""",
    'tenth_question_option_two': """Просто для удовольствия.""",
    'tenth_question_option_three': """В комнате есть единокот. <span class="red-heart">&hearts;</span>""",

    'button_title': """проверить""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  },
}


# Multilingual data for the 'result' page.

page_to_words['result-good'] = {
  'english': {
    'title': """Congratulate!""",
    'score-value': """{score}""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'image-name': 'dancing-jake',
    'paragraph': """You result is {score}/10. Good job! You earned your bounty! Now you are lucky owner of the 
      unicorn's license. (Yay!)""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Поздравляем!""",
    'score-value': """{score}""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'image-name': 'dancing-jake',
    'paragraph': """Ваш результат: {score}/10. Отличная работа! Вы заслужили вашу награду! Теперь вы счастливый 
      обладатель лицензии единорогов. (Ура!)""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  },
}

page_to_words['result-bad'] = {
  'english': {
    'title': """You need to learn more about the unicorns!""",
    'score-value': """{score}""",
    'label': """language""",
    'select_english_option': """english""",
    'select_russian_option': """russian""",
    'image-name': 'sad-finn',
    'paragraph': """You result is {score}/10. Please don't worry! You can try another 
      <a id="pass-test-again" href="/test">attempt</a>!""",
    'footer': """&copy; 2017 Ivan, Lina &amp; Unicorns Ltd. All rights reserved."""
  },
  'russian': {
    'title': """Вам необходимо узнать больше о единорогах!""",
    'score-value': """{score}""",
    'label': """язык""",
    'select_english_option': """английский""",
    'select_russian_option': """русский""",
    'image-name': 'sad-finn',
    'paragraph': """Ваш результат: {score}/10. Пожалуйста, не беспокойтесь! Вы можете предпринять новую 
      <a id="pass-test-again" href="/test">попытку</a>!""",
    'footer': """&copy; 2017 ОАО Иван, Лина &amp; Единороги. Все права защищены."""
  },
}


def apply(page_name, page_html):
  page_dictionary = page_to_words[page_name]
  in_specified_lang = page_dictionary[constants.SELECTED_LANG]
  if constants.SELECTED_LANG == 'russian':
    in_specified_lang = {key: value.decode(constants.UTF8) for key, value in in_specified_lang.items()}
  return page_html.format(**in_specified_lang)