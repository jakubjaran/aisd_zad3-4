import random
import sys
import pandas

from list import test_list
from bst import test_bst
from avg import avg


def main():
    sys.setrecursionlimit(10**6)

    print('Array length: ')
    a_length = int(input())
    print('Step: ')
    step = int(input())
    print('Tests: ')
    tests = int(input())

    writer = pandas.ExcelWriter(f'out/zad3_{a_length}__{step}_{tests}.xlsx',
                                engine='openpyxl')

    N = []

    LIST_C = []
    LIST_S = []
    LIST_R = []

    BST_C = []
    BST_S = []
    BST_R = []

    for i in range(0, 15):
        print(f'Array length: {a_length}')
        N.append(a_length)

        TEMP_LIST_C = []
        TEMP_LIST_S = []
        TEMP_LIST_R = []
        TEMP_BST_C = []
        TEMP_BST_S = []
        TEMP_BST_R = []

        for j in range(0, tests):
            print(f'Test {j + 1}')
            array = random.sample(range(1, a_length * 10), a_length)
            list_c, list_s, list_r = test_list(array)
            TEMP_LIST_C.append(list_c)
            TEMP_LIST_S.append(list_s)
            TEMP_LIST_R.append(list_r)
            bst_c, bst_s, bst_r = test_bst(array)
            TEMP_BST_C.append(bst_c)
            TEMP_BST_S.append(bst_s)
            TEMP_BST_R.append(bst_r)

        LIST_C.append(avg(TEMP_LIST_C))
        LIST_S.append(avg(TEMP_LIST_S))
        LIST_R.append(avg(TEMP_LIST_R))

        BST_C.append(avg(TEMP_BST_C))
        BST_S.append(avg(TEMP_BST_S))
        BST_R.append(avg(TEMP_BST_R))

        a_length += step

    data = pandas.DataFrame({
        'N': N,
        'List Creation': LIST_C,
        'BST Creation': BST_C,
    })
    data.to_excel(writer, sheet_name='Creation', index=False)

    data = pandas.DataFrame({
        'N': N,
        'List Searching': LIST_S,
        'BST Searching': BST_S,
    })
    data.to_excel(writer, sheet_name='Searching', index=False)

    data = pandas.DataFrame({
        'N': N,
        'List Removing': LIST_R,
        'BST Removing': BST_R
    })
    data.to_excel(writer, sheet_name='Removing', index=False)
    writer.save()


main()