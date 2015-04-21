# encoding: UTF-8

import machine_learning

from sklearn.linear_model import LogisticRegression

class LG(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)
        self.data_for_fit = machine_learning.MachineLearning.fit_data_1_0(self)
        
        self.lg = LogisticRegression()

    def fit(self):
        self.lg.fit(self.data_for_fit[0], self.data_for_fit[1])        
    
    def predict(self, json_file_path):
        bash_data = machine_learning.MachineLearning.predict_data_1_0(self, json_file_path)
        return self.lg.predict(bash_data)

#DEBUG = True
DEBUG = False

if DEBUG:
    lg = LG("../data/training_data/")        
    lg.fit()
    print lg.predict('../data/testing_data/2225_tf-idf')
