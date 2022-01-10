# Not recommended
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'stack')))
from stack import Stack

from queue import Queue

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type, start, traversal=""):
        """
        # Python 3.10
        match traversal_type:
            case "preorder":
                return self.preorder_print(start, traversal)
            case "inorder":
                return self.inorder_print(start, traversal)
            case "postorder":
                return self.postorder_print(start, traversal)
            case "levelorder":
                return self.levelorder_print(start)
            case "reverse_levelorder":
                return self.reverse_levelorder_print(start)
            case _:
                print("Traversal type " + str(traversal_type) + " is not supported.")
                return False
        """
        
        # Older python
        if traversal_type == "preorder":
            return self.preorder_print(start, traversal)
        elif traversal_type == "inorder":
            return self.inorder_print(start, traversal)
        elif traversal_type == "postorder":
            return self.postorder_print(start, traversal)
        elif traversal_type == "levelorder":
            return self.levelorder_print(start)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(start)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")  
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)        
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")  
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:    
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)

    def size_iterative(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                stack.push(node.left)
                size += 1
            if node.right:
                stack.push(node.right)
                size += 1
        return size