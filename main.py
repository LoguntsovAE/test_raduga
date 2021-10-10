from test_1 import list_creater as first_var
from test_2 import list_creater as second_var
import time


if __name__ == '__main__':
    lst_sum = 200
    elem_amount = 8
    min_v = 10
    max_v = 100
    start = time.time()
    print('При параметрах:')
    print('lst_sum =', lst_sum, '; elem_amount =', elem_amount)
    print('min_v =', min_v, '; max_v =', max_v)

    a1 = 0
    a2 = 0
    for _ in range(500):
        first_prg = first_var(lst_sum, elem_amount, min_v, max_v)
        assert sum(first_prg) == lst_sum, f'1-ый вариант: НЕ СХОДИТСЯ, РЕШЕНО НЕ ВЕРНО! {sum(first_prg)} != {lst_sum}'
        assert len(first_prg) == elem_amount, 'Длина списка с ответом = {}, а должна быть {}'.format(len(first_prg), elem_amount)
        print('Ответ 1:', first_prg)
        print('Время выполнения программы 1: {:.2f} сек'.format(time.time() - start))
        a1 += (time.time() - start)

        start = time.time()
        second_prg = second_var(lst_sum, elem_amount, min_v, max_v)
        assert sum(second_prg) == lst_sum, f'2-ый вариант: НЕ СХОДИТСЯ, РЕШЕНО НЕ ВЕРНО! {sum(second_prg)} != {lst_sum}'
        assert len(second_prg) == elem_amount, 'Длина списка с ответом = {}, а должна быть {}'.format(len(second_prg), elem_amount)
        print('Ответ 2:', second_prg)
        print('Время выполнения программы 2: {:.2f} сек'.format(time.time() - start))

        a2 += (time.time() - start)

    print('a1', a1, 'Среднее: {:.3f}'.format(a1 / 50))
    print('a2', a2, 'Среднее: {:.3f}'.format(a2 / 50))