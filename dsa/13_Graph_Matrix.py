class Graph:
    def __init__(self,vertex):
        self.mat = [ [0]*vertex for _ in range(vertex) ]
        self.size = vertex
    
    def add_edge(self,src,dest):
        if(0 <= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest] = 1
            self.mat[dest][dest] = 1
        else:
            print("Invalid Edge")
    
    def print(self):
        for row in self.mat:
            print(' | '.join(map(str,row)))

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(3,4)
g.add_edge(2,3)
g.print()