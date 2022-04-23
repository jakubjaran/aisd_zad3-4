import random
import time
import sys

from list import create_list, remove_list_elements, search_all_elements


def main():
    sys.setrecursionlimit(999999)

    array = random.sample(range(1, 1000000), 10000)

    print('Creating List')
    start = time.time()
    list_head = create_list(array)
    end = time.time()
    print(end - start)

    print('Searching List Elements')
    start = time.time()
    search_all_elements(list_head)
    end = time.time()
    print(end - start)

    print('Removing List Elements')
    start = time.time()
    remove_list_elements(list_head)
    end = time.time()
    print(end - start)


main()