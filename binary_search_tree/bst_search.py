def search(root, x):
    if x == root.val:
        return True

    if x < root.val:
        ret = search(root.left, x)
    else:
        ret = search(root.right, x)

    return ret


class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = BST(4)
root.left = BST(2)
root.right = BST(6)
root.left.left = BST(1)
root.left.right = BST(3)
root.right.left = BST(5)
root.right.right = BST(7)

print(search(root, 5))
