"""
#Graphs

An item in a graph is called a VERTEX (you may hear it referred to as NODE);
Plural is Vertices;
Between 2 connected vertices we have and EDGE; A vertex can have as many edges as we like, connecting it to other vertices;

##Concepts:
Edges can be:
Weighted - shows the cost going through a specific edge;
Bidirectional; VIsualized without pointer arrows, connection flows both ways;
One directional: the connection flows only one way, we have an arrow showing it usually;

## Trees are a form of a GRAPH, with the limitation that each node can only point to 2 other nodes (binary search tree)
## Linked List is a form of a GRAPH, with the limitation that each node can point to one other node

#Representing Graphs
## Adjecancy Matrix: 1's for edges a vertex connects to, and 0 for those it doesn't connect to; Image example:
The diagonal of such a matrix is always 0's; If the matrix is biderectional, we will always have a symmetrix matrix;
If the edges are weighted, we just stare these weights in the matrix instead of having 1s;
## Adjecancy List: We use a dictionary, the vertex is the key, and all the vertices it points to are in a list as the value of that key; 
# Example:
{
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    ...
}
In this course we will use an adjecancy list;

# Graph Big O:

## Adjecancy Matrix: 
    Space Complexity: O(|V|*2) # Each vertex has to store all verteces it is not connected to as 0s very inefficient;
    
    Adding a vertex: O(|V|*2) (basically rewriting the whole matrix)
    Remove a vertex: O (|V|*2)
    Adding an edge: O(1)
    Removing an edge: O(1)

## Adjecancy List:
    Space Complexity: O(|V| + |E|) - vertices + edges

    Adding a vertex: O(1)
    Remove a vertex: O (|V| + |E|)
    Adding an edge: O(1)
    Removing an edge: O(|E|) - E = number of edges
"""


class Graph:  # bidrectional edges
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        # specific efficiency for biderectional graphs -> if vertex has an edge to anoter vertex, that one will be have a pointer back to it;
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
my_graph.remove_vertex(1)
my_graph.print_graph()
