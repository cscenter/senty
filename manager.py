# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import extractor1
sys.path.append('ml/')
import naive_bayes_gaussian
import svm

testing_data = 'data/testing_data/'
training_data = 'data/training_data/'
extractor_data = 'data/extractor_data/'

NEW_DATA = False

def main():
    # обращаемся к экстрактору, он создаёт данные в папке training_data
    if NEW_DATA:
        extractor = extractor1.extractor(extractor_data, training_data)
        if extractor.extract() == False:    
            raise Exception('error in extractor')
        
        input_files = filter(lambda x: not x.endswith('~'), os.listdir(training_data))    
        testing_data_ratio = 0.2
        testing_data_count = int(testing_data_ratio * len(input_files))
        # экстрактор должен a процентов testing_data_ratio тестинг, остальные в обучалку
        import shutil
        import random
        for iter_num in range(0, testing_data_count):
            while True:
                num = random.randint(0, len(input_files))
                file_name = training_data + '%s_tf-idf' % num
                if os.path.exists(file_name):
                    shutil.move(file_name, testing_data + '%s_tf-idf' % num)
                    break
    
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