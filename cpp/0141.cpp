#include <iostream>
#include <stddef.h>
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
    bool hasCycle(ListNode *head)
    {
        if (head == NULL)
        {
            return false;
        }
        ListNode *l1 = head;
        ListNode *l2 = l1;
        ListNode nd(0);
        while (l1)
        {
            if (&(*l1) == &nd)
            {
                return true;
            }
            l1 = l1->next;
            l2->next = &nd;
            l2 = l1;
        }
        return false;
    }
};