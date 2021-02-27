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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2)
    {
        ListNode ret(0);
        ListNode *l = &ret;
        while (l1 != NULL && l2 != NULL)
        {
            if (l1->val < l2->val)
            {
                l->next = l1;
                l1 = l1->next;
            }
            else
            {
                l->next = l2;
                l2 = l2->next;
            }
            l = l->next;
        }
        l->next = l1 == NULL ? l2 : l1;
        return ret.next;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
