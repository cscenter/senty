# encoding: UTF-8

import os
import json
import machine_learning

from collections import namedtuple

from sklearn.naive_bayes import GaussianNB

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

class NaiveBayesGaussian(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        self.gnb = GaussianNB()
        self.term_num = {}
        self.terms_count = 0
        self.training_data_path = training_data_path
        
    def fit(self):
        input_files = filter(lambda x: not x.endswith('~'), os.listdir(self.training_data_path))
        all_words = set()
        for f in input_files:
            bash = json.load(open(os.path.join(self.training_data_path, f)), 'utf-8')
            for word in bash['terms']:
                all_words.add(word)
        
        iter = 0
        self.terms_count = len(all_words)
        for word in all_words:
            self.term_num[word] = iter
            iter += 1
        
        train_data = []
        target = []
        for f in input_files:
            bash = json.load(open(os.path.join(self.training_data_path, f)), 'utf-8')
            senty = 1
            if bash['positive'] == 'No':
                senty = -1
            target.append(senty)    
            bash_data = []
            for iter in range(0, self.terms_count):
                bash_data.append(0)
            bash_dict = dict(bash['terms'])
            for word in bash['terms']:
                tf = bash_dict[word][u'tf']
                idf = bash_dict[word][u'idf']
                bash_data[self.term_num[word]] = tf * idf
            train_data.append(bash_data)    
        self.gnb.fit(train_data, target)        
        #сначала получить список всех различных файлов в сет
        #во втором пробеге уже составлять вектора    
    
    def predict(self, json_file_path):
        bash = json.load(open(json_file_path), 'utf-8')
        bash_data = []
        for iter in range(0, self.terms_count):
            bash_data.append(0)
        bash_dict = dict(bash['terms'])
        for word in bash['terms']:
            if word not in self.term_num:
                continue
            tf = bash_dict[word][u'tf']
            idf = bash_dict[word][u'idf']
            bash_data[self.term_num[word]] = tf * idf
        return self.gnb.predict(bash_data)  


def main():
 #   DEBUG_training_data = '../data/training_data/' 
 #   DEBUG_test_file = '../data/testing_data/23_tf-idf'
 #   nb = NaiveBayesGaussian(DEBUG_training_data)
 #   nb.fit()
  #  y = nb.predict(DEBUG_test_file)
    #if y == -1:
    #    y = 'No'
    #else:
    #    y = 'Yes'
  #  print y    
    pass

if __name__ == '__main__':
    main()