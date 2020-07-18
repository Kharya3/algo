from collections import deque


def bfs(graph):
    num = 0
    explored = {}
    cc = {}
    for ver in graph.keys():
        if ver not in explored:
            num += 1
            queue = deque(ver)
            while queue:
                temp = queue.popleft()
                cc[temp] = num
                for edge in graph[temp]:
                    if edge not in explored:
                        num += 1
                        print(edge)
                        explored[edge] = True
                        queue.append(edge)


def main():
    n, m = map(int, input().split())
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
    print(graph)
    bfs(graph)


if __name__ == '__main__':
    main()
