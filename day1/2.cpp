#include "../common.h"
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Day1_2 {
private:
  unordered_map<int, int> freqs;
  VI nums;
  VI distances;
  int total{};

public:
  string output{};
  Day1_2() { solve(); }

  void solve() {
    string line;
    while (getline(cin, line)) {
      stringstream ss(line);
      int num;
      ss >> num;
      nums.PB(num);
      ss >> num;
      freqs[num]++;
    }
    for (auto c : nums) {
      distances.PB(freqs[c] * c);
      total += freqs[c] * c;
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
