import sys

def postOrder(preorder, inorder):
    if len(preorder) == 0:
        return

    elif len(preorder) == 1:
        print(preorder[0], end = ' ')
        return

    elif len(preorder) == 2:
        print(preorder[1], end = ' ')
        print(preorder[0], end = ' ')
        return

    root_idx = inorder.index(preorder[0])

    inorder_left = inorder[0:root_idx]
    preorder_left = preorder[1:len(inorder_left) + 1]
    postOrder(preorder_left, inorder_left)

    inorder_right = inorder[root_idx + 1:]
    preorder_right = preorder[len(inorder_left) + 1:]
    postOrder(preorder_right, inorder_right)

    print(preorder[0], end = ' ')
    


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postOrder(preorder, inorder)
    print()