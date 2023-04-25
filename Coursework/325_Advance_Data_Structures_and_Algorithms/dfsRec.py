from queue import *

# Breakdown comments
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    class __Vertex:                         # info of edges
        def __init__(self, key):            # 0.6: self = newVertex (not graph), key = 0
            self.id = key                   # 0.7: newVertex.id = 0
            self.connectedTo = {}           # 0.8: newVertex.connectedTo = {}

        def getId(self):
            return self.id
        
        def getConnections(self):
            return self.connectedTo.keys()  # get all the connections that are associated with the vertex
                
        def getWeights(self, nbr):          #self, neighbour
            return self.connectedTo[nbr]    # each vertex has dictionary that tracks what are they connected to and the weights
        
        def addNeighbor(self, nbr, weight = 0): #0.17: self = graph.vertList[0], nbr = graph.vertList[1], w = 5
            self.connectedTo[nbr] = weight      # 0.18: graph.vertList[0].connectedTo[graph.vertList[1]] = 5 or V0.connectedTo[v1] = 5
            # vo.connectedTo[v1] = 5

        def __str__(self):
            return f"connected to {str([x.id for x in self.connectedTo])}"

                                        # 0.1: graph.addVertex(0)
    def addVertex(self, key):           # 0.2: self = graph, key = 0
        self.numVertices += 1           # 0.3: update counter - graph.numVertices = 1
        newVertex = Graph.__Vertex(key) # 0.4: Graph.__Vertex(0) -> goto __Vertex class to create a new vertex
        self.vertList[key] = newVertex  # 0.9: graph.vertList[0] = newVertex - assign the newly created vertex in the graph
        return newVertex                # return the updated graph
    
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    # vertex in graph
    def __contains__(self, key):
        return (key in self.vertList)
    
    # 0.10: graph.addEdge(0, 1, 5)
    def addEdge(self, source, destination, weight = 0): # 0.11 - self = graph, source = 0, destination = 1, weight = 5
        if source not in self.vertList:                 # 0.12 - if 0 not in graph.vertList; we've just added 0 so won't execute
            newVertex = self.addVertex(source) #create a new vertex with source as key
        if destination not in self.vertList:            # 0.13: if 1 in not graph.vertList
            newVertex = self.addVertex(destination)     # 0.14: create a new vertex with source as key if it wasn't available

        self.vertList[source].addNeighbor(self.vertList[destination], weight) # self.vertList[source] it'll return instance of vertex class
        # 0.15: self = graph, graph.vertList.addNeighbor(self.vertList[1], 5)
        # 0.16: just, 0.addNeighbor doesn't work as python doesn't recognize 0 - so we pass key and get value
        
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

    # we're dealing with two dictionaries - one for contents, one for connections

def dfsRecursive(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfsRecursive(visited, graph, node)

def main():
    graph = Graph()
    for i in range(5): # i = 0, 1, 2, 3, 4, 5
        graph.addVertex(i)
    
    print(graph.vertList)
    print()

    graph.addEdge(0, 1) # 0.9_2 (self = graph, soruce = 0, destination = 1, weight = 5)
    graph.addEdge(0, 2) # 0.19
    graph.addEdge(1, 3)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    for vertex in graph:
        for adjacent in vertex.getConnections():
            print(f"({vertex.getId()}, {adjacent.getId()})")    # source and destination: 
    print()

    for k, v in graph.vertList.items():
        print(k, v) # v is an instance of vertex class, print will use __str__
    
main()