# lowest common ancestor


from binary_tree.base import BinaryTree, Node, print_tree
from binary_tree.level_up_order_structure import LevelUpOrder



class LCA(BinaryTree):

    def find_lca(self, root, p, q):
        if root is None:
            return None

        if root.data in [p, q]:
            return root

        left_result = self.find_lca(root.left, p, q)
        right_result = self.find_lca(root.right, p, q)

        if left_result and right_result:
            return root
        elif left_result is None and right_result:
            return right_result
        elif right_result is None and left_result:
            return left_result
        else:
            return None


arrayl = [1, 2, 4, 3]
luo = LevelUpOrder()
final_tree = luo.tree_order(arrayl, len(arrayl), 0, None)
print_tree(final_tree)

result = LCA().find_lca(final_tree, 9, 10)
print("LCA is -----------------------------")
print(result.data)
