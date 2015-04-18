# encoding: UTF-8

import machine_learning

from sklearn.svm import LinearSVC

class SVM(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)
        self.svm = LinearSVC()

    def fit(self):
        train_data, target = machine_learning.MachineLearning.fit_data(self)
        self.svm.fit(train_data, target)        
    
    def predict(self, json_file_path):
        bash_data = machine_learning.MachineLearning.predict_data(self, json_file_path)
        return self.svm.predict(bash_data) 
