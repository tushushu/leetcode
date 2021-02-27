#include <stddef.h>
#include <iostream>
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
private:
    bool _ret = false;
    int _target;

private:
    void _hasPathSum(TreeNode *node, int current)
    {
        // cout << "current is " << current << " target is " << target << "\n";
        if (this->_ret == true || node == NULL)
        {
            return;
        }
        current += node->val;
        if (node->left == NULL && node->right == NULL){
            this->_ret = (current == this->_target);
            return;
        }
        _hasPathSum(node->left, current);
        _hasPathSum(node->right, current);
    }

public:
    bool hasPathSum(TreeNode *root, int sum)
    {
        this->_target = sum;
        _hasPathSum(root, 0);
        return this->_ret;
    }
};

int main()
{
    Solution s;
    TreeNode *root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(0);
    // root->left->left = new TreeNode(4);
    // root->left->right = new TreeNode(4);
    // root->right->left = new TreeNode(4);
    // root->right->right = new TreeNode(4);
    bool ret = s.hasPathSum(root, 1);
    cout << "The result is: " << ret << "\n";
    return 0;
}
