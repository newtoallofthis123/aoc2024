#include "../common.h"
#include <bits/stdc++.h>
using namespace std;

class Day4_1 {
private:
  vector<vector<char>> graph;
  int count = 0;

public:
  string output{};
  Day4_1() { solve(); }

  void solve() {
    string line;
    while (getline(cin, line)) {
      stringstream ss(line);
      vector<char> nums;
      char num;
      while (ss >> num) {
        nums.PB(num);
      }
      graph.PB(nums);
    }

    // word XMAS can appear horizontally, vertically, or diagonally, written
    // backwards or forwards
    int rows = graph.size();
    int cols = graph[0].size();
    vector<pair<int, int>> directions = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        for (auto c : directions) {
          if (0 <= (i + c.first * 3) && (i + c.first * 3) < rows &&
              0 <= (j + c.second * 3) && (j + c.second * 3) < cols) {
            string word = "";
            for (int k = 0; k < 4; k++) {
              word += graph[i + c.first * k][j + c.second * k];
            }
            if (word == "XMAS") {
              count++;
            } else if (word == "SAMX") {
              count++;
            }
          }
        }
      }
    }
  }

  void print_output() {
    output = to_string(count);
    cout << "Output: " << output << endl;
  }

  void debug_print() {
    for (auto c : graph) {
      for (auto g : c) {
        cout << g << " ";
      }
      cout << "\n";
    }
  }
};