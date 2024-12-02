#include <bits/stdc++.h>
using namespace std;

class Day2_2 {
private:
  vector<string> safe;

  bool isDiffSafe(const vector<int> &diffs) {
    if (diffs.empty())
      return false;

    for (int d : diffs) {
      if (d == 0 || abs(d) < 1 || abs(d) > 3)
        return false;
    }

    bool isInc =
        all_of(diffs.begin(), diffs.end(), [](int d) { return d > 0; });
    bool isDec =
        all_of(diffs.begin(), diffs.end(), [](int d) { return d < 0; });

    return isInc || isDec;
  }

  bool isSafe(const vector<int> &nums) {
    if (unordered_set<int>(nums.begin(), nums.end()).size() != nums.size()) {
      return false;
    }

    vector<int> diffs;
    for (size_t i = 1; i < nums.size(); ++i) {
      diffs.push_back(nums[i] - nums[i - 1]);
    }

    return isDiffSafe(diffs);
  }

  bool canBeSafe(const vector<int> &nums) {
    if (isSafe(nums))
      return true;

    for (size_t i = 0; i < nums.size(); ++i) {
      vector<int> temp(nums.begin(), nums.end());
      temp.erase(temp.begin() + i);
      if (isSafe(temp))
        return true;
    }

    return false;
  }

public:
  string output;

  Day2_2() { solve(); }

  void solve() {
    string line;
    while (getline(cin, line)) {
      stringstream ss(line);
      vector<int> numbers;
      int num;

      while (ss >> num) {
        numbers.push_back(num);
      }

      if (canBeSafe(numbers)) {
        safe.push_back(line);
      }
    }
  }

  void print_output() {
    output = to_string(safe.size());
    cout << "Output: " << output << endl;
  }

  void debug_print() {
    for (const auto &line : safe) {
      cout << line << endl;
    }
  }
};
