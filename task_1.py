heap = []
height = int(input())
for i in range(height):
    heap.append([int(x) for x in input().split()])

path_list = []
len_list = []


def make_paths(index_, now_path):
    if index_ == height:
        path_list.append(now_path)
        return
    make_paths(index_ + 1, now_path + [now_path[-1]])
    make_paths(index_ + 1, now_path + [now_path[-1] + 1])


make_paths(1, [0])
# print(path_list)
for path_ in path_list:
    summ = 0
    for i in range(height):
        summ += heap[i][path_[i]]

