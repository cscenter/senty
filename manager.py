# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import standard_extractor
#import n_gram_extractor
sys.path.append('ml/')
import naive_bayes_gaussian
import svm

testing_data = 'data/testing_data/'
training_data = 'data/training_data/'
extractor_training_data = 'data/extractor_data/training_data/'
extractor_testing_data = 'data/extractor_data/testing_data/'

# return accuracy, TP, TN, FP, FN
def get_quality(ml):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(testing_data))
    testing_files_count = len(os.listdir(testing_data))         
    true_count = 0
    for f in input_files:
        bash = json.load(open(os.path.join(testing_data, f)), 'utf-8')
        real_class = 1
        if bash['positive'] == 'No':
            real_class = -1
        ml_class = ml.predict(testing_data + f)
        if ml_class == real_class:
            true_count += 1
    return float(true_count) / testing_files_count

#NEW_EXTRACTOR = True
NEW_EXTRACTOR = False

def main():
    # обращаемся к экстрактору, он создаёт данные в папках training_data и testing_data
    if NEW_EXTRACTOR:
        # очистить папки training и testing data        
        if os.path.exists(training_data):
            files = filter(lambda x: not x.endswith('~'), os.listdir(training_data))
            for f in files:
                os.remove(training_data + f)
            os.rmdir(training_data)
        os.mkdir(training_data)    
        if os.path.exists(testing_data):    
            files = filter(lambda x: not x.endswith('~'), os.listdir(testing_data))
            for f in files:
                os.remove(testing_data + f)
            os.rmdir(testing_data)        
        os.mkdir(testing_data)
        
        extractor_for_training = standard_extractor.standard_extractor(extractor_training_data, training_data)
       # extractor = n_gram_extractor.n_gramm_extractor(extractor_data, training_data, 2)
        if extractor_for_training.extract() == False:    
            raise Exception('error in extractor for training')
        
        extractor_for_testing = standard_extractor.standard_extractor(extractor_testing_data, testing_data)
        if extractor_for_testing.extract() == False:    
            raise Exception('error in extractor for testing')
        
    # обращаемся к ml, оно работает с данными из training_data
 
    # тестим качество на данных testing_data   
 
    # 1. NBG 
    nbg = naive_bayes_gaussian.NaiveBayesGaussian(training_data)
    nbg.fit()   
    print get_quality(nbg)
    # 2. LinearSVC    
    my_svm = svm.SVM(training_data)
    my_svm.fit()
    print get_quality(my_svm)    
    
if __name__ == '__main__':
    main()