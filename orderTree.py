import math

# completed binary tree
# i = index of the floor = n - 2 ** (f - 1) if f > 1 else 1
# f = floor of number = math.log(n + 1, 2)
# n = numbebr of position
# position start from 1
# l = left child node = r - 1
# r = right child node = 2 ** f - 1 + 2 * i

def orderTree(tree, root, method):
    if len(tree) < root : return [] 
    f = round(math.log(root + 1, 2))
    i = root - 2 ** (f - 1) + 1
    r = int(2 ** f - 1 + 2 * i)
    l = r -1
    if (method == 'preOrder'):
        return [tree[root - 1]] + orderTree(tree, l, 'preOrder')+ orderTree(tree, r, 'preOrder')
    elif (method == 'inOrder'):
        return orderTree(tree, l, 'inOrder') + [tree[root - 1]] + orderTree(tree, r, 'inOrder')
    elif (method == 'postOrder'):
        return orderTree(tree, l, 'postOrder') + orderTree(tree, r, 'postOrder') + [tree[root - 1]]

def arrayToInt(arr):
    return list(map(int, arr))

if __name__ == '__main__':
    x = input('Input：')[1:-1]
    if len(x) == 0 :
        print('Please input a non-empty array')
    else:
        x = x.split(',') 
        preorder = arrayToInt(orderTree(x, 1, 'preOrder'))
        inorder = arrayToInt(orderTree(x, 1, 'inOrder'))
        postorder = arrayToInt(orderTree(x, 1, 'postOrder'))
        print('Ourput:')
        print('Preorder', preorder)
        print('Inorder', inorder)
        print('Postorder', postorder)
    