#!/usr/bin/env python3
"""A class used to represent a Node in a Decision Tree."""
import numpy as np


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
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        return 1


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
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        return self.root.count_nodes_below(only_leaves=only_leaves)
