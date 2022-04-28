import time


class BST_Element:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value} L<{self.left}>L R<{self.right}>R'


class BST_Tree:

    def insert(self, root, value):
        if root == None:
            return BST_Element(value)

        if root.value < value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)

        return root

    def create_bst(self, array):
        root = None
        for x in array:
            root = self.insert(root, x)
        return root

    def inorder(self, root, array):
        if root:
            self.inorder(root.left, array)
            array.append(root.value)
            self.inorder(root.right, array)

    def find_all_elements(self, root):
        array = []
        self.inorder(root, array)
        return array

    def delete_all_elements(self, root):
        if (root != None):
            self.delete_all_elements(root.left)
            self.delete_all_elements(root.right)
            root = None

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return max(self.get_height(root.left), self.get_height(
                root.right)) + 1


def test_bst(A):
    array = A[:]
    print('Creating BST')
    start = time.time()
    bst = BST_Tree()
    root = bst.create_bst(array)
    end = time.time()
    creation_time = end - start

    print('Searching BST Elements')
    start = time.time()
    bst.find_all_elements(root)
    end = time.time()
    searching_time = end - start

    print('Removing BST Elements')
    start = time.time()
    bst.delete_all_elements(root)
    end = time.time()
    removing_time = end - start

    return creation_time, searching_time, removing_time
