'''Основные алгоритмы, применимые к графам:

Обход графа - это алгоритм, который позволяет перебрать все вершины графа. Существует несколько способов обхода графа, например, поиск в глубину и поиск в ширину.

Кратчайший путь - это алгоритм, который находит кратчайший путь между двумя вершинами в графе. Один из самых известных алгоритмов кратчайшего пути - это алгоритм Дейкстры.

Поиск минимального остовного дерева - это алгоритм, который находит минимальное поддерево графа, содержащее все вершины графа. Один из самых известных алгоритмов поиска минимального остовного дерева - это алгоритм Прима.

Поиск максимального потока - это алгоритм, который находит максимальный поток между двумя вершинами графа. Один из самых известных алгоритмов поиска максимального потока - это алгоритм Форда-Фалкерсона.

Топологическая сортировка - это алгоритм, который находит линейный порядок вершин в ориентированном ациклическом графе. Топологическая сортировка может быть использована для решения задач нахождения кратчайших путей в DAG (Directed Acyclic Graph), а также для определения порядка выполнения задач в процессах и схемах.

Кластеризация - это алгоритм, который разбивает граф на подграфы (кластеры), где вершины внутри кластера тесно связаны между собой, а между кластерами связи более редкие. Кластеризация может использоваться для анализа социальных сетей, выявления сообществ в Интернете и в других областях.
'''

# Прежде всего необходимо определиться со способом представления графов в памяти компьютера

# Отдельные списки вершин и рёбер

_nodes = [1, 2, 3, 4, 5]
_edges = [(1, 2), (1, 3), (3, 4), (4, 5)]


# список списков смежности

_adj_list = [[], [2, 3], [1], [1, 4], [3, 5], [4]]

# Матрица смежности


_adj_matrix = [[0 for _ in range(len(_nodes))] for _ in range(len(_nodes))]
_adj_matrix[0][:3] = 1, 1, 1
_adj_matrix[1][:2]= 1, 1
_adj_matrix[2][0], _adj_matrix[2][2], _adj_matrix[2][3] = 1, 1, 1
_adj_matrix[3][2], _adj_matrix[3][3], _adj_matrix[3][4] = 1, 1, 1
_adj_matrix[4][3:] = 1, 1

def _adj_matrix_print(matrix):
    print(*range(len(matrix) + 1), sep = '\t')
    for i in range(1, len(matrix) + 1):
        print(i, *matrix[i-1], sep = '\t')

_adj_matrix_print(_adj_matrix)


# дальше приведём алгоритмы применимо к списку списков смежности

# Поиск в глубину

def DFS(adj_list: list, start: int, visited = []):
    visited.append(start)
    for vertice in adj_list[start]:
        if not (vertice in visited):
            DFS(adj_list, vertice, visited)
    return visited


""" adj_list_1 = [[], [2, 3], [1], [1, 4], [3, 5], [4], [2]]
print(DFS(adj_list_1, 1)) """

# поиск в ширину
from collections import deque
def BFS(adj_list: list, start: int):
    visited = []
    q = deque([start])
    while q:
        cur = q.pop()
        visited.append(cur)
        for vertice in adj_list[cur]:
            if not (vertice in visited):
                q.appendleft(vertice)
    return visited

adj_list_1 = [[], [2, 3], [1], [1, 4], [3, 5], [4], [2]]
print(BFS(adj_list_1, 1))

# Алгоритм Дейкстры
from heapq import heapify, heappop, heappush

def Dijkstra(adj_list:list, start: int):
    distances = [float('inf')] * len(adj_list)
    distances[start] = 0
    visited = [False] * len(adj_list)
    
    q = [[0, start]]
    while q:
        cur = heappop(q)
        visited[cur[1]] = True
        for vertice, weight in adj_list[cur[1]]:
            if not visited[vertice]:
                heappush(q, [weight, vertice])
                distances[vertice] = min(distances[vertice], distances[cur[1]] + weight)
    return distances

""" adj_list_1 = [[], [[2, 10], [3, 15]], [[1, 12]], [[1, 12], [4, 5]], [[3, 7], [5, 11]], [[4, 3]], [[2, 10]]]
print(Dijkstra(adj_list_1, 1)) """



