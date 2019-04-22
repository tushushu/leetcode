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
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
  {
    ListNode *ret = new ListNode(0);
    ListNode *head = ret;
    int num, tmp = 0;
    while (l1 != NULL || l2 != NULL)
    {
      num = tmp + (l1 != NULL ? l1->val : 0) + (l2 != NULL ? l2->val : 0);
      tmp = num / 10;
      head->next = new ListNode(num % 10);
      head = head->next;
      if (l1 != NULL)
      {
        l1 = l1->next;
      }
      if (l2 != NULL)
      {
        l2 = l2->next;
      }
    }
    if (tmp)
    {
      head->next = new ListNode(tmp);
    }
    return ret->next;
  }
};