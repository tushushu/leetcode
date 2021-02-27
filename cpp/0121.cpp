#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy_min = INT_MAX;
        int ret = 0;
        int profit;
        for (int i = 0; i < prices.size(); ++i)
        {
            profit = prices[i] - buy_min;
            if (profit > ret)
            {
                ret = profit;
            }
            buy_min = min(prices[i], buy_min);
        }
        return ret;
    }
};