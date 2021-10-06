import time
import random

def randomizer(min, max):
    return random.randint(min, max)

def list_creater(lst_sum, elem_amount, min_v, max_v):

    lst = []

    if max_v * elem_amount < lst_sum or min_v * elem_amount > lst_sum:
        raise ValueError('Такого списка не создать')

    lst.append(randomizer(min_v, max_v))
    i = 1
    while True:
        lst.append(randomizer(min_v, max_v))
        if elem_amount - i == 1:
            if lst_sum == sum(lst):
                break
            else:
                del lst[-1]
                continue
        if (elem_amount-i) * min_v > lst_sum - sum(lst):
            del lst[-1]
            continue
        i += 1
        if i == elem_amount:
            break

    return lst


if __name__ == '__main__':
    lst_sum = 100
    elem_amount = 4
    min_v = 10
    max_v = 50
    start = time.time()
    answer = list_creater(lst_sum, elem_amount, min_v, max_v)
    print(answer)
    print('Время выполнения программы: {:.2f} сек'.format(time.time() - start))
    print('При параметрах:')
    print('lst_sum =', lst_sum, '; elem_amount =', elem_amount)
    print('min_v =', min_v, '; max_v =', max_v)
    assert sum(answer) == lst_sum, f'НЕ СХОДИТСЯ, РЕШЕНО НЕ ВЕРНО! {sum(answer)} != {lst_sum}'