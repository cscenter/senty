# encoding: UTF-8

extractor_data = '../data/extractor_data/'
training_data = extractor_data + 'training_data/'
testing_data = extractor_data + 'testing_data/'

import os
import shutil
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", help="Ratio", required = True, type = float)
args = parser.parse_args()
ratio = args.r

def main():
    input_files = filter(lambda x: not x.endswith('~'), os.listdir(extractor_data))
    
    files_count = len(input_files)
    testing_data_count = int(files_count * ratio)
    
    if os.path.exists(testing_data) == False:
        os.mkdir(testing_data)
    
    file_index_allready_in_testing_data = set()
    for iter_num in range(0, testing_data_count):
        while True:
            file_num = random.randint(0, files_count)
            if file_num not in file_index_allready_in_testing_data:
                shutil.move(extractor_data + input_files[file_num], testing_data + input_files[file_num])
                file_index_allready_in_testing_data.add(file_num)
                break

    if os.path.exists(training_data) == False:
        os.mkdir(training_data)
            
    for file_num in range(0, files_count):
        if file_num not in file_index_allready_in_testing_data:
            shutil.move(extractor_data + input_files[file_num], training_data + input_files[file_num])
            file_index_allready_in_testing_data.add(file_num)
    
if __name__ == '__main__':
    main()    