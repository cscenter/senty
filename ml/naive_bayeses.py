# encoding: UTF-8

import argparse

def naive_bayes_gausian():
    print 'Gaussian'

def another_bayes_method():
    print 'Another'

# другие Байесы со скит леарна, парсить аргументы командной строки

parser = argparse.ArgumentParser()
parser.add_argument("-m", help = "ML method number:0-Gaussian,1-Another", required = True, type = int)
args = parser.parse_args()

def main(method):
    if method == 0:
        naive_bayes_gausian()
    elif method == 1:
        another_bayes_method()
    else:
        raise Exception('Bad choice, unknown Bayes ml method!')
        
if __name__ == '__main__':
    main(args.m)        
        
