#include <iostream>
#include <vector>

using namespace std;

struct FenwickTree {
    int n;
    vector<long long> tree;

    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    // Добавление значения delta к элементу с индексом idx
    void add(int idx, long long delta) {
        for (; idx <= n; idx += idx & -idx) {
            tree[idx] += delta;
        }
    }
    long long query(int idx) {
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += tree[idx];
        }
        return sum;
    }

    long long query(int left, int right) {
        if (left > right) swap(left, right);
        return query(right) - query(left - 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    FenwickTree bit(n);

    for (int q = 0; q < k; ++q) {
        int type;
        cin >> type;

        if (type == 1) {
            int i;
            long long x;
            cin >> i >> x;
            bit.add(i, x);
        } else if (type == 2) {
            int u, r;
            cin >> u >> r;
            cout << bit.query(u, r) << "\n";
        }
    }

    return 0;
}