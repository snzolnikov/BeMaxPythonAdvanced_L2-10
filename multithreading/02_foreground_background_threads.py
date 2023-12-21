import threading

from multithreading.count_three_sum import read_ins, count_three_sum

if __name__ == '__main__':
    print('started main\n')

    ints = read_ins('..\\data\\1Kints.txt')           # последовательно получаем строчки из файла
    t1 = threading.Thread(target=count_three_sum, args=(ints, ), daemon=True) # daemon=False/True - Foreground/Background
    t1.start() # запуск процесса Foreground/Background
    print(input('What is your name?\n'))

    t1.join() # блокирующий вызов
    print('ended main')
    print('Hello ', name)