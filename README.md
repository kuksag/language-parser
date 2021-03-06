# Типовой проект для языка M на парсер-комбинаторах

Благодаря статье [tomassetti.me/parsing-in-python](https://tomassetti.me/parsing-in-python/) появилась возможность выбора между
библиотеками. По итогу выбор стоял между [Parsec.py](https://github.com/sighingnow/parsec.py) и [Parsy](https://github.com/python-parsy/parsy) 
из-за их схожести с либой на haskell -- [parsec](https://hackage.haskell.org/package/parsec). Использован Parsy из-за более дружелюбной документации.

## Сборка и запуск

### Загрузка
```shell
git clone git@github.com:kuksag/language-parser.git
cd language-parser
pip3 install -r requirements.txt
```

### Запуск интерактора
```shell
python3 main.py
```

### Запуск тестов
```shell
pytest tests/
python3 main.py --input tests/data.in --output tests/data.out
```

## Описание программ

Программой на языке M является возможно пустая последовательность определений отношений и одна цель. 
После каждого определения отношения, а также после каждой "внешней" цепи должна быть точка с запятой `;`.
Индентация не является значащей.

Результатом парсера для файла является список синтаксических деревьев строк (а точнее логических конструкций, разделенных точкой с запятой). <br>
Результатом интерактора является синтаксическое дерево для каждой строки.

## Описание синтаксиса языка

### Идентификатор, переменная
```regexp
ID, VAR = \w(\w|\d)*
```
Строка из символов латинского алфавита и цифр.

### Атом 
```regexp
ATOM = VAR | CONS_APP 
```
Переменная или конструктор, примененный к списку атомов.

### Применение конструктора
```regexp
CONS_APP = ID {ATOM_LIST}
```
Конструкция, которая начинается с идентификатора и заканчивается списком атомов, отделенным в фигурные скобки.


### Список атомов 
```regexp
ATOM_LIST = Ø | VAR | VAR, ATOM_LIST
```
Конструкция, которая содержит ненулевое количество атомов, разделенных запятой.


### Отношение
```regexp
REL = ID (ATOM_LIST) {AIM}
```
Отношение содержит идентификатор; список атомов, заключенных в круглые скобки; цель, которая 
заключена в фигурные скобки. 

### Цель 
```regexp
AIM = [TERM -> TERM] \ [AIM && AIM] \ [AIM || AIM] \ REL_CALL 
```
- Унификация двух термов.
- Конъюнкция двух целей.
- Дизъюнкция двух целей.
- Вызов отношения.

### Вызов отношения
```regexp
REL_CALL = ID (ATOM_LIST)
```
Идентификатор, затем список атомов в круглых скобках. 
