# extractors

Экстракторы:

* __standard_extractor_with_mystem.py__ - создаёт tf-idf для униграмм

* __n_gram_extractor_with_mystem.py__ - создает tf-idf для n-грамм (только n-граммы)

* __more_than_n_gram_extractor_with_mystem.py__ - создает tf-idf для n-грамм (1, 2, ..., n - граммы)

* __standard_extractor_with_mystem_with_not.py__ - создаёт tf-idf для униграмм и для биграмм вида не+(слово) 

* __standard_extractor_with_counting_number_of_rows_with_mystem.py__ - экстрактор производный от стандартного с майстемом, учитывает количество строк, если их больше пяти

* __standard_extractor_without_mystem.py__ - создаёт tf-idf для униграмм, только без mystem-а
