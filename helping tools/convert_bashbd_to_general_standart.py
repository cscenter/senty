# -*- coding: utf-8 -*-
    
import json
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)
    
bd = 'snapshot/bd'
bd_processed = 'snapshot/processed/bd'
path_from = 'Marked(without json mark)/'
path_processed = 'Marked(without json mark)/processed/'
path_to = 'Marked(with json mark)/'
    
def main():
    f = open(bd, 'r')
    all_data = f.read().split(' ')
    total_count_lines = len(all_data) / 3
    index_in_all_data = 0
    for num_iter in range(0, total_count_lines):
        id = int(all_data[index_in_all_data])
        text = json2obj(open(path_from + str(id)).read())[0]
        mark = int(all_data[index_in_all_data + 1])
        sarcasm = int(all_data[index_in_all_data + 2])
        if sarcasm == 2:
            sarcasm = 0
        isSarcasm = 'No'
        if sarcasm == 1:
            isSarcasm = 'Yes'
        if mark != 0:    
            positive = 'Yes'
            if (mark < 0):
                positive = 'No'
    
            #создаем новый жисон
            for_json_file = {"id" : id, "text" : text, "positive" : positive, "sarcasm" : isSarcasm}
            json_file = open(path_to + str(id), 'w')
            json.dump(for_json_file, json_file, indent = 2)   
            
        import shutil # файл обработан
        shutil.move(path_from + str(id), path_processed + str(id))
        index_in_all_data += 3

    f.close()
    import datetime
    shutil.move(bd, bd_processed + ' ' + str(datetime.date.today()))

if __name__ == '__main__':
    main()    