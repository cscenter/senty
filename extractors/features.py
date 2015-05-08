# encoding: UTF-8
from pymystem3 import Mystem
import json
import os
import re

def mystem_using(input_directory, output_directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(input_directory))
    output_data = {}
    m = Mystem()
    for input_file in input_files:
        with open(input_directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x != '', re.split(''' |\.|,|:|\?|"|\n|<|>|\*|!|@|_ +''', data['text']))
        text = " ".join(["%s" % term for term in list_of_terms])
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), m.lemmatize(text))
        text_of_output = ' '.join(['%s' % term for term in list_of_terms])
        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(output_directory + '/' + input_file, 'w') as output_file:
                    json.dump(output_data[input_file], output_file)

def n_gram_feature(n, directory):
    #вычисляем, сколько в директории лежит файлов
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in (" ", "\n"), data['text'].split(' '))
        list_of_n_grams_tuples = zip(*[list_of_terms[i:] for i in range(n)])
        list_of_n_grams_strings = []
        for gram_tuple in list_of_n_grams_tuples:
            string_of_n_gram = ''.join(["%s" % term for term in gram_tuple])
            list_of_n_grams_strings.append(string_of_n_gram)

        text_of_output = ' '.join(["%s" % n_gram_string for n_gram_string in list_of_n_grams_strings])
        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def more_than_n_gram_feature(n, directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in (" ", "\n"), data['text'].split(' '))
        list_of_n_grams_tuples = {}
        for j in range(0, n):
            list_of_n_grams_tuples[j] = zip(*[list_of_terms[i:] for i in range(j + 1)])
        list_of_n_grams_strings = []
        for j in range(0, n):
            for gram_tuple in list_of_n_grams_tuples[j]:
                string_of_n_gram = ''.join(['%s' % term for term in gram_tuple])
                list_of_n_grams_strings.append(string_of_n_gram)
        text_of_output = ' '.join(['%s' % n_gram_string for n_gram_string in list_of_n_grams_strings])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)