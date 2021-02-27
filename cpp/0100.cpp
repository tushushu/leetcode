#include <stddef.h>
#include <queue>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution
{
public:
    bool isSameTree(TreeNode *t1, TreeNode *t2)
    {
        queue<TreeNode *> q;
        q.push(t1);
        q.push(t2);
        while (!q.empty())
        {
            t1 = q.front();
            q.pop();
            t2 = q.front();
            q.pop();
            if (t1 == NULL)
            {
                if (t2 == NULL)
                {
                    continue;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                if (t2 == NULL)
                {
                    return false;
                }
                else
                {
                    if (t1->val == t2->val)
                    {
                        q.push(t1->left);
                        q.push(t2->left);
                        q.push(t1->right);
                        q.push(t2->right);
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};