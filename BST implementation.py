# Exercise of implementing a BST from scratch
from queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if value is None:
            exit

        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.root

            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value > parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
                else:
                    raise Exception('Duplicates are not allowed')

        return new_node

    def lookup(self, value):
        node = self.root

        while node is not None:
            if value == node.value:
                break
            elif value < node.value:
                node = node.left
            else:
                node = node.right

        return node is not None

    def overwrite_node(self, parent_node, old_node, new_node):
        if parent_node is None:
            self.root = new_node
        elif old_node == parent_node.left:
            parent_node.left = new_node
        elif old_node == parent_node.right:
            parent_node.right = new_node
        else:
            raise Exception('Node not found')

    def remove(self, value):
        if self.root is None:
            return False

        parent_node = None
        node = self.root

        # Find the node and its parent
        while node is not None:
            if value == node.value:
                break
            elif value < node.value:
                parent_node = node
                node = node.left
            else:
                parent_node = node
                node = node.right

        # We now need to re-organize the tree
        # Easy cases, where node only has one child or none
        if (node.left is None) and (node.left is None):
            self.overwrite_node(parent_node, node, None)
        elif node.left is None and node.right is not None:
            self.overwrite_node(parent_node, node, node.right)
        elif node.left is not None and node.right is None:
            self.overwrite_node(parent_node, node, node.left)
        else:
            # More complex scenario, we will need to reorganize the tree.
            # We prioritize the left node, because.
            self.overwrite_node(parent_node, node, node.left)

            # We go down the tree until we find a free right-sided node
            current_node = node.left

            while True:
                if node.right.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = node.right
                        break
                    else:
                        current_node = current_node.left
                elif node.right.value > current_node.value:
                    if current_node.right is None:
                        current_node.right = node.right
                        break
                    else:
                        current_node = current_node.right
                else:
                    raise Exception('Duplicates are not allowed')

    def print_tree(self):
        if self.root is not None:
            print('BFS: ')
            print_bfs(self.root)
            print()
            print('DFS: ')
            print_dfs(self.root)


# Breadth-First Search\Traversal
def print_bfs(curr_node):
    if curr_node is not None:
        node_queue = Queue()
        node_queue.put(curr_node)

        while not node_queue.empty():
            curr_node = node_queue.get()
            print(str(curr_node.value))

            if curr_node.left:
                node_queue.put(curr_node.left)

            if curr_node.right:
                node_queue.put(curr_node.right)


# Depth-First Search\Traversal
def print_dfs(curr_node):
    if curr_node is not None:
        print(str(curr_node.value))
        print_dfs(curr_node.left)
        print_dfs(curr_node.right)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print_tree()
# tree.remove(9)
# tree.print_tree()
# tree.remove(6)
# tree.print_tree()
