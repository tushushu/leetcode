#include <stddef.h>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *ret = new ListNode(0);
        ListNode *head = ret;
        int current = 0;
        int next = 0;
        while (l1 != NULL || l2 != NULL)
        {
            if (l1 != NULL)
            {
                current += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL)
            {
                current += l2->val;
                l2 = l2->next;
            }
            current += next;
            next = current / 10;
            head->next = new ListNode(current % 10);
            head = head->next;
            current = 0;
        }
        if (next)
        {
            head->next = new ListNode(next);
        }
        return ret->next;
    }
};