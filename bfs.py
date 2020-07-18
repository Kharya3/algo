from collections import deque


def bfs(graph, vertex):
    queue = deque()
    queue.append(vertex)
    explored = {vertex: True}
    level = {vertex: 0}
    while queue:
        temp = queue.popleft()
        for edge in graph[temp]:
            if edge not in explored:
                level[edge] = level[temp]+1
                print(edge)
                explored[edge] = True
                queue.append(edge)


def main():
    graph = {}
    print("Enter the vertices")
    for i in range(n):
        vertex = tuple(map(int, input().split()))
        graph[vertex] = []

    print("Enter the edges")
    for i in range(m):
        v1 = tuple(map(int, input().split()))
        v2 = tuple(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)
    vertex = tuple(map(int, input().split()))
    print(graph)
    bfs(graph, vertex)


if __name__ == '__main__':
    n, m = map(int, input().split())
    INF = 2*n
    main()
