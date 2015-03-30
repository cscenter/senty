# encoding: utf-8
__author__ = 'alexander'
import json
import os
from pymystem3 import Mystem
#подключаемся к json-ам с оценкой
directory = 'materials'
#вычисляем, сколько в директории лежит файлов
number_of_input_files = len(filter(lambda x: not x.endswith('~'), os.listdir(directory)))
output_data = {}
#count_of_good_marks = 0
#count_of_bad_marks = 0
list_of_all_terms = {}
#иду по документам
for i in range(1, number_of_input_files + 1):
    with open('materials/' + str(i)) as data_file:
        data = json.load(data_file)
    #нормализую слова из сообщения
    m = Mystem()
    list_of_terms = filter(lambda x: not x == ' ', m.lemmatize(data['text']))
    #убираю повторяющиеся слова
    list_of_unique_terms = set(list_of_terms)
    #формирую draft выходного json файла
    output_data[i] = {}
    output_data[i]['id'] = data['id']
    output_data[i]['mark'] = data['mark']
    output_data[i]['terms'] = {}
    #иду по списку не повторяющихся терминов из документа и заполняю общий словарь
    #термов, где ключом является наименование терма, а значением - количество документов, его содержащие(нужно для idf),
    #параллельно вычисляю tf для каждого терма и документа i, idf вычисляю в другом цикле
    for unique_term in list_of_unique_terms:
        if not list_of_all_terms.has_key(unique_term):
            list_of_all_terms[unique_term] = 1
        else:
            list_of_all_terms[unique_term] += 1
        count_of_unique_term = 0
        for term in list_of_terms:
            if unique_term == term:
                count_of_unique_term += 1
        output_data[i]['terms'][unique_term] = {'tf': float(count_of_unique_term)/ len(list_of_terms), 'idf': 0}

for i in range(1, number_of_input_files + 1):
    for term in output_data[i]['terms']:
        output_data[i]['terms'][term]['idf'] = float(list_of_all_terms[term])/ number_of_input_files
    with open('results/' + str(i) + '_tf-idf', 'w') as output_file:
        json.dump(output_data[i], output_file)
