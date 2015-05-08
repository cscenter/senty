# encoding: UTF-8
import json
import os
import math

class extractor:
    def __init__(self, middle_directory, output_directory):
        self.output_directory = output_directory
        self.middle_directory = middle_directory

    def extract(self):
        try:
            #вычисляем, сколько в директории лежит файлов
            input_files = filter(lambda x: not x.endswith('~'), os.listdir(self.middle_directory))
            output_data = {}
            list_of_all_terms = {}
            #иду по документам
            for input_file in input_files:
                with open(self.middle_directory + '/' + input_file) as data_file:
                    data = json.load(data_file)
                list_of_terms = filter(lambda x: x not in (' ', '', '\n'), data['text'].split(' '))
                output_data[input_file] = {}
                output_data[input_file]['id'] = data['id']
                output_data[input_file]['positive'] = data['positive']
                output_data[input_file]['sarcasm'] = data['sarcasm']
                output_data[input_file]['terms'] = {}
                #убираю повторяющиеся слова
                for term in list_of_terms:
                    if term not in output_data[input_file]['terms']:
                        output_data[input_file]['terms'][term] = 1
                    else:
                        output_data[input_file]['terms'][term] += 1
                for term in output_data[input_file]['terms'].keys():
                    if term not in list_of_all_terms:
                        list_of_all_terms[term] = 1
                    else:
                        list_of_all_terms[term] += 1
                    #подсчёт tf
                    count_of_terms = output_data[input_file]['terms'][term]
                    output_data[input_file]['terms'][term] = {'tf': float(count_of_terms)/len(list_of_terms), 'idf': 0,
                                                        'count': count_of_terms}

            for input_file in input_files:
                #подсчёт idf
                for term in output_data[input_file]['terms'].keys():
                    output_data[input_file]['terms'][term]['idf'] = math.log(float(len(input_files))/list_of_all_terms[term])
                #запись результата
                with open(self.output_directory + '/' + input_file + '_tf-idf', 'w') as output_file:
                    json.dump(output_data[input_file], output_file)
        except Exception:
            return False
        else:
            return True

#features
#features.mystem_using('materials', 'materials1')
#features.n_gram_feature(3, 'materials1')
#features.more_than_n_gram_feature(3, 'materials1')


#my_extractor = extractor('materials1', 'results')
#my_extractor.extract()


