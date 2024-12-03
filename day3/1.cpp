#include "../common.h"
#include <bits/stdc++.h>
#include <regex>
using namespace std;

// Uses a regex based solution
class Day3_1 {
private:
  string re_pattern = R"(mul\((\d{1,3}),(\d{1,3})\))";
  regex re = regex(re_pattern);
  smatch matches;
  vector<pair<int, int>> nums;
  int total{};

public:
  string output{};
  Day3_1() { solve(); }

  void solve() {
    string str;
    string text;
    while (cin >> text) {
      str += text;
    }
    auto search_start = str.cbegin();
    while (std::regex_search(search_start, str.cend(), matches, re)) {
      nums.PB({stoi(matches[1]), stoi(matches[2])});
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
