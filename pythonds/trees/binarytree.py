"""
This is binarytree
"""


class BinaryTree:
    """
    This is BinaryTree class
    """

    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None

    def insert_left(self, new_node):
        """
        This is insert_left function
        """
        if self._left_child is None:
            self._left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._left_child = self._left_child
            self._left_child = t

    def insert_right(self, new_node):
        """
        This is insert_left function
        """
        if self._right_child is None:
            self._right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._right_child = self._right_child
            self._right_child = t

    def get_right_child(self):
        """
        This is get_right_child function
        """
        return self._right_child

    def get_left_child(self):
        """
        This is get_left_child function
        """
        return self._left_child

    def set_root_val(self, obj):
        """
        This is set_root_val function
        """
        self._key = obj

    def get_root_val(self):
        """
        This is get_root_val function
        """
        return self._key

    def preorder(self):
        """
        This is preorder function
        """
        print(self._key)
        if self._left_child:
            self._left_child.preorder()
        if self._right_child:
            self._right_child.preorder()

    def postorder(self):
        """
        This is postorder function
        """
        if self._left_child:
            self._left_child.postorder()
        if self._right_child:
            self._right_child.postorder()
        print(self._key)

    def inorder(self):
        """
        This is inorder function
        """
        if self._left_child:
            self._left_child.postorder()
        print(self._key)
        if self._right_child:
            self._right_child.postorder()
