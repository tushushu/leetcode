#include <stddef.h>
#include <vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    inline ListNode *helper(ListNode *node1, ListNode *node2)
    {
        ListNode tmp(0);
        ListNode *node = &tmp;
        ListNode *ret = node;
        while (node1 && node2)
        {
            if (node1->val < node2->val)
            {
                node->next = node1;
                node1 = node1->next;
            }
            else
            {
                node->next = node2;
                node2 = node2->next;
            }
            node = node->next;
        }
        if (node1)
        {
            node->next = node1;
        }
        else
        {
            node->next = node2;
        }
        return ret->next;
    }

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.empty())
        {
            return NULL;
        }
        int j = 0;
        int n = lists.size();
        while (n > 1)
        {
            for (int i = 0; i < n; i += 2)
            {
                if (i + 1 < n)
                {
                    lists[j] = helper(lists[i], lists[i + 1]);
                }
                else
                {
                    lists[j] = lists[i];
                }
                ++j;
            }
            n = j;
            j = 0;
        }
        return lists[0];
    }
};