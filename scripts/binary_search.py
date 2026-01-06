class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return f"{data} inserted successfully as the main root of the tree"
        else:
            return self.insert_recursive(self.root, data)

    def insert_recursive(self, sub_root, data):
        if data <= sub_root.data:
            if sub_root.left is None:
                sub_root.left = Node(data)
                return f"{data} inserted successfully to the left side of the tree"
            else:
                return self.insert_recursive(sub_root.left, data)
        else:
            if sub_root.right is None:
                sub_root.right = Node(data)
                return f"{data} inserted successfully to the right side of the tree"
            else:
                return self.insert_recursive(sub_root.right, data)

    def pre_order_traversal(self, sub_root):
        if sub_root is not None:
            print(sub_root.data, end=" ")
            self.pre_order_traversal(sub_root.left)
            self.pre_order_traversal(sub_root.right)
        else:
            return

    def post_order_traversal(self, sub_root):
        if sub_root is not None:
            self.post_order_traversal(sub_root.left)
            self.post_order_traversal(sub_root.right)
            print(sub_root.data, end=" ")
        else:
            return

    def in_order_traversal(self, sub_root):
        if sub_root is not None:
            self.in_order_traversal(sub_root.left)
            print(sub_root.data, end=" ")
            self.in_order_traversal(sub_root.right)
        else:
            return

    def get_main_root(self):
        if self.root is None:
            return "No nodes in the tree"
        else:
            return f"The main root of the tree is {self.root.data}"

    def get_min_value(self):
        if self.root is None:
            return "No nodes in the tree"
        else:
            current = self.root
            while current.left is not None:
                current = current.left
            return f"The minimum value in the tree is {current.data}"

    def get_max_value(self):
        if self.root is None:
            return "No nodes in the tree"
        else:
            current = self.root
            while current.right is not None:
                current = current.right
            return f"The maximum value in the tree is {current.data}"

    def find(self, data):
        if self.root is None:
            return "No nodes in the tree"
        elif self.root.data == data:
            return f"{data} found as the main root in the tree"
        else:
            return self.find_recursive(self.root, data)

    def find_recursive(self, sub_root, data):
        if data == sub_root.data:
            return f"{data} found in the tree"
        elif data < sub_root.data:
            if sub_root.left is None:
                return f"{data} not found in the tree"
            else:
                return self.find_recursive(sub_root.left, data)
        else:
            if sub_root.right is None:
                return f"{data} not found in the tree"
            else:
                return self.find_recursive(sub_root.right, data)

    @staticmethod
    def find_min_node(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, data):
        if self.root is None:
            return "No nodes in the tree"

        if self.root.data == data:
            if self.root.left is None and self.root.right is None:
                self.root = None
                return f"{data} deleted successfully from the tree (main root)"
            elif self.root.left is None:
                self.root = self.root.right
                return f"{data} deleted successfully (replaced with right child). Now the main root is {self.root.data}"
            elif self.root.right is None:
                self.root = self.root.left
                return f"{data} deleted successfully (replaced with left child). Now the main root is {self.root.data}"
            else:
                successor = self.find_min_node(self.root.right)
                self.root.data = successor.data
                self.root.right, _ = self.delete_recursive(self.root.right, successor.data)
                return f"{data} (root) deleted successfully (replaced with {successor.data})"

        else:
            self.root, msg = self.delete_recursive(self.root, data)
            return msg

    def delete_recursive(self, sub_root, data):
        if sub_root is None:
            return sub_root, f"{data} not found in the tree"

        if data < sub_root.data:
            sub_root.left, msg = self.delete_recursive(sub_root.left, data)
            return sub_root, msg

        elif data > sub_root.data:
            sub_root.right, msg = self.delete_recursive(sub_root.right, data)
            return sub_root, msg

        else:
            if sub_root.left is None and sub_root.right is None:
                return None, f"{data} deleted (leaf node)"

            elif sub_root.left is None:
                return sub_root.right, f"{data} deleted (had only right child)"

            elif sub_root.right is None:
                return sub_root.left, f"{data} deleted (had only left child)"

            else:
                successor = self.find_min_node(sub_root.right)
                original_data = sub_root.data
                sub_root.data = successor.data
                sub_root.right, _ = self.delete_recursive(sub_root.right, successor.data)
                return sub_root, f"{original_data} deleted (replaced with {successor.data})"

bst = BinarySearchTree()

print(bst.insert(10))
print(bst.insert(5))
print(bst.insert(15))
print(bst.insert(2))
print(bst.insert(7))
print(bst.insert(12))
print(bst.insert(18))
print(bst.insert(13))
print(bst.insert(17))

print("\nPre-Order:")
bst.pre_order_traversal(bst.root)
print("\nPost-Order:")
bst.post_order_traversal(bst.root)
print("\nIn-Order:")
bst.in_order_traversal(bst.root)

print("\n\nStats:")
print(bst.get_main_root())
print(bst.get_min_value())
print(bst.get_max_value())

print("\nFind Tests:")
print(bst.find(10))     # main root
print(bst.find(2))      # found
print(bst.find(17))     # found
print(bst.find(9))      # not found

print("\nDelete Tests:")
print(bst.delete(100))  # not found
print(bst.delete(2))    # leaf
print(bst.delete(5))    # one child
print(bst.delete(15))   # two children
print(bst.delete(10))   # main root
print("\nIn-Order After Deletions:")
bst.in_order_traversal(bst.root)
