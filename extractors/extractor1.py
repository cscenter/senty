
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
            input_files = filter(lambda x: not x.endswith('~'), os.listdir(self.input_directory))
            output_data = {}
            list_of_all_terms = {}
            m = Mystem()
            #иду по документам 
            for file in input_files:
                print file
                with open(self.input_directory + '/' + file) as data_file:
                    data = json.load(data_file)
                #нормализую слова из сообщения
                list_of_terms = filter(lambda x: not x == ' ', m.lemmatize(data['text']))
                output_data[file] = {}
                output_data[file]['id'] = data['id']
                output_data[file]['positive'] = data['positive']
                output_data[file]['sarcasm'] = data['sarcasm']
                output_data[file]['terms'] = {}
                #убираю повторяющиеся слова
                for term in list_of_terms:
                    if term not in output_data[file]['terms']:
                        output_data[file]['terms'][term] = 1
                    else:
                        output_data[file]['terms'][term] += 1
                for term in output_data[file]['terms'].keys():
                    if term not in list_of_all_terms:
                        list_of_all_terms[term] = 1
                    else:
                        list_of_all_terms[term] += 1
                    #подсчёт tf
                    count_of_terms = output_data[file]['terms'][term]
                    output_data[file]['terms'][term] = {'tf': float(count_of_terms)/len(list_of_terms), 'idf': 0}

            for file in input_files:
                #подсчёт idf
                for term in output_data[file]['terms'].keys():
                    output_data[file]['terms'][term]['idf'] = math.log(float(len(input_files))/list_of_all_terms[term])
                #запись результата
                with open(self.output_directory + '/' + file + '_tf-idf', 'w') as output_file:
                    json.dump(output_data[file], output_file)
	except Exception:
		return False
	else:
		return True
