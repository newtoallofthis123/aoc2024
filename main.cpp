#include "day5/1.cpp"
#include <bits/stdc++.h>
using namespace std;

const string INPUT_FILE = "day5/input.txt";

int main() {
  freopen(INPUT_FILE.c_str(), "r", stdin);

  auto sol = Day5_1();
  sol.debug_print();
}
