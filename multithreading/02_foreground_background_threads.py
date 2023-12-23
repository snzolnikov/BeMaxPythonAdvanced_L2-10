import threading

from count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main\n')

    ints = read_ints('..\\data\\1Kints.txt')           # последовательно получаем строчки из файла

    t1 = threading.Thread(target=count_three_sum, daemon=True, kwargs=dict(ints=ints)) # daemon=False/True - Foreground/Background
    t1.start() # запуск процесса Foreground/Background
    print(input('What is your name?\n'))

    t1.join() # блокирующий вызов блокирующий основной поток до тех пор пока выполняется t1 поток
    print('ended main')
    #print('Hello ', name)