#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int ret = 0;
        for (int i = 0; i < s.size(); ++i){
            ret *= 26;
            ret += (s[i] - 64);
        }
        return ret;
    }
};

int main(int argc, const char** argv) {
    Solution my_solution;
    vector<string> inputs = {"A", "B", "Z", "AA", "AB", "AZ", "ZZ", "AAA"};
    vector<int> outputs = {1, 2, 26, 27, 28, 52, 702, 703};
    for (int i = 0; i < inputs.size(); ++i){
        cout << inputs[i] << endl;
        cout << my_solution.titleToNumber(inputs[i]) << endl;
        cout << outputs[i] << endl;
        cout << endl;
    }
    
    return 0;
}