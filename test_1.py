import time
import random


def list_creater(lst_sum, elem_amount, min_v, max_v):

    if max_v * elem_amount < lst_sum or min_v * elem_amount > lst_sum:
        raise ValueError('Такого списка не создать')

    lst = []
    while sum(lst) != lst_sum:
        lst = []
        for _ in range(elem_amount):
            elem = random.randint(min_v, max_v)
            lst.append(elem)
        
    return lst


if __name__ == '__main__':
    lst_sum = 100
    elem_amount = 7
    min_v = 10
    max_v = 50
    start = time.time()
    print(list_creater(lst_sum, elem_amount, min_v, max_v))
    print('Время выполнения программы: {:.2f} сек'.format(time.time() - start))
    print('При параметрах:')
    print('lst_sum =', lst_sum, '; elem_amount =', elem_amount)
    print('min_v =', min_v, '; max_v =', max_v)