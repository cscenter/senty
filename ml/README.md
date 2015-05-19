# ml

Все модули МО (кроме _machine_learning.py_) имеют методы fit и predict

Модули: 

* __logistic_regression_count.py__ - логическая регрессия подсчетом

*  __machine_learning.py__ - класс, в котором реализованы методы fit_data и predict_data(их вариации для tf/idf, count и 1-0), составляющие вектора из документов. Остальные модули МО наследуются от этого класса и используют эти методы для обучения и классификации.

* __naive_bayes_gaussian_count.py__ - гауссианский Байес подсчетом термов

* __naive_bayes_multinomial_count.py__ - мультиномиальный Байес подсчетом термов

* __svm_1_0.py__ - LinearSVC, принимает вектора из 1 и 0

* __svm_td_idf.py__ - LinearSVC, принимает вектора из tf и idf
