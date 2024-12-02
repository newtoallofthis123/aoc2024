#include "../common.h"
#include <bits/stdc++.h>
using namespace std;

class Day1_1 {
private:
  priority_queue<int, vector<int>, greater<int>> pq1;
  priority_queue<int, vector<int>, greater<int>> pq2;
  VI distances;
  int total{};

public:
  string output{};
  Day1_1() { solve(); }

  void solve() {
    string line;
    while (getline(cin, line)) {
      stringstream ss(line);
      int num;
      ss >> num;
      pq1.push(num);
      ss >> num;
      pq2.push(num);
    }

    while (!pq1.empty() && !pq2.empty()) {
      auto n1 = pq1.top();
      auto n2 = pq2.top();
      pq1.pop();
      pq2.pop();
      distances.PB(abs(n2 - n1));
      total += abs(n2 - n1);
    }
  }

  void print_output() {
    output = to_string(total);
    cout << "Output: " << output << endl;
  }

  void debug_print() {
    for (auto d : distances) {
      cout << d << endl;
    }
  }
};
