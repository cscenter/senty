# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import standard_extractor
#import n_gram_extractor
import more_than_n_gram_extractor
sys.path.append('ml/')
import naive_bayes_gaussian_count
import naive_bayes_multinomial_count
import svm_1_0
import svm_tf_idf
import logistic_regression_1_0

marked_data = 'data/marked_data/'
extractor_data = 'data/extractor_data/'

'''
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
'''    

def getMlResults(ml):
    return ml.predict(0.05)
    
def getMlLogInExtractor(ml, extractor):    
    if os.path.exists(extractor_data):
        files = filter(lambda x: not x.endswith('~'), os.listdir(extractor_data))
        for f in files:
            os.remove(extractor_data + f)
        os.rmdir(extractor_data)
    os.mkdir(extractor_data)    
    if extractor.extract() == False:     
        raise Exception('error in extractor')    
    log = getMlResults(ml)
    return log
    
def getFalsesInExtractor(ml, extractor):
    log = getMlLogInExtractor(ml, extractor)
    log_with_falses = []
    for l in log:
        if l[1] != l[2]:
            log_with_falses.append(l)
    print len(log_with_falses)        
    return log_with_falses

def getDiffBetweenExtractors(ml, extractor1, extractor2):
    pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def main():
    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
  #  nbg_count = naive_bayes_gaussian_count.NaiveBayesGaussian(marked_data)
    mnb_count = naive_bayes_multinomial_count.NaiveBayesMultinomial(extractor_data)
    getFalsesInExtractor(mnb_count, extractor1)    
    '''
    # 1. NBG count
    nbg_count = naive_bayes_gaussian_count.NaiveBayesGaussian(marked_data)
    nbg_count.fit()   
    print 'Naive Bayes Gaussian with count'
    get_quality(nbg_count)

    # 2. MBG count
    mbg_count = naive_bayes_multinomial_count.NaiveBayesMultinomial(marked_data)
    mbg_count.fit()   
    print 'Naive Bayes Multinomial with count'
    get_quality(mbg_count)

    # 3. LinearSVC 1 0    
    my_svm_1_0 = svm_1_0.SVM(marked_data)
    my_svm_1_0.fit()
    print 'SVC with 1 0'
    get_quality(my_svm_1_0)        
    
    # 4. LinearSVC tf idf    
    my_svm_tf_idf = svm_tf_idf.SVM(marked_data)
    my_svm_tf_idf.fit()
    print 'SVC with tf idf'
    get_quality(my_svm_tf_idf)    
    
    # 5. Logistic Regression 1 0
    lg_with_1_0 = logistic_regression_1_0.LG(marked_data)
    lg_with_1_0.fit()
    print 'Logistic Regression with 1 0'
    get_quality(lg_with_1_0)    
    '''
    
if __name__ == '__main__':
    main()