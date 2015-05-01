# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import standard_extractor
import standard_extractor_with_not
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
    #log1 = getFalsesInExtractor(ml, extractor1)
    #log2 = getFalsesInExtractor(ml, extractor2)
    log1 = getMlLogInExtractor(ml, extractor1)
    log2 = getMlLogInExtractor(ml, extractor2)
    diff_log1_log2 = []
    for l in log1:
        ok = False
        res = ""
        for l2 in log2:
            if l[0] == l2[0] and l[1] != l2[1]:
                ok = True
                res = str(l[0]) + '; extr1): ' + str(l[1]) + '; extr2): ' + str(l2[1]) + '; really: ' + str(l[2]) 
                break
        if ok == True:
            diff_log1_log2.append(res)
    return diff_log1_log2        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def main():
#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    extractor2 = standard_extractor_with_not.standard_extractor(marked_data, extractor_data)
#    nbg_count = naive_bayes_gaussian_count.NaiveBayesGaussian(extractor_data)
#    getFalsesInExtractor(nbg_count, extractor1)    
#    diff = getDiffBetweenExtractors(nbg_count, extractor1, extractor2)    

    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
    mnb_count = naive_bayes_multinomial_count.NaiveBayesMultinomial(extractor_data) 
    extractor2 = standard_extractor_with_not.standard_extractor(marked_data, extractor_data)    
    diff = getDiffBetweenExtractors(mnb_count, extractor1, extractor2)    
    
#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    extractor2 = standard_extractor_with_not.standard_extractor(marked_data, extractor_data)
#    my_svm_1_0 = svm_1_0.SVM(extractor_data)
  #  diff = getDiffBetweenExtractors(my_svm_1_0, extractor1, extractor2)    
    f = open('diff.txt', 'w')
    for d in diff:
        f.write(d + '\n')
    f.close()
    print 'Diffrence has been writen into diff.txt'
#    extractor1 = standard_extractor.standard_extractor(marked_data, extractor_data)
#    my_svm_tf_idf = svm_tf_idf.SVM(extractor_data)
#    getFalsesInExtractor(my_svm_tf_idf, extractor1)    
    
    '''
    # 5. Logistic Regression 1 0
    lg_with_1_0 = logistic_regression_1_0.LG(marked_data)
    lg_with_1_0.fit()
    print 'Logistic Regression with 1 0'
    get_quality(lg_with_1_0)    
    '''
    
if __name__ == '__main__':
    main()