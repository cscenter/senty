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
        machine_learning.MachineLearning.__init__(self, training_data_path)
        self.gnb = GaussianNB()

    def fit(self):
        train_data, target = machine_learning.MachineLearning.fit_data(self)
        self.gnb.fit(train_data, target)        
    
    def predict(self, json_file_path):
        bash_data = machine_learning.MachineLearning.predict_data(self, json_file_path)
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