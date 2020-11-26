from translate import Translator as Trn
from googletrans import Translator
import goslate
from textblob import TextBlob

"""
# variant 1. Unstable work due to google token issues
translator = Translator()
with open('text_file_hw5-04-final.txt', 'w', encoding='utf-8') as dest_file:
    with open('text_file_hw5-04.txt', 'r', encoding='utf-8') as init_file:
        data = init_file.read().split('\n')
        for elem in data:
            word = elem.split(' ')
            new_word = translator.translate(word[0], src='en', dest='ru').text
            print(f"{new_word} {word[1]} {word[2]}", file=dest_file)


# variant 2 Awful translation
translator_second = Trn(from_lang="English", to_lang = "Russian")
with open('text_file_hw5-04-final02.txt', 'w', encoding='utf-8') as dest_file_2:
    with open('text_file_hw5-04.txt', 'r', encoding='utf-8') as init_file:
        data = init_file.read().split('\n')
        for elem in data:
            word = elem.split(' ')
            new_word = translator_second.translate(word[0])
            print(f"{new_word} {word[1]} {word[2]}", file=dest_file_2)


# variant 3 sometimes works (if error 429 is not appeared)
with open('text_file_hw5-04-final03.txt', 'w', encoding='utf-8') as dest_file_3:
    with open('text_file_hw5-04.txt', 'r', encoding='utf-8') as init_file:
        data = init_file.read().split('\n')
        gs = goslate.Goslate()
        for elem in data:
            word = elem.split(' ')
            new_word = gs.translate(word[0], 'ru')
            print(f"{new_word} {word[1]} {word[2]}", file=dest_file_3)
"""
# variant 4 the most stable for now
with open('text_file_hw5-04-final04.txt', 'w', encoding='utf-8') as dest_file_4:
    with open('text_file_hw5-04.txt', 'r', encoding='utf-8') as init_file:
        data = init_file.read().split('\n')
        for elem in data:
            word = elem.split(' ')
            blob = TextBlob(word[0])
            new_word = blob.translate(to='ru')
            print(f"{new_word} {word[1]} {word[2]}", file=dest_file_4)
