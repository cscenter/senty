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


def mystem_using_with_considering_of_multiple_letters(input_directory, output_directory):
        input_files = filter(lambda x: not x.endswith('~'), os.listdir(input_directory))
        output_data = {}
        m = Mystem()
        #иду по документам
        for input_file in input_files:
            with open(input_directory + '/' + input_file) as data_file:
                data = json.load(data_file)
            list_of_terms = filter(lambda x: x != '', re.split(''' |\.|,|:|\?|"|\n|<|>|\*|!|@|_ +''', data['text']))
            my_list_of_terms = []
            for term in list_of_terms:
                if term == m.lemmatize(term)[0]:
                    my_term = term
                    term = u''
                    prev_letter = my_term[0]
                    term += my_term[0]
                    for i in range(1, len(my_term)):
                        if my_term[i] != prev_letter:
                            term += my_term[i]
                        prev_letter = my_term[i]
                    my_list_of_terms.append(term)
                else:
                    my_list_of_terms.append(term)
            list_of_terms = my_list_of_terms
            text = ' '.join(['%s' % term for term in list_of_terms])
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


def without_prepositions(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    m = Mystem()
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))
        my_list = list_of_terms
        list_of_terms = []
        for term in my_list:
            if m.analyze(term)[0].get(u'analysis'):
                if not m.analyze(term)[0][u'analysis'][0][u'gr'].startswith(u'PR'):
                    list_of_terms.append(term)
            else:
                list_of_terms.append(term)
        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def without_conjunctions(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    m = Mystem()
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))
        my_list = list_of_terms
        list_of_terms = []
        for term in my_list:
            if m.analyze(term)[0].get(u'analysis'):
                if not m.analyze(term)[0][u'analysis'][0][u'gr'].startswith(u'CONJ'):
                    list_of_terms.append(term)
            else:
                list_of_terms.append(term)
        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def without_pronouns(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    m = Mystem()
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))
        my_list = list_of_terms
        list_of_terms = []
        for term in my_list:
            if m.analyze(term)[0].get(u'analysis'):
                if not m.analyze(term)[0][u'analysis'][0][u'gr'].startswith((u'SPRO', u'APRO')):
                    list_of_terms.append(term)
            else:
                list_of_terms.append(term)
        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def with_not(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    m = Mystem()
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))


        # обработка не + (слово)
        nums_of_bigrams = []
        helping_words = [u'совсем', u'очень', u'слишком', u'самый']
        for i in range(0, len(list_of_terms)):
            if list_of_terms[i] == u'не' and list_of_terms[i+1] not in helping_words:
                if m.analyze(list_of_terms[i+1])[0].get(u'analysis'):
                    if not m.analyze(list_of_terms[i+1])[0][u'analysis'][0][u'gr'].startswith(u'S,'):
                        nums_of_bigrams.append((i, i+1))
            elif list_of_terms[i] == u'не' and list_of_terms[i+1] in helping_words:
                if m.analyze(list_of_terms[i+2])[0].get(u'analysis'):
                    if not m.analyze(list_of_terms[i+2])[0][u'analysis'][0][u'gr'].startswith(u'S,'):
                        nums_of_bigrams.append((i, i+2))
        for i in range(0, len(nums_of_bigrams)):
            if nums_of_bigrams[i][0] + 1 == nums_of_bigrams[i][1]:
                list_of_terms[nums_of_bigrams[i][0]] = list_of_terms[nums_of_bigrams[i][0]] + list_of_terms[nums_of_bigrams[i][1]]
                list_of_terms[nums_of_bigrams[i][1]] = ''
            elif nums_of_bigrams[i][0] + 2 == nums_of_bigrams[i][1]:
                list_of_terms[nums_of_bigrams[i][0]] = list_of_terms[nums_of_bigrams[i][0]] + list_of_terms[nums_of_bigrams[i][1]]
                list_of_terms[nums_of_bigrams[i][1] - 1] = ''
                list_of_terms[nums_of_bigrams[i][1]] = ''
        list_of_terms = filter(lambda x: x != '', list_of_terms)


        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def considering_of_multiple_letters(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))
        my_list_of_terms = []
        for term in list_of_terms:
            my_term = term
            term = u''
            prev_letter = my_term[0]
            term += my_term[0]
            for i in range(1, len(my_term)):
                if my_term[i] != prev_letter:
                    term += my_term[i]
                prev_letter = my_term[i]
            my_list_of_terms.append(term)
        list_of_terms = my_list_of_terms

        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

def without_foreign_words(directory):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(directory))
    output_data = {}
    m = Mystem()
    #иду по документам
    for input_file in input_files:
        with open(directory + '/' + input_file) as data_file:
            data = json.load(data_file)
        list_of_terms = filter(lambda x: x not in ('', ' ', '\n'), data['text'].split(' '))
        my_list = list_of_terms
        list_of_terms = []
        for term in my_list:
            if m.analyze(term)[0].get(u'analysis'):
                list_of_terms.append(term)
        text_of_output = ' '.join(['%s' % term for term in list_of_terms])

        output_data[input_file] = {}
        output_data[input_file]['id'] = data['id']
        output_data[input_file]['positive'] = data['positive']
        output_data[input_file]['sarcasm'] = data['sarcasm']
        output_data[input_file]['text'] = text_of_output

        with open(directory + '/' + input_file, 'w') as output_file:
            json.dump(output_data[input_file], output_file)

