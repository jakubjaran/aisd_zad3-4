import random
import sys
import pandas

from avl import AVL_Tree
from bst import BST_Tree
from avg import avg


def main():
    sys.setrecursionlimit(10**6)

    print('Array length: ')
    a_length = int(input())
    print('Step: ')
    step = int(input())
    print('Tests: ')
    tests = int(input())

    writer = pandas.ExcelWriter(f'out/zad4_{a_length}__{step}_{tests}.xlsx',
                                engine='openpyxl')

    N = []
    BST_H = []
    AVL_H = []

    for i in range(0, 15):
        print(f'Array length: {a_length}')

        N.append(a_length)

        TEMP_BST_H = []
        TEMP_AVL_H = []

        for j in range(0, tests):
            print(f'Test {j+1}')
            array = random.sample(range(1, a_length * 10), a_length)

            bst = BST_Tree()
            bst_root = bst.create_bst(array)
            TEMP_BST_H.append(bst.get_height(bst_root))

            sorted_array = bst.find_all_elements(bst_root)

            avl = AVL_Tree()
            avl_root = avl.create_avl(sorted_array)
            TEMP_AVL_H.append(avl.get_height(avl_root))

        BST_H.append(int(avg(TEMP_BST_H)))
        AVL_H.append(int(avg(TEMP_AVL_H)))
        a_length += step

    data = pandas.DataFrame({
        'N': N,
        'Wysokość BST': BST_H,
        'Wysokość AVL': AVL_H
    })

    data.to_excel(writer, sheet_name='BST vs AVL', index=False)
    writer.save()


main()