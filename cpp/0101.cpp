#include <iostream>
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
    bool isSymmetric(TreeNode *root)
    {
        if (root == NULL)
        {
            return true;
        }
        queue<TreeNode *> que;
        que.push(root->left);
        que.push(root->right);
        TreeNode *left;
        TreeNode *right;
        while (que.size())
        {
            left = que.front();
            que.pop();
            right = que.front();
            que.pop();
            if (left == NULL)
            {
                if (right != NULL)
                {
                    return false;
                }
            }
            else
            {
                if (right == NULL || left->val != right->val)
                {
                    return false;
                }
            }
            if (left && right)
            {
                que.push(left->left);
                que.push(right->right);
                que.push(left->right);
                que.push(right->left);
            }
        }
        return true;
    }
};