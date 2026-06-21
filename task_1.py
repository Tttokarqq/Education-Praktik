heap = []
height = int(input())
for i in range(height):
    heap.append([int(x) for x in input().split()])


# 1) решение через перебор всех путей
path_list = []
len_list = []


def make_paths(index_, now_path):
    if index_ == height:
        path_list.append(now_path)
        return
    make_paths(index_ + 1, now_path + [now_path[-1]])
    make_paths(index_ + 1, now_path + [now_path[-1] + 1])


make_paths(1, [0])
for path_ in path_list:
    summ = 0
    for i in range(height):
        summ += heap[i][path_[i]]
    len_list.append(summ)
minn = min(len_list)
print(minn)
print(*[heap[i][path_list[len_list.index(minn)][i]] for i in range(height)])


# 2) решение через проход от нижних вершин к верхним с прибавлением минимального
for i in range(height - 2, -1, -1):
    for j in range(len(heap[i])):
        min_vertex = min(heap[i + 1][j], heap[i + 1][j + 1])
        # print(min_vertex, heap[i][j], min_vertex + heap[i][j])
        heap[i][j] += min_vertex
    # print("!!!!!")
print(heap[0][0])
print(heap)
ind = 0
vertex_ = heap[0][0]
for i in range(1, height):
    if heap[i][ind] < heap[i][ind + 1]:
        print(vertex_ - heap[i][ind], end=" ")
        vertex_ = heap[i][ind]
    else:
        print(vertex_ - heap[i][ind + 1], end=" ")
        ind += 1
        vertex_ = heap[i][ind]
print(vertex_)
