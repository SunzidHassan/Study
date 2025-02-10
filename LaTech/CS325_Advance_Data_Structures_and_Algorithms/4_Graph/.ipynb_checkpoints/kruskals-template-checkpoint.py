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

    # used idea from: <https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/>
    # used idea from: <https://www.pythonpool.com/kruskals-algorithm-python/>
    # used idea from: <https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/minimum-spanning-trees-kruskals-algorithm/>
    
    def kruskals(self):
        vertices_sets = set()
        edgesDict = dict()
        MST = set()
        
        ### WRITE YOUR CODE HERE ###
        # Create set for each vertex
        verticesSets = [set([v.id]) for v in self.verList.values()]

        # Create a dictionary to hold edges and weights
        for vertex in self.verList.values():
            for nbr in vertex.connectedTo.keys():
                edgesDict[(vertex.id, nbr.id)] = vertex.connectedTo[nbr]
                
        # Sort the edges by weight
        sortedEdges = sorted(edgesDict.items(), key=lambda item: item[1])

        for edge in sortedEdges:
            (u, v), weight = edge
            setU = None
            setV = None
            for verticesSet in verticesSets:
                for item in verticesSet:
                    if u == item:
                        setU = verticesSet
                    if v == item:
                        setV = verticesSet

            # If S(u) != S(v), merge sets together and add edge to MST
            if setU != setV:
                MST.add(((u, v), weight))
                mergedSet = setU.union(setV)
                verticesSets.remove(setU)
                verticesSets.remove(setV)
                verticesSets.append(mergedSet)
        return MST

def main():
    
    # create an empty graph
    graph = Graph()

    # get graph vertices & edges from input file and add them to the graph
    file = open(sys.argv[1], "r")
    for line in file:
        values = line.split()
        graph.addEdge(int(values[0]), int(values[1]), int(values[2]))
        graph.addEdge(int(values[1]), int(values[0]), int(values[2]))   

    # print adjacency list representation of the graph
    print()
    ### WRITE YOUR CODE HERE ###
    for k, v in graph.verList.items():
        print(k, v)
    
    # create graph MST
    MST = graph.kruskals()
    # print graph MST
    print()    
    print("Graph MST:")
    print("Edge\t\tWeight")
    for edge in MST:
        print(f"{edge[0]}\t\t{edge[1]}")

main() 
    
    
