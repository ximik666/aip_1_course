# 2 семестр

__Для получения зачета необходимо выполнить:__
-  необходимо выполнить все практические работы, которые были даны на практике.
> __`Срок сдачи  - за 2 недели до окончания курса`__
-  выполнить и сдать итоговую практическую работу.
> __`Срок сдачи  - за 2 недели до окончания курса`__

### Лекциионный материал:
1. [Лекция 1 -  Поиск элементов в массиве](https://github.com/ximik666/aip_1_course/tree/main/2_semestr/lessons/lesson_1)
2. [Лекция 2 - Алгоритмы сортировки](https://github.com/ximik666/aip_1_course/tree/main/2_semestr/lessons/lesson_2)
3. [Лекция 3 - Стеки и очереди в Python](https://github.com/ximik666/aip_1_course/tree/main/2_semestr/lessons/lesson_3)
3. [Лекция 4 - Основы функционального программирования](https://ru.wikibooks.org/wiki/Python/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_Python)
### Практические работы на занятиях
1. [Практика 1](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/1.ipynb)
2. [Практика 2](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/2.ipynb)
3. [Практика 3](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/3.ipynb)
4. [Практика 4](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/4.ipynb)
5. [Практика 5](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/5.ipynb)
6. [Практика 6](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/6.ipynb)
7. [Практика 6](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/practice/7.ipynb)

### `Итоговая семестровая задача`
#### Требования к семестровой задачи
- > задачу необходимо выполнить до 15 мая
- >решение задач не должно повторяться
- >не использовать внешние библиотеки(numpy и т.д.)
- >перед сдачей работы необходимо проверить программу на все assert ([assert.py](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/semestr_task_2/assert.py) лежит в папке с semestr_tasks_2, инструкция дана ниже)
- >на защите программы необходимо обьяснить работу программы.
- >файл с программой должен называться `semestr_task_2`

Необходимо на языке программирования Python реализовать 8 функции для работы над матрицами
- +`summa[mat1:list, mat2:list]->list` - суммирование 2 матриц и возвращения значения, в случае ошибки возращать `'error'`
- `mul[mat1:list, mat2:list]->list` - умножнение 2 матриц и возвращения значения, в случае ошибки возращать `'error'`
- `diff[mat1:list, mat2:list]->list` - "деление" 2 матриц и возвращения значения, в случае ошибки возращать `'error'`
- +`det[mat1:list]->float` - определитель матрицы и возвращения значения, в случае ошибки возращать `'error'`
- +`transp[mat1:list]->list` - транспонирование матрицы и возвращения значения, в случае ошибки возращать `'error'`
- `rank[mat1:list]->int` - ранг матрицы и возвращения значения, в случае ошибки возращать `'error'`
- `L1[mat1:list]->int` - максимальная сумма модулей элементов в столбце и возвращения значения, в случае ошибки возращать `'error'`
- `L0[mat1:list]->int` - подсчет ненулевых элементов в матрице и возвращения значения, в случае ошибки возращать `'error'`

#### Список assert, которые необходимо проверить находится в файле ([assert.py](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/semestr_task_2/assert.py).
- [x] **для запуска проверки необходимо переименовать файл с вашей программой в semestr_task_2.py**
- [x] **для проверки запускаем файл ([assert.py](https://github.com/ximik666/aip_1_course/blob/main/2_semestr/semestr_task_2/assert.py)**
- [x] **если вы не видите строку 'ошибка проверки', значит программу можно показывать преподавателю. Иначе - программу необходимо переделать.**

Для каждой функции предусмотреть необходимые проверки (деление на 0, совпадение и соответвстие размерностей матрицы и т.д.), в случае несоответствия возращать `'error'`. Следует учесть, что на вход могут подаваться и неверные данные, например, знаки препинания.
