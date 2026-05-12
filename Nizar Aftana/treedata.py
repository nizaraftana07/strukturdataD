class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert Node
    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    # Preorder
    def preorder(self, root):

        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Inorder
    def inorder(self, root):

        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    # Postorder
    def postorder(self, root):

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")


# Membuat BST
tree = BST()

# Data awal
data = [50, 30, 70, 20, 40, 60, 80]

for item in data:
    tree.root = tree.insert(tree.root, item)

# Tambahan node baru
tambahan = [10, 90, 65]

for item in tambahan:
    tree.root = tree.insert(tree.root, item)

# Hasil Traversal
print("Preorder : ")
tree.preorder(tree.root)

print("\n\nInorder : ")
tree.inorder(tree.root)

print("\n\nPostorder : ")
tree.postorder(tree.root)