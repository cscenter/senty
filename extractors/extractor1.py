# encoding: UTF-8
import json
import os
import math
from pymystem3 import Mystem
class extractor:
    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def extract(self):
        try:
            #вычисляем, сколько в директории лежит файлов
            number_of_input_files = len(filter(lambda x: not x.endswith('~'), os.listdir(self.input_directory)))
            output_data = {}
            #count_of_good_marks = 0
            #count_of_bad_marks = 0
            list_of_all_terms = {}
            #иду по документам
            for i in range(1, number_of_input_files + 1):
                with open(self.input_directory + '/' + str(i)) as data_file:
                    data = json.load(data_file)
                #нормализую слова из сообщения
                m = Mystem()
                list_of_terms = filter(lambda x: not x == ' ', m.lemmatize(data['text']))
                output_data[i] = {}
                output_data[i]['id'] = data['id']
                output_data[i]['mark'] = data['mark']
                output_data[i]['terms'] = {}
                #убираю повторяющиеся слова
                for term in list_of_terms:
                    if term not in output_data[i]['terms']:
                        output_data[i]['terms'][term] = 1
                    else:
                        output_data[i]['terms'][term] += 1
                for term in output_data[i]['terms'].keys():
                    if term not in list_of_all_terms:
                        list_of_all_terms[term] = 1
                    else:
                        list_of_all_terms[term] += 1
                    #подсчёт tf
                    count_of_terms = output_data[i]['terms'][term]
                    output_data[i]['terms'][term] = {'tf': float(count_of_terms)/len(list_of_terms), 'idf': 0}

            for i in range(1, number_of_input_files + 1):
                #подсчёт idf
                for term in output_data[i]['terms'].keys():
                    output_data[i]['terms'][term]['idf'] = math.log(float(number_of_input_files)/list_of_all_terms[term])
                #запись результата
                with open(self.output_directory + '/' + str(i) + '_tf-idf', 'w') as output_file:
                    json.dump(output_data[i], output_file)
        except Exception:
            return False
        else:
            return True
#how to use
'''my_extractor = extractor('materials', 'results')
if my_extractor.extract():
    print 'All right'
else:
    print 'Not all right
'''
