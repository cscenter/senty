# encoding: UTF-8

from abc import ABCMeta, abstractmethod, abstractproperty

class MachineLearning():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def fit():
        pass
        
    @abstractmethod
    def predict():  
        pass    
