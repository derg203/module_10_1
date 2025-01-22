from threading import Thread
from time import sleep
from datetime import datetime
def write_words(word_count, file_name):
        with open(file_name,'a', encoding='utf-8') as file:
            for i in range(word_count):
                file.write(f'Какое-то слово №  {i+1}\n')
                sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
time_result = time_stop - time_start
print(f'Работа функции составила {time_result} секунд')


time_start2 = datetime.now()
first = Thread(target=write_words, args= (10, 'example5.txt'))
second = Thread(target=write_words, args= (30, 'example6.txt'))
third = Thread(target=write_words, args= (200, 'example7.txt'))
four = Thread(target=write_words, args= (100, 'example8.txt'))
first.start()
second.start()
third.start()
four.start()
first.join()
second.join()
third.join()
four.join()
time_stop2 = datetime.now()
time_result2= time_stop2 - time_start2
print(f'Работа функции составила {time_result2} секунд')
print(f'Использование Потоков быстрее функций на {time_result-time_result2} секунд')
