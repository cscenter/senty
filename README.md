# senty

Фреймворк для определения семантики коротких текстов.

Состоит из экстракторов (папка extractors), модулей машинного обучения(папка ml) и диспетчера, содержащего систему контроля качества

Вспомогательные программы:

BashViewer - программа под андроид для упрощения процедуры получения чистой разметки: https://github.com/andrey9594/bash-viewer

Parser 1.1 - парсер на python для сбора текстов с сайта bash.im

extraсtor1.1.py - базовый экстрактор термов

convert_bashbd_to_general_standart.py - скрипт для конвертирования исходных спарсенных json-ов в размечанные json-ы на основе снимка БД из программы BashViewer

