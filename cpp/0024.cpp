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
    ListNode *swapPairs(ListNode *head)
    {
        ListNode node(0);
        ListNode *ret = &node;
        ListNode *pre = ret;
        ListNode *cur = head;
        pre->next = cur;
        ListNode *next;
        ListNode *tmp;
        while (cur && cur->next)
        {
            next = cur->next;
            tmp = next->next;
            pre->next = next;
            next->next = cur;
            cur->next = tmp;
            pre = cur;
            cur = tmp;
        }
        return ret->next;
    }
};
