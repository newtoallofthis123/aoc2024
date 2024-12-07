// #include "../common.h"
#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

class Day6_1 {
private:
    vector<vector<char>> grid;
    pair<int, int> curr;
    char curr_dir = '^';
    map<char, pair<int, int>> directions {
        { '^', { -1, 0 } }, { 'v', { 1, 0 } }, { '<', { 0, -1 } }, { '>', { 0, 1 } }
    };
    map<char, char> turns = { { '^', '>' }, { '>', 'v' }, { 'v', '<' }, { '<', '^' } };
    unordered_set<char> visited;

    void find_position()
    {
        for (size_t i = 0; i < grid.size(); i++) {
            for (size_t j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == '^' || grid[i][j] == 'v' || grid[i][j] == '<' || grid[i][j] == '>') {
                    curr = { i, j };
                    curr_dir = grid[i][j];
                    return;
                }
            }
        }
    }

public:
    string output {};
    int total {};
    Day6_1() { solve(); }

    void solve()
    {
        string line;
        while (getline(cin, line)) {
            grid.push_back(vector<char>(line.begin(), line.end()));
        }

        find_position();
        int i = curr.first;
        int j = curr.second;

        while (true) {
            auto dir = directions[curr_dir];

            auto dx = i + dir.first;
            auto dy = j + dir.second;

            if (dx < 0 || dx >= (int)grid.size() || dy < 0 || dy >= (int)grid[0].size()) {
                break;
            }

            if (grid[dx][dy] == '#') {
                curr_dir = turns[curr_dir];
            } else {
                i = dx;
                j = dy;
                visited.insert(grid[i][j]);
            }
        }
    }

    void print_output() { cout << "Output: " << output << endl; }

    void debug_print()
    {
        for (auto row : grid) {
            for (auto cell : row) {
                cout << cell;
            }
            cout << endl;
        }

        cout << "Current position: " << curr.first << " " << curr.second << endl;
        cout << "Total" << visited.size() << endl;
    }
};
