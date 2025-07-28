class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def createbst(root, val):
    if root is None:
        return TreeNode(val)
    else:
        if root.data == val:
            return root
        elif root.data < val:
            root.right = createbst(root.right, val)
        else:
            root.left = createbst(root.left, val)
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

def search(root, ele):
    if root is None:
        return False
    if root.data == ele:
        return True
    return search(root.left, ele) or search(root.right, ele)

def find_min(root):
    while root.left is not None:
        root = root.left
    return root

def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

    return root

def update_node(root, old_val, new_val):
    root = delete_node(root, old_val)
    root = createbst(root, new_val)
    return root

def find_floor(root, X):
    floor = None
    while root:
        if root.data == X:
            return root.data
        elif root.data > X:
            root = root.left
        else:
            floor = root.data
            root = root.right
    return floor

def find_ceil(root, X):
    ceil = None
    while root:
        if root.data == X:
            return root.data
        elif root.data < X:
            root = root.right
        else:
            ceil = root.data
            root = root.left
    return ceil

# Initial array
arr = [8, 3, 10, 1, 6, 14, 4, 7]

# Create BST
root = TreeNode(arr[0])
for i in range(1, len(arr)):
    root = createbst(root, arr[i])

# Print traversals
print("Preorder Traversal: ", end="")
preorder(root)
print()

print("Inorder Traversal: ", end="")
inorder(root)
print()

print("Postorder Traversal: ", end="")
postorder(root)
print()

# Search for an element
print("Search for 10:", search(root, 10))
print("Search for 20:", search(root, 20))

# Delete a node
root = delete_node(root, 6)
print("Inorder Traversal after deleting 6: ", end="")
inorder(root)
print()

# Update a node
root = update_node(root, 3, 5)
print("Inorder Traversal after updating 3 to 5: ", end="")
inorder(root)
print()

# Find floor and ceil
X = 12
print("Floor of", X, ":", find_floor(root, X))
print("Ceil of", X, ":", find_ceil(root, X))
