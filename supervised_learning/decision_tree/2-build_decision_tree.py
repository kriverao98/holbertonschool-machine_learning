#!/usr/bin/env python3
"""A class used to represent a Node in a Decision Tree."""
import numpy as np


def left_child_add_prefix(text):
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += ("    |  " + x) + "\n"
    return new_text


def right_child_add_prefix(text):
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += "       " + x + "\n"
    return new_text


class Node:
    """
    A class used to represent a Node in a Decision Tree.
    """
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Calculate the maximum depth of the tree below
        the current node.
        Returns:
            int: The maximum depth of the tree below
            the current node.
        """
        if self.is_leaf:
            return self.depth
        left_depth = (self.left_child.max_depth_below()
                      if self.left_child else self.depth)
        right_depth = (self.right_child.max_depth_below()
                       if self.right_child else self.depth)
        return max(left_depth, right_depth)

    def count_nodes_below(self, only_leaves=False):
        """
        Count the number of nodes below the current node in the
        decision tree.

        Returns:
        int: The number of nodes below the current node.
        If only_leaves is True, returns the number of leaf nodes.
        Otherwise, returns the total number of nodes.
        """
        if only_leaves:
            if self.left_child is None and self.right_child is None:
                return 1
            left_count = (
                self.left_child.count_nodes_below(only_leaves=True)
                if self.left_child else 0
            )
            right_count = (
                self.right_child.count_nodes_below(only_leaves=True)
                if self.right_child else 0
            )
            return left_count + right_count
        else:
            left_count = (
                self.left_child.count_nodes_below(only_leaves=False)
                if self.left_child else 0
            )
            right_count = (
                self.right_child.count_nodes_below(only_leaves=False)
                if self.right_child else 0
            )
            return 1 + left_count + right_count

    def __str__(self):
        """
        Generate a string representation of the node and its subtree.
        """
        text = f"[X{self.feature} < {self.threshold}]\n"
        if self.left_child:
            text += left_child_add_prefix(str(self.left_child))
        if self.right_child:
            text += right_child_add_prefix(str(self.right_child))
        return text


class Leaf(Node):
    """
    A class used to represent a Leaf in a Decision Tree.
    """
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        Returns the maximum depth
        of the decision tree below the current node.
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
        Counts the number of nodes below
        the current node in the decision tree.
        """
        return 1

    def __str__(self):
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """
    A class used to represent a Decision Tree.
    """
    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
        Calculate the depth of the decision tree.
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
        Count the number of nodes in the decision tree.
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        return self.root.__str__()
