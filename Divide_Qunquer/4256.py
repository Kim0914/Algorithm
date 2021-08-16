import sys

# 루트를 기준으로 중위(inorder)순회한 결과의 왼쪽은 왼쪽 서브트리, 오른쪽 서브트리
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

    inorder_left = inorder[0:root_idx] # inorder에서는 처음부터 루트 인덱스 까지가 왼쪽 서브트리
    preorder_left = preorder[1:len(inorder_left) + 1] # preorder에서는 1부터 inorder_left의 갯수만큼이 왼쪽 서브트리
    postOrder(preorder_left, inorder_left) # 재귀적으로 반복

    inorder_right = inorder[root_idx + 1:] # inorder에서는 루트 다음부터 마지막 까지가 오른쪽 서브트리
    preorder_right = preorder[len(inorder_left) + 1:] # preorder에서는 inorder_right의 갯수만큼 부터 마지막 까지가 오른쪽 서브트리
    postOrder(preorder_right, inorder_right) # 반복

    print(preorder[0], end = ' ') # 후위(postorder) 방식에서 루트노드는 제일 마지막 => 루트노드 값 출력
    


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postOrder(preorder, inorder)
    print()