

from binary_tree.base import Node, BinaryTree, print_tree


class LevelUpOrder(BinaryTree):

    def tree_order(self, arr, n, i, root):
        if i < n:
            if root is None:
                root = Node(arr[i])
            if root.left is None:
                root.left = self.tree_order(arr, n, i*2 + 1, root.left)
            if root.right is None:
                root.right = self.tree_order(arr, n, i*2 + 2, root.right)
        return root


array = list(range(25))
luo = LevelUpOrder()
final_tree = luo.tree_order(array, len(array), 0, None)
print_tree(final_tree)