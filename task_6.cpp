#include <iostream>

long long min_val(long long v1, long long v2) {
    return (v1 < v2) ? v1 : v2;
}

int main() {
    int n;
    if (!(std::cin >> n)) return 0; //
    for (int i = 0; i < n; ++i) { //
        long long a, b, x, y;
        std::cin >> a >> b >> x >> y; //

        long long max_pairs = min_val(a + b, min_val(x + y, a + x)); //

        std::cout << max_pairs << (i == n - 1 ? "" : " "); //[cite: 1]
    }

    std::cout << "\n";
    return 0;
}