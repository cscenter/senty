# extractors

Экстракторы:

* __standard_extractor.py__ - создаёт tf-idf для униграмм

* __n_gram_extractor.py__ - создает tf-idf для n-грамм (только n-граммы)

* __more_than_n_gram_extractor.py__ - создает tf-idf для n-грамм (1, 2, ..., n - граммы)

* __standard_extractor_with_not.py__ - создаёт tf-idf для униграмм и для биграмм вида не+(слово) 

* __extractor_with_counting_number_of_rows.py__ -учитывает количество строк, если их больше пяти
