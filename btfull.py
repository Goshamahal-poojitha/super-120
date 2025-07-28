class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def create_btree(arr, i, n):
    if i > n:
        return None
    
    root = TreeNode(arr[i - 1])
    root.left = create_btree(arr, 2 * i, n)
    root.right = create_btree(arr, 2 * i + 1, n)
    
    return root

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def levelorder(root):
    if root is None:
        return []
    
    result = []
    queue = [root]  
    while queue:
        node = queue.pop(0)  
        result.append(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def search_levelorder(root, ele):
    if root is None:
        return False
    queue = []  
    queue.append(root)
    while queue:
        node = queue.pop(0)  
        
        if node.data == ele:
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False

def search_preorder(root, ele):
    if root is None:
        return False
    
    if root.data == ele:
        return True
    
    return search_preorder(root.left, ele) or search_preorder(root.right, ele)

def search_inorder(root, ele):
    if root is None:
        return False
    
    if search_inorder(root.left, ele):
        return True
    
    if root.data == ele:
        return True
    return search_inorder(root.right, ele)

def search_postorder(root, ele):
    if root is None:
        return False
    if search_postorder(root.left, ele):
        return True
    if search_postorder(root.right, ele):
        return True
    if root.data == ele:
        return True
    return False

arr = [3, 4, 5, 6, 7, 8, 9, 0]
binary_tree = create_btree(arr, 1, len(arr))

print("Preorder Traversal:")
preorder(binary_tree)
print("\nInorder Traversal:")
inorder(binary_tree)
print("\nPostorder Traversal:")
postorder(binary_tree)
print("\nLevelorder Traversal:")
print(levelorder(binary_tree))

print("\nSearch for element 11:")
print("Levelorder:", search_levelorder(binary_tree, 11))
print("Preorder:", search_preorder(binary_tree, 11))
print("Inorder :", search_inorder(binary_tree, 11))
print("Postorder:", search_postorder(binary_tree, 11))

print("\nSearch for element 7:")
print("Levelorder Search:", search_levelorder(binary_tree, 7))
print("Preorder Search:", search_preorder(binary_tree, 7))
print("Inorder Search:", search_inorder(binary_tree, 7))
print("Postorder Search:", search_postorder(binary_tree, 7))