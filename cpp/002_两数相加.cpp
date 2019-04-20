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
  int getNumber(ListNode *l)
  {
    ListNode *head = l;
    int ret = 0, n = 1;
    while (head != NULL)
    {
      ret += head->val * n;
      head = head->next;
      n *= 10;
    }

    return ret;
  };

  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
  {
    int num = this->getNumber(l1) + this->getNumber(l2);

    ListNode *ret = new ListNode(0);
    ListNode *head = ret;
    int k;
    while (num != 0)
    {
      k = num % 10;
      num = num / 10;
      head->next = new ListNode(k);
      head = head->next;
    }
    return ret->next;
  }
};