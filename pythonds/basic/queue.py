"""
This is queue module
"""


class Queue:
    """
    This is Queue class
    """

    def __init__(self):
        self._items = []

    def is_empty(self):
        """
        This is is_empty function
        """
        return self._items == []

    def enqueue(self, item):
        """
        This is enqueue function
        """
        self._items.insert(0, item)

    def dequeue(self):
        """
        This is dequeue function
        """
        return self._items.pop()

    def size(self):
        """
        This is size function
        """
        return len(self._items)
