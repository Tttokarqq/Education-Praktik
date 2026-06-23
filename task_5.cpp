#include <iostream>

int main() {
    int h, w;
    if (!(std::cin >> h >> w)) {
        return 0;
    }

    int min_row = h, max_row = -1;
    int min_col = w, max_col = -1;

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            int val;
            std::cin >> val;
            if (val == 1) {
                if (r < min_row) min_row = r;
                if (r > max_row) max_row = r;
                if (c < min_col) min_col = c;
                if (c > max_col) max_col = c;
            }
        }
    }
    int top_left_row = min_row - 1;
    int top_left_col = min_col - 1;
    int bottom_right_row = max_row + 1;
    int bottom_right_col = max_col + 1;

    std::cout << top_left_row << " " << top_left_col << " "
              << bottom_right_row << " " << bottom_right_col << "\n";
    return 0;
}