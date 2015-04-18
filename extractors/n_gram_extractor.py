# encoding: UTF-8
import re
import json
import os
import math
from pymystem3 import Mystem
class n_gramm_extractor:
    def __init__(self, input_directory, output_directory, n):
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.n = n
    def extract(self):
        try:
            #вычисляем, сколько в директории лежит файлов
            input_files = filter(lambda x: not x.endswith('~'), os.listdir(self.input_directory))
            output_data = {}
            list_of_all_n_grams = {}
            m = Mystem()
            #иду по документам
            for file in input_files:
                with open(self.input_directory + '/' + file) as data_file:
                    data = json.load(data_file)
                list_of_terms = filter(lambda x: x != "", re.split(""" |\.|,|:|\?|"|\n|<|>|\*|!|@|_ +""", data['text']))
                text = " ".join(["%s" % term for term in list_of_terms])
                list_of_terms = filter(lambda x: x not in (" ", "\n"), m.lemmatize(text))
                list_of_n_grams_tuples = zip(*[list_of_terms[i:] for i in range(self.n)])
                list_of_n_grams_strings = []
                for gram_tuple in list_of_n_grams_tuples:
                    string_of_n_gram = " ".join(["%s" % term for term in gram_tuple])
                    list_of_n_grams_strings.append(string_of_n_gram)
                output_data[file] = {}
                output_data[file]['id'] = data['id']
                output_data[file]['positive'] = data['positive']
                output_data[file]['sarcasm'] = data['sarcasm']
                output_data[file]['terms'] = {}
                #убираю повторяющиеся слова
                for gram in list_of_n_grams_strings:
                    if gram not in output_data[file]['terms']:
                        output_data[file]['terms'][gram] = 1
                    else:
                        output_data[file]['terms'][gram] += 1
                for gram in output_data[file]['terms'].keys():
                    if gram not in list_of_all_n_grams:
                        list_of_all_n_grams[gram] = 1
                    else:
                        list_of_all_n_grams[gram] += 1
                    #подсчёт tf
                    count_of_n_grams = output_data[file]['terms'][gram]
                    output_data[file]['terms'][gram] = {'tf': float(count_of_n_grams)/len(list_of_n_grams_strings), 'idf': 0}

            for file in input_files:
                #подсчёт idf
                for gram in output_data[file]['terms'].keys():
                    output_data[file]['terms'][gram]['idf'] = math.log(float(len(input_files))/list_of_all_n_grams[gram])
                #запись результата
                with open(self.output_directory + '/' + file + '_tf-idf', 'w') as output_file:
                    json.dump(output_data[file], output_file)
        except Exception:
            return False
        else:
            return True

#my_extractor = n_gramm_extractor('materials', 'results', 3)
#my_extractor.extract()

