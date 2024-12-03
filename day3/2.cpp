#include "../common.h"
#include <bits/stdc++.h>
using namespace std;

class Day3_2 {
private:
  vector<pair<int, int>> nums;
  string part = "";
  int total{};
  string re_pattern = R"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))";
  regex re = regex(re_pattern);
  bool enabled = true;
  smatch matches;

public:
  string output{};
  Day3_2() { solve(); }

  void solve() {
    string str;
    string text;
    while (cin >> text) {
      str += text;
    }
    auto search_start = str.cbegin();
    while (std::regex_search(search_start, str.cend(), matches, re)) {
      string instr = matches[0];
      if (instr == "do()") {
        enabled = true;
      } else if (instr == "don't()") {
        enabled = false;
      } else if (enabled) {
        nums.PB({stoi(matches[1]), stoi(matches[2])});
      }
      search_start = matches.suffix().first;
    }
    total = accumulate(nums.begin(), nums.end(), 0, [](int acc, auto p) {
      return acc + p.first * p.second;
    });
  }

  void print_output() {
    output = to_string(total);
    cout << "Output: " << output << endl;
  }

  void debug_print() {
    for (auto c : nums) {
      cout << "a: " << c.first << ", b: " << c.second << endl;
    }
  }
};
