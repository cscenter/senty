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

NEW_EXTRACTOR = True
#NEW_EXTRACTOR = False

def main():
    # обращаемся к экстрактору, он создаёт данные в папке training_data
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
    
    nbg = naive_bayes_gaussian.NaiveBayesGaussian(training_data)
    nbg.fit()
    my_svm = svm.SVM(training_data)
    my_svm.fit()    
    
    # тестим качество на данных testing_data
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(testing_data))
    testing_files_count = len(os.listdir(testing_data))         
    nbg_true = 0
    svm_true = 0
    for f in input_files:
        bash = json.load(open(os.path.join(testing_data, f)), 'utf-8')
        real_class = 1
        if bash['positive'] == 'No':
            real_class = -1
        nbg_class = nbg.predict(testing_data + f)
        svm_class = my_svm.predict(testing_data + f)
        if nbg_class == real_class:
            nbg_true += 1
        if svm_class == real_class:
            svm_true += 1
    print float(nbg_true) / testing_files_count
    print float(svm_true) / testing_files_count

if __name__ == '__main__':
    main()