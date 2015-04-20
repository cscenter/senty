# encoding: UTF-8

import machine_learning

from sklearn.naive_bayes import MultinomialNB

class NaiveBayesMultinomial(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)
        self.gnb = MultinomialNB(alpha = 1.0)

    def fit(self):
        train_data, target = machine_learning.MachineLearning.fit_data_1_0(self)
        self.gnb.fit(train_data, target)        
    
    def predict(self, json_file_path):
        bash_data = machine_learning.MachineLearning.predict_data_1_0(self, json_file_path)
        return self.gnb.predict(bash_data)  