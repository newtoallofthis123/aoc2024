#include "../common.h"
#include <bits/stdc++.h>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Day2_1 {
private:
  vector<string> safe{};
  VI diffs{};

  bool isSafe(stringstream *ss) {
    int num{};
    int prev{};

    *ss >> prev;

    while (*ss >> num) {
      auto diff = num - prev;
      prev = num;
      diffs.PB(diff);
    }

    for (auto d : diffs) {
      if (d == 0) {
        return false;
      }
      if (abs(d) > 3 || abs(d) < 1) {
        return false;
      }
    }

    auto isInc = true;
    auto isDec = true;

    for (auto d : diffs) {
      if (d > 0) {
        isDec = false;
      }
    }

    for (auto d : diffs) {
      if (d < 0) {
        isInc = false;
      }
    }

    return isInc || isDec;
  }

public:
  string output{};
  Day2_1() { solve(); }

  void solve() {
    string line;
    while (getline(cin, line)) {
      stringstream ss(line);
      if (isSafe(&ss)) {
        safe.PB(line);
      }
      diffs.clear();
    }
  }

  void print_output() {
    output = to_string(safe.size());
    cout << "Output: " << output << endl;
  }

  void debug_print() {
    for (auto c : safe) {
      cout << c << "\n";
    }
  }
};
