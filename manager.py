# encoding: UTF-8

import sys
sys.path.append('extractors/')
import extractor1
sys.path.append('ml/')
import naive_bayes_gaussian

testing_data = 'data/testing_data/'
training_data = 'data/training_data/'
extractor_data = 'data/extractor_data/'

def main():
    # обращаемся к экстрактору, он создаёт данные в папке training_data
#    extractor = extractor1.extractor(extractor_data, training_data)
#    if extractor.extract() == False:    
#        raise Exception('error in extractor')
    # экстрактор должен N процентов в тестинг, 100 - N в обучалку
    
    # обращаемся к ml, оно работает с данными из training_data
    nbg = NaiveBayesGaussian(training_data)
    nbg.fit()    
    
    # тестим качество на данных testing_data
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(testing_data))
    ok = 0
    for f in input_files:
        bash = json.load(open(os.path.join(testing_data, f)), 'utf-8')
        real_class = 1
        if bash['positive'] == 'No':
            real_class = -1
        y = nbg.predict(testing_data + f)
        if y == real_class:
            ok += 1
    print float(ok) / len(os.listdir(testing_data))         

if __name__ == '__main__':
    main()