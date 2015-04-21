# encoding: UTF-8

import machine_learning

from sklearn.naive_bayes import MultinomialNB

class NaiveBayesMultinomial(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)
        self.data_for_fit = machine_learning.MachineLearning.fit_data_count(self)
        
     #   best_alpha = 3.1321 # установлена по сиви, запустить сиви сново при новом обучающем множестве
        #best_alpha = self.get_best_alpha_cv()
        best_alpha = 1.0
        self.gnb = MultinomialNB(alpha = best_alpha)

    def fit(self):
        self.gnb.fit(self.data_for_fit[0], self.data_for_fit[1])        
    
    def predict(self, json_file_path):
        bash_data = machine_learning.MachineLearning.predict_data_count(self, json_file_path)
        return self.gnb.predict(bash_data)
        
    def get_best_alpha_cv(self):
        best_alpha = 1.0
        best_score = 0
        from sklearn import cross_validation
        test_alpha = 0.01
        step = 0.01
        n = 5 # num of parts
        while test_alpha < 10:
            self.gnb = MultinomialNB(test_alpha)
            scores = cross_validation.cross_val_score(self.gnb, self.data_for_fit[0], 
                                                      self.data_for_fit[1], cv = n)
            print str(test_alpha) + ': ' + str(scores.mean())            
            if scores.mean() > best_score:
                best_score = scores.mean()
                best_alpha = test_alpha
            test_alpha += step
        print 'best_alpha: ' + str(best_alpha) + ', with score: ' + str(best_score)    
        return best_alpha

#DEBUG = True
DEBUG = False

if DEBUG:
    nbm = NaiveBayesMultinomial("../data/training_data/")        
    nbm.fit()
