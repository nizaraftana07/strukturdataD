class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root

    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

# --- Eksekusi Bagian 1 ---
tree = BST()
data = [50, 30, 70, 20, 40, 60, 80]
for item in data:
    tree.root = tree.insert(tree.root, item)

print("--- Hasil Awal ---")
print("Preorder :", end=" "); tree.preorder(tree.root); print()
print("Inorder  :", end=" "); tree.inorder(tree.root); print()
print("Postorder:", end=" "); tree.postorder(tree.root); print()

# --- Eksekusi Bagian 2 (Penambahan Node) ---
new_data = [10, 90, 65]
for item in new_data:
    tree.root = tree.insert(tree.root, item)

print("\n--- Setelah Penambahan Node (10, 90, 65) ---")
print("Preorder :", end=" "); tree.preorder(tree.root); print()
print("Inorder  :", end=" "); tree.inorder(tree.root); print()
print("Postorder:", end=" "); tree.postorder(tree.root); print()
print("\n--- Struktur Pohon ---")
print("50")
print("        /    \\")
print("      30      70")
print("     /  \\    /  \\")
print("    20  40  60  80")
print("   /         \\    \\")
print("  10         65   90")
"""
ANALISIS PERUBAHAN:
1. Inorder: Tetap menampilkan urutan angka dari terkecil ke terbesar (terurut).
2. Struktur: Pohon menjadi lebih dalam dengan tambahan daun (leaf) baru.
3. Efisiensi: Penambahan 10, 90, dan 65 mengikuti jalur pencarian logaritmik.
"""