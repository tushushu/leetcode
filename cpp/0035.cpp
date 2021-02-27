#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int low = 0;
        int high = nums.size() - 1;
        int mid;
        while (low <= high)
        {
            mid = low + (high - low) / 2; //In case of integer overflow
            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] < target)
            {
                low = mid + 1;
            }
            else
            {
                high = mid - 1;
            }
        }
        return low;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    vector<int> v = {1, 3, 5, 6};
    Solution s;
    cout << 5 << ' ' << s.searchInsert(v, 5) << endl;
    cout << 2 << ' ' << s.searchInsert(v, 2) << endl;
    cout << 7 << ' ' << s.searchInsert(v, 7) << endl;
    cout << 0 << ' ' << s.searchInsert(v, 0) << endl;
    v.resize(0);
    cout << 7 << ' ' << s.searchInsert(v, 7) << endl;
    v.push_back(2);
    cout << 5 << ' ' << s.searchInsert(v, 5) << endl;
    cout << 2 << ' ' << s.searchInsert(v, 2) << endl;
    cout << 7 << ' ' << s.searchInsert(v, 7) << endl;
    cout << 0 << ' ' << s.searchInsert(v, 0) << endl;
    cout << 3 << ' ' << s.searchInsert(v, 3) << endl;
    return 0;
}
