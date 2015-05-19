# encoding: UTF-8

import os
import json

import sys
sys.path.append('extractors/')
import features
import extractor
sys.path.append('ml/')
import naive_bayes_gaussian_count
import naive_bayes_multinomial_count
import svm_1_0
import svm_tf_idf
import logistic_regression_count

marked_data = 'data/marked_data/'
middle_data = 'data/middle_data/'
extractor_data = 'data/extractor_data/'

def getAccuracyAndTF(ml):
    log = getMlLogInExtractor(ml)
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    correct = 0
    for l in log:
        ml_result = l[1]
        real_result = l[2]
        if ml_result == real_result:
            correct += 1
            if ml_result == 1:
                TP += 1
            else:
                TN += 1
        else:
            if ml_result == 1:
                FP += 1
            else:
                FN += 1
    return [correct, len(log), float(correct) / len(log), TP, TN, FP, FN]            

def getMlResults(ml, block_size_in_ratio):
    return ml.predict(block_size_in_ratio)
    
def getMlLogInExtractor(ml):    
    block_size_in_ratio = 0.1
    log = getMlResults(ml, block_size_in_ratio)
    return log
    
def getFalsesInExtractor(ml, extractor):
    log = getMlLogInExtractor(ml, extractor)
    log_with_falses = []
    for l in log:
        if l[1] != l[2]:
            log_with_falses.append(l)
    return log_with_falses
     
def delete_folder_with_files(folder):
    if os.path.exists(folder) == True:
        files_in_folder = os.listdir(folder)
        for f in files_in_folder:
            os.remove(folder + f)
        os.rmdir(folder)     

def executeMlAndPrintAccurancy(ml):
    res = getAccuracyAndTF(ml)
    print res
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
def main():
    print 'Подготовка материалов...'
    delete_folder_with_files(middle_data)
    os.mkdir(middle_data)    
    delete_folder_with_files(extractor_data)
    os.mkdir(extractor_data)     

    # до насадки разбираемся с смайликами
    print 'Ищем и преобразовываем смайлики...' 
    features.emoticon_detection(marked_data, middle_data)
    
    # обязательная насадка без удаления повторяющихся букв - прогонка через mystem + убираем знаки препинания
    #print 'Прогоняем через mystem и убираем знаки препинания...'
    #features.mystem_using(marked_data, middle_data)        
    
    # обязательная насадка с удалением повторяющихся букв - прогонка через mystem + убираем знаки препинания    
    print 'Прогоняем через mystem (удаляем подряд идущие повторяющиеся буквы) и убираем знаки препинания...'
    features.mystem_using_with_considering_of_multiple_letters(middle_data, middle_data)

    # убирает повторяющиеся буквы, фича, не насадка
    print 'Удаляем подряд идущие повторяющиеся буквы...'  
    features.considering_of_multiple_letters(middle_data)    
        
    # удаление предлогов
    #print 'Убираем предлоги...'
    #features.without_prepositions(middle_data)    
    
    # удаление союзов
    #print 'Убираем союзы...'
    #features.without_conjunctions(middle_data)    
    
    # удаление местоимений
    #print 'Убираем местоимения...'
    #features.without_pronouns(middle_data)         
    
    # частица не
    print 'Присоединяем частицу не к словам не состояниям...'
    features.with_not(middle_data)    
    
    # убираем термы на английском языке
    print 'Убираем термы на английском языке...'
    features.without_foreign_words(middle_data)    
    
    # 1, 2, ..., n-граммы
    #print '1, 2, 3, .. n граммы...'
    #features.more_than_n_gram_feature(2, middle_data)
    
    # n-граммы
    #print 'n граммы...'
    #features.n_gram_feature(3, middle_data) 
    
    print 'Экстрактор работает...'    
    my_extractor = extractor.extractor(middle_data, extractor_data)
    if my_extractor.extract() == False:
        raise Exception('Error in extractor!')

    print 'Запускаем машинное обучение...' 
    executeMlAndPrintAccurancy(naive_bayes_gaussian_count.NaiveBayesGaussian(extractor_data))
    executeMlAndPrintAccurancy(naive_bayes_multinomial_count.NaiveBayesMultinomial(extractor_data))
    #executeMlAndPrintAccurancy(svm_1_0.SVM(extractor_data))
    #executeMlAndPrintAccurancy(svm_tf_idf.SVM(extractor_data))
    #executeMlAndPrintAccurancy(logistic_regression_count.LG(extractor_data))
    
    #delete_folder_with_files(middle_data)    
    
if __name__ == '__main__':
    main()