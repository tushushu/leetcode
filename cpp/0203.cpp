#include <stddef.h>
#include <iostream>
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
    ListNode *removeElements(ListNode *head, int val)
    {
        if (head == NULL)
        {
            return head;
        }
        ListNode node(0);
        ListNode *ret = &node;
        ListNode *tmp = head;
        ListNode *last = ret;
        ret->next = head;
        while (tmp != NULL)
        {
            if (tmp->val == val)
            {
                last->next = tmp->next;
                delete tmp;
            }
            else
            {
                last = tmp;
            }
            tmp = tmp->next;
        }
        return ret->next;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
