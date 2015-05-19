# senty

Фреймворк для определения семантики коротких текстов.

Состоит из экстрактора и фич (папка extractors), модулей машинного обучения(папка ml) и диспетчера, содержащего систему контроля качества, а также вспомогательных модулей (папка helping tools). Папка data не является частью репозитория, она содержит обучающее множество и множество для тестирования(папки extractor_data - данные для экстрактора, training_data - для МО, testing_data - для диспетчера); у каждого разработчика своё содержимое в этой папке.

Вспомогательные программы:

* __BashViewer__ - программа под андроид для упрощения процедуры получения чистой разметки: [BashViewer](https://github.com/andrey9594/bash-viewer)

* __GUI__ - программы с графическим интерфейсом (см readme в папке)

* __extractors/*__ - экстрактор и скрипт, содержащий различные фичи (смотри readme в папке)

* __helping tools/*__ - вспомогательные скрипты (смотри readme в папке)

* __ml/*__ - модули МО (смотри readme в папке)

* __old/extractors/__ - папка, содержащая предыдущие (теперь неиспользуемые) версии экстракторов

* __presentations/__ - презентации относящиеся к проекту (tex и pdf)

* __manager.py__ - диспетчер

