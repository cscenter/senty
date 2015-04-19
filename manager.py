# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import standard_extractor
#import n_gram_extractor
sys.path.append('ml/')
import naive_bayes_gaussian_1_0
import naive_bayes_gaussian_tf_idf
import naive_bayes_multinomial_1_0
import naive_bayes_multinomial_tf_idf
import svm_1_0
import svm_tf_idf

testing_data = 'data/testing_data/'
training_data = 'data/training_data/'
extractor_training_data = 'data/extractor_data/training_data/'
extractor_testing_data = 'data/extractor_data/testing_data/'

# print accuracy, TP, TN, FP, FN
def get_quality(ml):
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(testing_data))
    testing_files_count = len(os.listdir(testing_data))         
    true_count = 0
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for f in input_files:
        bash = json.load(open(os.path.join(testing_data, f)), 'utf-8')
        real_class = 1
        if bash['positive'] == 'No':
            real_class = -1
        ml_class = ml.predict(testing_data + f)
        if ml_class == real_class:
            true_count += 1
            if bash['positive'] == 'Yes':
                TP += 1
            else:
                TN += 1;
        else:
            if bash['positive'] == 'Yes':
                FN += 1
            else:
                FP += 1
    print 'Accuracy: ' + str(float(true_count) / testing_files_count)
    print 'All test count: ' + str(testing_files_count) + '; TP: ' + str(TP) + '; TN: ' + str(TN) + '; FP: ' + str(FP) + '; FN: ' + str(FN)  
    print ''    
    
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
 
    # 1. NBG 1 0
    nbg_1_0 = naive_bayes_gaussian_1_0.NaiveBayesGaussian(training_data)
    nbg_1_0.fit()   
    print 'Naive Bayes Gaussian with 1 0'
    get_quality(nbg_1_0)

    # 2. NBG tf idf
    nbg_tf_idf = naive_bayes_gaussian_tf_idf.NaiveBayesGaussian(training_data)
    nbg_tf_idf.fit()   
    print 'Naive Bayes Gaussian with tf idf'
    get_quality(nbg_tf_idf)

    # 3. MBG 1 0
    mbg_1_0 = naive_bayes_multinomial_1_0.NaiveBayesMultinomial(training_data)
    mbg_1_0.fit()   
    print 'Naive Bayes Multinomial with 1 0'
    get_quality(mbg_1_0)

    # 4. MBG tf idf
    mbg_tf_idf = naive_bayes_multinomial_tf_idf.NaiveBayesMultinomial(training_data)
    mbg_tf_idf.fit()   
    print 'Naive Bayes Multinomial with tf idf'
    get_quality(mbg_tf_idf)

    # 5. LinearSVC 1 0    
    my_svm_1_0 = svm_1_0.SVM(training_data)
    my_svm_1_0.fit()
    print 'SVC with 1 0'
    get_quality(my_svm_1_0)        
    
    # 6. LinearSVC tf idf    
    my_svm_tf_idf = svm_tf_idf.SVM(training_data)
    my_svm_tf_idf.fit()
    print 'SVC with tf idf'
    get_quality(my_svm_tf_idf)    
    
if __name__ == '__main__':
    main()