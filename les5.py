class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_full_binary_tree(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)
    return False

def is_perfect_binary_tree(root, depth=0):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return depth
    left_depth = is_perfect_binary_tree(root.left, depth + 1)
    right_depth = is_perfect_binary_tree(root.right, depth + 1)
    return left_depth == right_depth

def is_complete_binary_tree(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)
        else:
            while queue:
                if queue.pop(0) is not None:
                    return False
    return True

def is_balanced_binary_tree(root):
    def check_height(root):
        if root is None:
            return 0
        left_height = check_height(root.left)
        right_height = check_height(root.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return check_height(root) != -1


def __init__(self):
    self.root = None
 
 
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1
 
 
def getcol(h):
    if h == 1:
        return 1
    return getcol(h-1) + getcol(h-1) + 1
 
 
def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.value
    printTree(M, root.left, col-pow(2, height-2), row+1, height-1)
    printTree(M, root.right, col+pow(2, height-2), row+1, height-1)
 
 
def TreePrinter():
    h = height(root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M,root, col//2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")
 
root = TreeNode(42)
root.left = TreeNode(22)
root.right = TreeNode(1213)
root.left.left = TreeNode(432)
root.left.right = TreeNode(5212)
root.right.left = TreeNode(6213)
root.right.right = TreeNode(3217)
root.right.right.right = TreeNode(3217)


TreePrinter()


print("Повне бін дерево:", is_full_binary_tree(root))
print("Ідеальне бін дерево:", is_perfect_binary_tree(root) != -1)
print("Завершене бін дерево", is_complete_binary_tree(root))
print("Збалансоване бін дерево:", is_balanced_binary_tree(root))




