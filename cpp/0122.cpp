#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() < 2)
        {
            return 0;
        }
        int ret = 0;
        int last_buy;
        int i = 0;
        int n = prices.size();
        prices.push_back(INT_MIN);
        while (i < n)
        {
            while (i < n && prices[i] <= prices[++i]);
            last_buy = prices[i];
            while (i < n && prices[i] < prices[++i]);
            ret += prices[i - 1] - last_buy;
        }
        return ret;
    }
};