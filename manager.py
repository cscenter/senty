# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import standard_extractor
#import n_gram_extractor
#import more_than_n_gram_extractor
sys.path.append('ml/')
import naive_bayes_gaussian_count
import naive_bayes_multinomial_count
import svm_1_0
import svm_tf_idf
import logistic_regression_1_0

marked_data = 'data/marked_data/'
extractor_data = 'data/extractor_data/'

def getMlResults(ml):
    return ml.predict(0.05)
    
def getMlLogInExtractor(ml, extractor):    
    if os.path.exists(extractor_data):
        files = filter(lambda x: not x.endswith('~'), os.listdir(extractor_data))
        for f in files:
            os.remove(extractor_data + f)
        os.rmdir(extractor_data)
    os.mkdir(extractor_data)    
    print 'Starting extracting...'
    if extractor.extract() == False:     
        raise Exception('error in extractor')    
    print 'Extracting ok'    
    log = getMlResults(ml)
    return log
    
def getFalsesInExtractor(ml, extractor):
    log = getMlLogInExtractor(ml, extractor)
    log_with_falses = []
    for l in log:
        if l[1] != l[2]:
            log_with_falses.append(l)
    return log_with_falses

def getDiffBetweenExtractors(ml, extractor1, extractor2):
    pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def main():
#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    nbg_count = naive_bayes_gaussian_count.NaiveBayesGaussian(extractor_data)
#    getFalsesInExtractor(nbg_count, extractor1)    

#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    mnb_count = naive_bayes_multinomial_count.NaiveBayesMultinomial(extractor_data)
#    getFalsesInExtractor(mnb_count, extractor1)    
    
    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
    my_svm_1_0 = svm_1_0.SVM(extractor_data)
    getFalsesInExtractor(my_svm_1_0, extractor1)    

#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    my_svm_tf_idf = svm_tf_idf.SVM(extractor_data)
#    getFalsesInExtractor(my_svm_tf_idf, extractor1)    
    
    '''
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