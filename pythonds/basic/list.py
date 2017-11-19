"""
This is list module
"""


class Node:
    """
    This is Node class
    """

    def __init__(self, initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        """
        This is get_data function
        """
        return self._data

    def get_next(self):
        """
        This is get_next function
        """
        return self._next

    def set_data(self, newdata):
        """
        This is set_data function
        """
        self._data = newdata

    def set_next(self, newnext):
        """
        This is set_next function
        """
        self._next = newnext


class UnorderedList:
    """
    This is UnorderedList class
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        This is is_empty function
        """
        return self._head is None

    def add(self, item):
        """
        This is add function
        """
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        """
        This is size function
        """
        current = self._head
        count = 0
        while current is None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        This is search function
        """
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """
        This is remove function
        """
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())


class OrderedList:
    """
    This is OrderedList class
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        This is is_empty function
        """
        return self._head is None

    def add(self, item):
        """
        This is add function
        """
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        """
        This is size function
        """
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        This is search function
        """
        current = self._head
        stop = False
        found = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def remove(self, item):
        """
        This is remove function
        """
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
