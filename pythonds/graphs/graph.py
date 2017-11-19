"""
This script is graph module
"""


class Vertex:
    """
    This is vertex class
    """

    def __init__(self, key):
        """
        this is init
        """
        self._id = key
        self._connected_to = {}
        self._color = 'white'

    def add_neighbor(self, nbr, weight=0):
        """
        This is neighbor function
        """
        self._connected_to[nbr] = weight

    def __str__(self):
        return (str(self._id) + ' connectedTo: '
                + str([x.id for x in self._connected_to]))

    def get_connections(self):
        """
        This is get connection function
        """
        return self._connected_to.keys()

    def get_id(self):
        """
        This is get id function
        """
        return self._id

    def get_weight(self, nbr):
        """
        This is get weight function
        """
        return self._connected_to[nbr]


class Graph:
    """
    This is Graph class
    """

    def __init__(self):
        """
        This is init
        """
        self._vert_list = {}
        self._num_vertices = 0

    def add_vertex(self, key):
        """
        This is add vertex function
        """
        self._num_vertices = self._num_vertices + 1
        new_vertex = Vertex(key)
        self._vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        """
        This is get vertex function
        """
        if n in self._vert_list:
            return self._vert_list[n]
        else:
            return None

    def __contains__(self, n):
        """
        This is contains function
        """
        return n in self._vert_list

    def add_edge(self, f, t, cost=0):
        """
        This is add edge function
        """
        if f not in self._vert_list:
            nv = self.add_vertex(f)
        if t not in self._vert_list:
            nv = self.add_vertex(t)
        self._vert_list[f].add_neighbor(self._vert_list[t], cost)

    def get_vertices(self):
        """
        This is get vertices fucntion
        """
        return self._vert_list.keys()

    def __iter__(self):
        """
        This is iter function
        """
        return iter(self._vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print(w)
