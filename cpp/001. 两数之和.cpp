class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
            int n = numbers.size();
            vector<int> result;
            map<int, int> index;
            for (int i = 0; i < n; i++) {
                if (index.count(numbers[i]) != 0) {
                    // if exists
                    result.push_back(index[numbers[i]] + 1);
                    result.push_back(i + 1);
                    break;
                } 
                index[target - numbers[i]] = i; 
            }
            return result;
    }
};