# encoding: UTF-8

import machine_learning

from sklearn.svm import LinearSVC

class SVM(machine_learning.MachineLearning):        
    def __init__(self, training_data_path):
        machine_learning.MachineLearning.__init__(self, training_data_path)
    
    def predict(self, block_size_in_ratio):
        self.data_for_fit = machine_learning.MachineLearning.fit_data_tf_idf(self)
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
        
        print 'SVC with tf idf: ' + str(round(100. * float(totalTrue) / N, 2)) + '%'
        return result  

