from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list);

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visit = [False]*(len(self.graph))

        queue = []

        #add root to queue
        queue.append(s)
        visit[s]=True

        while queue:
            #deque
            s=queue.pop(0)
            print s

            for i in self.graph[s]:
                if not visit[i]:
                    queue.append(i)
                    visit[i]=True

    # A function used by DFS
    def DFSUtil(self,v,visited):

        # Mark the current node as visited and print it
        visited[v]= True
        print v

        print visited
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):

        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))

        # Call the recursive helper function to print
        # DFS traversal
        for i in range(0,len(self.graph)):
            if not visited[i]:
                self.DFSUtil(i,visited)

def test_BD():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(3, 2)

    print "Following is Breadth First Traversal (starting from vertex 2)"
    g.BFS(2)
    print "Following is DFS from (starting from vertex 2)"
    g.DFS()

test_BD()
