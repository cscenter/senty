# encoding: UTF-8

import sys
sys.path.append('extractors/')
import extractor1

training_data = 'data/training_data'
extractor_data = 'data/extractor_data'

def main():
    # обращаемся к экстрактору, он создаёт данные в папке training_data
    extractor = extractor1.extractor(extractor_data, training_data)
    if extractor.extract() == False:    
        raise Exception('error in extractor')
    
    # обращаемся к ml, оно работает с данными из training_data
        
    
    # тестим качество на данных testing_data

if __name__ == '__main__':
    main()