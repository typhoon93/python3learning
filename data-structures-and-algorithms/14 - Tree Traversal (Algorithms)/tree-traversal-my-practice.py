"""

Tree Traversal - get the values of every node in a list and put them in a list, and then we return that list.

# breadth first search (Level-Order)
Start at the top, then do the second row, then the third etc.. row by row.
qeueu [] - we store the nodes
results [] - we store the values

This method is used when you need to explore the tree level by level. 
This traversal technique is especially useful in scenarios like printing nodes in the tree level by level, 
or in certain algorithms like the shortest path in unweighted graphs or decision trees where all nodes at each level are evaluated.


# depth first search (3 types)
    ## preorder (Root, Left, Right) - we go to the left as much as we can, then go backwards and pick up the ones on the right. 
                    we go back to root and go right, then left first, until no nodes on the left -> then we pick out the ones on the right again.
                    we use recursion to do this.
                    useful for - creating a copy of the tree
    ## postorder  (Left, Right, Root) - we start at the top, but we do not write it on result.
                    we go to the left until there are no more left nodes.
                    we check the last node for a right node as well, if that is none too -> we write the value to results
                    once again we go back to the previous one, we check right etc.
                    tldr, traverse almostsame as preorder, but we append after checking left and right, instead of before.
                    useful for operations where you need to work with children nodes before their respective parent nodes, 
                    such as when calculating the size or height of the tree,
                    or when performing cleanup (destruction) tasks.

    ## inorder  (Left, Root, Right): - we go to the left once again as much as we can, same loop but we the traverse appends items before checking the right nodes.
        all of the numbers are written in numerical order
        useful for getting sorted data
"""


# breadth first search
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def dfs_post_order(self):
        """
        similar to preorder, but traverse appends after we go left and right, not before
        """
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)

            results.append(current_node.value)

            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.dfs_in_order())
