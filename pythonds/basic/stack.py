"""
This is stack module
"""


class Stack:
    """
    This is Stack class
    """

    def __init__(self):
        self._items = []

    def is_empty(self):
        """
        This is empty function
        """
        return self._items == []

    def push(self, item):
        """
        This is push function
        """
        self._items.append(item)

    def pop(self):
        """
        This is pop function
        """
        return self._items.pop()

    def peek(self):
        """
        This is peek function
        """
        return self._items[len(self._items) - 1]

    def size(self):
        """
        This is size function
        """
        return len(self._items)
