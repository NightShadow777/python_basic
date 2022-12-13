'''
На вход функции popular_words передаются 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
При решении этой задачи обратите внимание на следующие моменты
Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
Искомые слова всегда указаны в нижнем регистре
Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
Входные параметры: Текст и массив искомых слов.

Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.

Пример:
popular_words(\'\'\'When I was One I had just begun When I was Two I was nearly new \'\'\', ['i', 'was', 'three', 'near']) ==
 { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }

Предусловия:
Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.
'''

def popular_words(text, keywords):
    text_list = text.split()
    res_dict = {}
    for text in text_list:
        for keyword in keywords:
            if keyword == text.lower():
                #print(text_list)
                n = text_list.count(text)
                res_dict[keyword] = n
            else:
                if not res_dict.get(keyword):
                    res_dict[keyword] = 0
    return res_dict

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
print(popular_words('''Interesting Facts For Curious Minds gives you the answer to all these and many many more questions that I know have crossed your mind from time to time . This book is divided into 63 chapters by topic for your convenience, bringing you a nice mix of science, history, pop culture, and all sorts of stuff in between. Each chapter contains 25 concise yet engaging factoids that are sure to make you think and at times laugh. ''', ['many', 'time', 'book', 'read']))