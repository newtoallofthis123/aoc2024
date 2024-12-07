#include "../common.h"
#include <bits/stdc++.h>
#include <string>
using namespace std;

class Day7_1 {
private:
    map<long long, vector<int>> mat;
    long long total {};

public:
    string output {};
    Day7_1() { solve(); }

    void generate_combs(size_t n, vector<char> current,
        vector<vector<char>>& result)
    {
        if (current.size() == n) {
            result.push_back(current);
            return;
        }

        current.push_back('+');
        generate_combs(n, current, result);
        current.pop_back();

        current.push_back('*');
        generate_combs(n, current, result);
        current.pop_back();
    }

    bool isPossible(long long res, vector<int> nums)
    {
        vector<vector<char>> combinations;
        vector<char> current;

        generate_combs(nums.size() - 1, current, combinations);

        for (auto comb : combinations) {
            long long curr = nums[0];
            for (int i = 1; i < (int)nums.size(); i++) {
                if (comb[i - 1] == '+') {
                    curr += nums[i];
                } else {
                    curr *= nums[i];
                }
            }

            if (curr == res) {
                return true;
            }
        }

        return false;
    }

    void solve()
    {
        string line;
        while (getline(cin, line)) {
            stringstream ss(line);
            string num;
            ss >> num;
            num.pop_back();
            long long parent = stoll(num);
            while (ss >> num) {
                int child = stoi(num);
                mat[parent].push_back(child);
            }
        }
        for (auto const& [key, val] : mat) {
            if (isPossible(key, val)) {
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
        for (auto const& [key, val] : mat) {
            cout << key << ": ";
            for (auto v : val) {
                cout << v << " ";
            }
            cout << endl;
        }
    }
};
