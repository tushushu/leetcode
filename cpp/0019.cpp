#include <iostream>
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
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        vector<ListNode *> v;
        ListNode *node = head;
        while (node != NULL)
        {
            v.push_back(node);
            node = node->next;
        }
        int m = v.size();
        v.push_back(NULL);
        v[m - n - 1]->next = v[m - n + 1];
        return head;
    }
};