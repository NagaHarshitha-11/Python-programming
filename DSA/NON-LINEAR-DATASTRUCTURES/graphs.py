class GRAPH:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        return False

    def display(self):
        if len(self.graph) != 0:
            for k,v in self.graph.items():
                print(k," : ",v)
        else:
            print("No Vertex")
            
    def addEdges(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdges(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)
            return True
        return False
    
    def remove_vertex(self,vertex):
        if vertex in self.graph:
            for i in self.graph[vertex]:
                self.graph[i].remove(vertex)
            # self.graph.pop(vertex)  
            del self.graph[vertex]
            return True
        return False

    def bfs_traversing(self,vertex):
        if vertex in self.graph:
            visited = [vertex]
            queue = [vertex]
            while queue:
                delvertex = queue.pop(0)
                print(delvertex,end=" ")
                for i in self.graph[delvertex]:
                    if i not in visited:
                        visited.append(i)
                        queue.append(i)          
        else:
            print("Given vertex is doesn't exsist in graph")
            
    def dfs_traversing(self,vertex):
        if vertex in self.graph:
            visited = [vertex]
            stack = [vertex]
            while stack:
                delvertex = stack.pop()
                print(delvertex,end=" ")
                for i in self.graph[delvertex]:
                    if i not in visited:
                        visited.append(i)
                        stack.append(i)
        else:
            print("Given vertex is doesn't exsist in graph")
            
        

gh = GRAPH()
gh.add_vertex('A')
gh.add_vertex('B')
gh.add_vertex('C')
gh.add_vertex('D')
gh.add_vertex('E')
gh.display()
print()
gh.addEdges('A','B')
gh.addEdges('A','C')
gh.addEdges('A','D')
gh.addEdges('C','D')
gh.addEdges('B','E')
gh.addEdges('D','E')
gh.display()
print()
# gh.removeEdges('A','C')
# gh.display()
# print()
# gh.remove_vertex('A')
# gh.display()
# print()
print("Breadth First Search Traversing")
gh.bfs_traversing('A')

print()
print("Depth First Search Traversing")
gh.dfs_traversing('A')