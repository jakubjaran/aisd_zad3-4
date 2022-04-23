class Element:

    def __init__(self, value, ptr):
        self.value = value
        self.ptr = ptr

    def __str__(self):
        return f'[{self.value}] --> {self.ptr} '


def _next_el(el, x):
    prev = el
    current = el.ptr
    if current.value > x:
        prev.ptr = Element(x, current)
    else:
        if current.ptr == None:
            current.ptr = Element(x, None)
        else:
            _next_el(current, x)


def create_list(array):
    head = None
    for x in array:
        if head == None:
            head = Element(x, None)
            continue
        if head != None:
            if head.value > x:
                temp = head
                head = Element(x, temp)
            else:
                if head.ptr == None:
                    temp = Element(x, None)
                    head.ptr = temp
                else:
                    _next_el(head, x)
    return head


def search_all_elements(list_head):
    temp = list_head
    temp_array = []
    while (temp != None):
        temp_array.append(temp.value)
        temp = temp.ptr
    return temp_array


def remove_list_elements(list_head):
    temp = list_head
    while (temp != None):
        list_head = None
        temp = temp.ptr