# ml

Все модули МО (кроме _machine_learning.py_) имеют методы fit и predict

Модули: 

*  __machine_learning.py__ - класс, в котором реализованы методы fit_data и predict_data, составляющие вектора из документов. Остальные модули МО наследуются от этого класса и используют эти методы для обучения и классификации.

* __naive_bayes_gaussian_count.py__ - Гауссианский Байес подсчетом термов

* __naive_bayes_multinomial_count.py__ - Мультиномиальный Байес подсчетом термов

* __logistic_regression_1_0.py__ - Логическая регрессия, принимает вектора из 1 и 0

* __svm_1_0.py__ - LinearSVC, принимает вектора из 1 и 0

* __svm_td_idf.py__ - LinearSVC, принимает вектора из tf и idf
