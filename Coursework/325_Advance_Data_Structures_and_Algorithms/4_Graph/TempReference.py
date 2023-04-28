import queue
import sys

class Graph:

    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    class __Vertex:
        def __init__(self, key):
            self.id = key       
            self.connectedTo = {} 

        def getId(self):
            return self.id

        def getConnections(self):
            return self.connectedTo.keys()

        def getWeight(self, nbr):
            return self.connectedTo[nbr] 

        def addNeighbor(self, nbr, weight = 0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return f"connected to: {str([x.id for x in self.connectedTo])}"   

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Graph.__Vertex(key)
        self.verList[key] = newVertex 
        return newVertex

    def getVertex(self, n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, source, destination, weight = 0):
        if source not in self.verList:
            newVertex = self.addVertex(source)
        if destination not in self.verList:
            newVertex = self.addVertex(destination)
        self.verList[source].addNeighbor(self.verList[destination], weight)
    
    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

    def dfs(self, s, visited = None):
        if visited is None:
            visited = set()

        if s not in visited:
            print(s, end = " ")
            visited.add(s)
            for next_node in [x.id for x in self.verList[s].connectedTo]:
                self.dfs(next_node, visited)        

    def bfs(self, s, visited = None):
        if visited is None:
            visited = set()

        q = Queue()
        q.put(s)
        visited.add(s)

        while not q.empty():
            current_node = q.get()
            print(current_node, end = " ")

            for next_node in [x.id for x in self.verList[current_node].connectedTo]:
                if next_node not in visited:
                    q.put(next_node)
                    visited.add(next_node)

    def kruskals(self):
        vertices_sets = set()
        # Create set S(v) = {v} for each vertex v in G
        vertices_sets = [set([v.id]) for v in self.verList.values()]


    # Create a dictionary to hold the edges and their weights
        edges_dict = {}
        for vertex in self.verList.values():
            for nbr in vertex.connectedTo.keys():
                if vertex.id < nbr.id:
                    edges_dict[(vertex.id, nbr.id)] = vertex.connectedTo[nbr]
                else:
                    edges_dict[(nbr.id, vertex.id)] = vertex.connectedTo[nbr]

        # Sort the edges by weight in ascending order
        sorted_edges = sorted(edges_dict.items(), key=lambda x: x[1])

        # Create a set to hold the edges in the minimum spanning tree
        MST = set()

        # For each edge (u, v) in sorted_edges
        for edge in sorted_edges:
            (u, v), weight = edge

            # Find the sets that contain u and v
            set_u = None
            set_v = None
            for vertices_set in vertices_sets:
                for item in vertices_set:
                    if type(item) == set:
                        if u in item or u == item:
                            set_u = vertices_set
                        if v in item or v == item:
                            set_v = vertices_set
                    else:
                        if u == item:
                            set_u = vertices_set
                        if v == item:
                            set_v = vertices_set


            # If S(u) != S(v), merge the sets together and add the edge to the MST
            if set_u != set_v:
                # Add edge (u, v) and weight w to T
                MST.add(((u, v), weight))

                # Merge S(u) and S(v) into one set
                merged_set = set_u.union(set_v)
                # Remove S(u) and S(v) from vertices_sets
                vertices_sets.remove(set_u)
                vertices_sets.remove(set_v)
                # Add the merged set to vertices_sets
                vertices_sets.append(merged_set)

        # Convert the set of edges in the MST to a list and return it
        # Convert the sets in MST to tuples
        MST = set([(tuple(edge[0]), edge[1]) for edge in MST])        
        
        return MST


def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open("test.txt", "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   
    
    print()
    print("Graph Adjacency List: ")
    ### WRITE YOUR CODE HERE ###
    for k, v in graph.verList.items():
        print(k, v) # v is an instance of vertex class, print will use __str__
    
    
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    
    
