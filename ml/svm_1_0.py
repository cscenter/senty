# encoding: UTF-8

import machine_learning

from sklearn.svm import LinearSVC

class SVM(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)

    def predict(self, t):
        self.data_for_fit = machine_learning.MachineLearning.fit_data_1_0(self)
        self.input_files = machine_learning.MachineLearning.getInputFiles(self)
        
        N = len(self.data_for_fit[0])
        n = block_size_in_ratio * float(len(self.data_for_fit[0]))
        n = int(n)
        
        result = []
        totalTrue = 0
        cur_first_index = 0
        while cur_first_index < N:
            print 'Testing set: ' + str(cur_first_index + 1) + ' to ' + str(min(N, cur_first_index + n)) + ' of ' + str(N)
            alone = []
            alone_target = []
            num = 0
            while num < n and num + cur_first_index < N:    
                alone.append(self.data_for_fit[0][0])
                alone_target.append(self.data_for_fit[1][0])
                self.data_for_fit[0].remove(self.data_for_fit[0][0])
                self.data_for_fit[1].remove(self.data_for_fit[1][0])
                num += 1
            
            self.svc = LinearSVC()
            self.svc.fit(self.data_for_fit[0], self.data_for_fit[1])
            
            alone_size = len(alone)
            for iter_num in range(0, alone_size):
                svc_result = self.svc.predict(alone[iter_num])
                if alone_target[iter_num] == svc_result:
                    totalTrue += 1
                result.append((self.input_files[cur_first_index + iter_num], svc_result[0], alone_target[iter_num]))  
            
            
            for iter_num in range(0, alone_size):               
                self.data_for_fit[0].append(alone[iter_num])
                self.data_for_fit[1].append(alone_target[iter_num])
            
            cur_first_index += n
        
        print 'SVC with 1 0: ' + str(round(100. * float(totalTrue) / N, 2)) + '%'
        return result  
      
    def qtCV(self, t):        
        self.data_for_fit = machine_learning.MachineLearning.fit_data_1_0(self)
        from sklearn import cross_validation
        all_scores = 0
        for test in range(0, t):
            print 'test number ' + str(test + 1)
            self.svm = LinearSVC(C = 2)
            import random
            cv = cross_validation.ShuffleSplit(len(self.data_for_fit[0]), n_iter = 10, test_size = 0.1, random_state = random.randint(0, 255))
            print cv
            scores = cross_validation.cross_val_score(self.svm, self.data_for_fit[0], self.data_for_fit[1], cv=cv)            
            
            print 'mean: ' + str(scores.mean())
            all_scores += scores.mean()
            print ''
        print all_scores / float(t)   
      
#DEBUG = True
DEBUG = False

if DEBUG:
    svm_1_0 = SVM("../data/extractor_data/")        
    svm_1_0.predict(5)
