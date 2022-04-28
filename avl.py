class AVL_Element:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL_Tree:

    def create_avl(self, array):
        root = None
        for x in array:
            root = self.insert(root, x)
        return root

    def insert(self, root, key):
        if not root:
            return AVL_Element(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        bal = self.get_bal(root)

        if bal > 1 and key < root.left.value:
            return self.rotate_right(root)

        if bal < -1 and key > root.right.value:
            return self.rotate_left(root)

        if bal > 1 and key > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if bal < -1 and key < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left()

        return root

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_heigth(z.left), self.get_height(z.right))

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_bal(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(f'{root.value}')
        self.pre_order(root.left)
        self.pre_order(root.right)