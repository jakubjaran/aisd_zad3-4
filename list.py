import time


class List_Element:

    def __init__(self, value, ptr):
        self.value = value
        self.ptr = ptr

    def __str__(self):
        return f'[{self.value}] --> {self.ptr} '


class List:

    def next_el(self, el, x):
        prev = el
        current = el.ptr
        if current.value > x:
            prev.ptr = List_Element(x, current)
        else:
            if current.ptr == None:
                current.ptr = List_Element(x, None)
            else:
                self.next_el(current, x)

    def create_list(self, array):
        head = None
        for x in array:
            if head == None:
                head = List_Element(x, None)
                continue
            if head != None:
                if head.value > x:
                    temp = head
                    head = List_Element(x, temp)
                else:
                    if head.ptr == None:
                        temp = List_Element(x, None)
                        head.ptr = temp
                    else:
                        self.next_el(head, x)
        return head

    def find_all_list_elements(self, list_head):
        temp = list_head
        array = []
        while (temp != None):
            array.append(temp.value)
            temp = temp.ptr
        return array

    def remove_list_elements(self, list_head):
        temp = list_head
        while (temp != None):
            list_head = None
            temp = temp.ptr


def test_list(A):
    array = A[:]
    print('Creating List')
    start = time.time()
    list = List()
    list_head = list.create_list(array)
    end = time.time()
    creation_time = end - start

    print('Searching List Elements')
    start = time.time()
    list.find_all_list_elements(list_head)
    end = time.time()
    searching_time = end - start

    print('Removing List Elements')
    start = time.time()
    list.remove_list_elements(list_head)
    end = time.time()
    removing_time = end - start

    return creation_time, searching_time, removing_time