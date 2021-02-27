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
    ListNode *deleteDuplicates(ListNode *head)
    {
        ListNode *l = head;
        while (l != NULL)
        {
            while (l->next != NULL && l->next->val == l->val)
            {
                l->next = l->next->next;
            }
            l = l->next;
        }
        return head;
    }
};

int main(int argc, char const *argv[])
{
    ListNode nd1(1);
    ListNode nd2(1);
    ListNode nd3(2);
    ListNode *head = &nd1;
    head->next = &nd2;
    head->next->next = &nd3;
    Solution s;
    ListNode *ret = s.deleteDuplicates(head);
    while (ret)
    {
        cout << ret->val << endl;
        ret = ret->next;
    }
    return 0;
}
