# encoding: UTF-8
import re
import json
import os
import math
from pymystem3 import Mystem
class standard_extractor:
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
                with open(self.input_directory + '/' + file) as data_file:
                    data = json.load(data_file)
                list_of_terms = filter(lambda x: x != "", re.split(""" |\.|,|:|\?|"|\n|<|>|\*|!|@|_ +""", data['text']))
                text = " ".join(["%s" % term for term in list_of_terms])
                list_of_terms = filter(lambda x: x not in (" ", "\n"), m.lemmatize(text))


                # обработка не + (слово)
                nums_of_bigrams = []
                helping_words = [u'совсем', u'очень', u'слишком', u'самый']
                for i in range(0, len(list_of_terms)):
                    if list_of_terms[i] == u'не' and list_of_terms[i+1] not in helping_words:
                        nums_of_bigrams.append((i, i+1))
                    elif list_of_terms == u'не' and list_of_terms[i+1] in helping_words:
                        nums_of_bigrams.append((i, i+2))
                for i in range(0, len(nums_of_bigrams)):
                    if nums_of_bigrams[i][0] + 1 == nums_of_bigrams[i][1]:
                        list_of_terms[nums_of_bigrams[i][0]] = list_of_terms[nums_of_bigrams[i][0]] + ' ' + list_of_terms[nums_of_bigrams[i][1]]
                        list_of_terms[nums_of_bigrams[i][1]] = ''
                    elif nums_of_bigrams[i][0] + 2 == nums_of_bigrams[i][1]:
                        list_of_terms[nums_of_bigrams[i][0]] = list_of_terms[nums_of_bigrams[i][0]] + ' ' + list_of_terms[nums_of_bigrams[i][1]]
                        list_of_terms[nums_of_bigrams[i][1] - 1] = ''
                        list_of_terms[nums_of_bigrams[i][1]] = ''
                list_of_terms = filter(lambda x: x != '', list_of_terms)

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
                    output_data[file]['terms'][term] = {'tf': float(count_of_terms)/len(list_of_terms), 'idf': 0,
                                                        'count': count_of_terms}

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
         
'''                    
my_extractor = standard_extractor('materials', 'results')
my_extractor.extract()
'''

