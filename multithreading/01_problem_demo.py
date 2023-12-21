from multithreading.count_three_sum import read_ins, count_three_sum

if __name__ == '__main__':
    print('started main')

    ints = read_ins('..\\data\\1Kints.txt')
    count_three_sum(ints)

    print('What are we waiting for?')
    print('ended main')
