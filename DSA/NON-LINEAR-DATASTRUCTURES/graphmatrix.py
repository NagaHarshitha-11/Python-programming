class ADJ_GRAPH:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for j in range(len(self.vertices))] for i in range(len(self.vertices))]
        
        # print(self.adj_matrix)
        
    def display(self):
        print("  ",end="")
        for i in range(len(self.adj_matrix)):
            print(self.vertices[i],end=" ")
        print()
        for k,v in enumerate(self.adj_matrix):
            print(self.vertices[k],end=" ")
            for i in v:
                print(i,end=" ")
            print()
            
            
    def addEdges(self,vertex1,vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # print(f"idx of {vertex1} ",self.adj_matrix.index(vertex1))
            # print(f"idx of {vertex2} ",self.adj_matrix.index(vertex2))
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.adj_matrix[idx1][idx2] = 1
            self.adj_matrix[idx2][idx1] = 1
            return True
        return False
    
    def removeEdges(self,vertex1,vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            idx1 = self.vertices.index(vertex1)
            idx2 = self.vertices.index(vertex2)
            self.adj_matrix[idx1][idx2] = 0
            self.adj_matrix[idx2][idx1] = 0
            return True
        return False
    
    def display_adj_vertex(self,vertex):
        if vertex in self.vertices:
            idx = self.vertices.index(vertex)               # res = self.adj_matrix[self.vertices.index(vertex)]
            for i in range(len(self.adj_matrix[idx])):      # for i in range(len(res)):
                if self.adj_matrix[idx][i] == 1:                # if res[i] == 1:
                    print(self.vertices[i],end=" ")                 # print(self.vertices[i],end=" ")
        else:
            print("Vertex doesn't exsist")
            
    

    # def find_path(self,end_vertex):
    #     path = []
    #     if end_vertex in self.vertices:
    #         i = 0
    #         j = 0
    #         while i < len(self.vertices):
    #             while j < len(self.vertices):
    #                 if self.adj_matrix[i][j] == 1:
    #                     path.append(self.adj_matrix[i][j])
    #                     j += 1
    #                 else:
    #                     i += 1
    #         return path
    #     return None
    

total = int(input("Enter the total vertix to add: "))
vertices = []
for i in range(total):
    val = input("Enter the vertex: ")
    vertices.append(val)
gh = ADJ_GRAPH(vertices)
gh.display()
print()
gh.addEdges('A','D')
gh.addEdges('A','B')
gh.addEdges('A','C')
gh.addEdges('B','E')
gh.addEdges('C','D')
gh.addEdges('D','E')
gh.addEdges('E','E')

gh.display()
print()
# gh.removeEdges('A','D')
# gh.display()
# print()
gh.display_adj_vertex('A')
print()
# print(gh.find_path('E'))