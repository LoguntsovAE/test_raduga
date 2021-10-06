from test_1 import list_creater as first_var
from test_2 import list_creater as second_var
import time


if __name__ == '__main__':
    lst_sum = 100
    elem_amount = 4
    min_v = 10
    max_v = 50
    start = time.time()
    first_prg = first_var(lst_sum, elem_amount, min_v, max_v)
    second_prg = second_var(lst_sum, elem_amount, min_v, max_v)
    assert sum(first_prg) == lst_sum, f'НЕ СХОДИТСЯ, РЕШЕНО НЕ ВЕРНО! {sum(first_prg)} != {lst_sum}'
    assert sum(second_prg) == lst_sum, f'НЕ СХОДИТСЯ, РЕШЕНО НЕ ВЕРНО! {sum(second_prg)} != {lst_sum}'
    print('При параметрах:')
    print('lst_sum =', lst_sum, '; elem_amount =', elem_amount)
    print('min_v =', min_v, '; max_v =', max_v)
    print('Ответ:', first_prg)
    print('Время выполнения программы 1: {:.2f} сек'.format(time.time() - start))
    print('Ответ:', second_prg)
    start = time.time()
    print('Время выполнения программы 2: {:.2f} сек'.format(time.time() - start))
