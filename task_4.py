def solve():
    n, k = map(int, input().split())
    p = [int(x) - 1 for x in input().split()]
    word = input().strip()
    res = list(word)
    for _ in range(k):
        previous_word = [''] * n
        for i in range(n):
            previous_word[p[i]] = res[i]
        res = previous_word
    print(''.join(res))


solve()