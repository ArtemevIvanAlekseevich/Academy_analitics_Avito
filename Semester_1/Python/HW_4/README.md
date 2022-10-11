# Homework 4
Для начала работы с данной директорией предполагается, что рабочей директорией является [HW_4](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4). Во всех тестах присутствует флаг ```-v``` или его аналоги (это про непосредственно в коде ```verbose=True``` у ```doctest ``` и ```verbosity=2``` у ```unittest ```) для предоставления более детального отчета. Все тесты и результаты их выполнения находятся в папках, соответствующих их номеру. Команды для запуска из терминала реализуют запись результата выволнения программы в result.txt.
___

[issue-01](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-01_doctest)
---

Запуск [теста doctest_morse.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-01_doctest/doctest_morse.py) в терминале 
```
cd issue-01_doctest
python -m doctest -o NORMALIZE_WHITESPACE -v doctest_morse.py > result.txt
```
Так же файл можно запустить стандартными средсвами IDE. Все необходимые флаги прописаны в ```doctest.testmod()```
```Python
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
```
[Результат работы теста](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-01_doctest/result.txt)

[issue-02](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-02_parametrize)
---

Запуск [теста test_parametrize_morse.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-02_parametrize/test_parametrize_morse.py) в терминале
```
cd issue-02_parametrize
python -m pytest -v test_parametrize_morse.py > result.txt
```
Так же файл можно запустить стандартными средсвами IDE. Все необходимые флаги прописаны в ```pytest.main()```
```Python
if __name__ == '__main__':
    pytest.main(['issue-02_parametrize/test_parametrize_morse.py', '-v'])
```
[Результат работы теста](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-02_parametrize/result.txt)

[issue-03](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-03_unittest)
---

Запуск [теста test_unittest_one_hot_encoder.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-03_unittest/test_unittest_one_hot_encoder.py) в терминале
```
cd issue-03_unittest
python -m unittest -v test_unittest_one_hot_encoder.py 2> result.txt
```
Так же файл можно запустить стандартными средсвами IDE. Все необходимые флаги прописаны в ```unittest.main()```
```Python
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
[Результат работы теста](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-03_unittest/result.txt)

[issue-04](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-04_pytest)
---

Запуск [теста test_pytest_one_hot_encoder.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-04_pytest/test_pytest_one_hot_encoder.py) в терминале
```
cd issue-04_pytest
python -m pytest -v test_pytest_one_hot_encoder.py > result.txt
```
Так же файл можно запустить стандартными средсвами IDE. Все необходимые флаги прописаны в ```pytest.main()```
```Python
if __name__ == '__main__':
    pytest.main(['issue-04_pytest/test_pytest_one_hot_encoder.py', '-v'])
```
[Результат работы теста](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-04_pytest/result.txt)

[issue-05](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-05)
---

Запуск [теста test_what_is_year_now.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-05/test_what_is_year_now.py) в терминале
```
cd issue-05
python -m pytest -v test_what_is_year_now.py --cov=what_is_year_now > result.txt
```
[Результат работы теста](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-05/result.txt)

Запуск [теста test_what_is_year_now.py](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-05/test_what_is_year_now.py) в терминале с созданием [HTML отчета](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/tree/Flow/Semester_1/Python/HW_4/issue-05/htmlcov) в файле [what_is_year_now_py.html](https://github.com/ArtemevIvanAlekseevich/Academy_analitics_Avito/blob/Flow/Semester_1/Python/HW_4/issue-05/htmlcov/what_is_year_now_py.html).
```
cd issue-05
python -m pytest -v test_what_is_year_now.py --cov=what_is_year_now --cov-report html > result.txt
```

Так же файл можно запустить стандартными средсвами IDE. Все необходимые флаги прописаны в ```pytest.main()```
```Python
if __name__ == '__main__':
    pytest.main(['issue-05/test_what_is_year_now.py',
                 '-v', '--cov=what_is_year_now'])
```

К сожалению не понял почему в терминале тест не выдает 100% покрытие (приложил вывод терминала). Хотя если выводить результат в отдельный файл или в HTML то там 100%.
```
platform win32 -- Python 3.8.5, pytest-7.1.3, pluggy-0.13.1 -- C:\Users\jhnar\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jhnar\OneDrive\Рабочий стол\Programs\Courses\AAA\GIt\Academy_analitics_Avito\Academy_analitics_Avito\Semester_1\Python\HW_4
plugins: cov-4.0.0
collected 4 items

issue-05/test_what_is_year_now.py::test_date_YMD PASSED                                                                                                            [ 25%] 
issue-05/test_what_is_year_now.py::test_date_DMY PASSED                                                                                                            [ 50%] 
issue-05/test_what_is_year_now.py::test_date_invalid PASSED                                                                                                        [ 75%] 
issue-05/test_what_is_year_now.py::test_date_API PASSED                                                                                                            [100%]

----------- coverage: platform win32, python 3.8.5-final-0 -----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
issue-05\what_is_year_now.py      21     10    52%
--------------------------------------------------
TOTAL                             21     10    52%


========================================================================== 4 passed in 33.38s =========================================================================== 
PS C:\Users\jhnar\OneDrive\Рабочий стол\Programs\Courses\AAA\GIt\Academy_analitics_Avito\Academy_analitics_Avito\Semester_1\Python\HW_4>
```

