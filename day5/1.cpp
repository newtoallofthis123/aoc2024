#include "../common.h"
#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Day5_1 {
private:
    map<int, vector<int>> rules;
    vector<map<int, int>> lines;
    vector<int> mids;
    int total = 0;

    int find_key(map<int, int>& m, int idx)
    {
        for (auto c : m) {
            if (c.second == idx) {
                return c.first;
            }
        }
        return -1;
    }

public:
    string output {};
    Day5_1() { solve(); }

    bool checkLine(map<int, int> line)
    {
        for (auto c : line) {
            int ele = c.first;
            int idx = c.second;

            if (rules.find(ele) != rules.end()) {
                auto nums = rules[ele];
                for (auto num : nums) {
                    if (line.find(num) != line.end()) {
                        if (line[num] < idx)
                            return false;
                    }
                }
            }
        }
        return true;
    }

    void solve()
    {
        string line;
        while (getline(cin, line) && line != "") {
            auto num1 = stoi(line.substr(0, 2));
            auto num2 = stoi(line.substr(3, 2));
            rules[num1].PB(num2);
        }

        while (getline(cin, line)) {
            map<int, int> temp;
            int idx = 0;
            for (size_t i = 0; i < line.size(); i += 3) {
                auto num1 = stoi(line.substr(i, 2));
                temp[num1] = idx;
                idx++;
            }
            mids.PB((int)temp.size() / 2);
            lines.PB(temp);
        }

        for (size_t i = 0; i < lines.size(); i++) {
            auto line = lines[i];
            if (checkLine(line)) {
                int key = find_key(line, mids[i]);
                if (key == -1) {
                    cerr << "Key not found" << endl;
                }
                total += key;
            }
        }
    }

    void print_output()
    {
        output = to_string(total);
        cout << "Output: " << output << endl;
    }

    void debug_print()
    {
        for (auto c : rules) {
            cout << "a: " << c.first << " b: ";
            for (auto d : c.second) {
                cout << d << " ";
            }
            cout << endl;
        }

        cout << "Lines" << "\n";
        for (auto l : lines) {
            for (auto c : l) {
                cout << c.first << " " << c.second << " ";
            }
            cout << "\n";
        }
        cout << total << endl;
    }
};
