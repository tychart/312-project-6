# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     """
    #     Returns a string representation of the binary tree, formatted to
    #     resemble a tree structure.
    #     """
    #     if not self:
    #         return "Empty Tree"

    #     def get_height(node):
    #         if not node:
    #             return 0
    #         return 1 + max(get_height(node.left), get_height(node.right))

    #     def get_width(node):
    #         if not node:
    #             return 0
    #         if not node.left and not node.right:
    #             return 1
    #         return get_width(node.left) + get_width(node.right)

    #     def build_string(node, curr_height, height, curr_width, total_width, string_list):
    #         if not node:
    #             return
    #         # Calculate the position for the current node
    #         left_width = get_width(node.left)
    #         node_position = curr_width + left_width
    #         # Add the node value to the string list at the correct position
    #         string_list[curr_height][node_position] = str(node.val)

    #         # Recursively build the string for the left and right children
    #         build_string(node.left, curr_height + 1, height, curr_width, total_width, string_list)
    #         build_string(node.right, curr_height + 1, height, node_position + 1, total_width, string_list)
    #     height = get_height(self)
    #     total_width = 2**(height-1) # Maximum possible width, adjusted.
    #     string_list = [[" " for _ in range(total_width)] for _ in range(height)]

    #     build_string(self, 0, height, 0, total_width, string_list)
    #     result = "\n".join(["".join(row) for row in string_list])
    #     return result




class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        print_tree(root)

        print(p.val)
        print(q.val)

            
        p_path = self.recurse(root, p.val)
        q_path = self.recurse(root, q.val)

        print(p_path)
        print(q_path)

        if q.val in p_path:
            return q
        
        if p.val in q_path:
            return p
        
        if len(p_path) >= len(q_path):
            for i in range(len(q_path)):
                if q_path[i] in p_path:
                    return TreeNode(q_path[i])
        else:
            for i in range(len(p_path)):
                if p_path[i] in q_path:
                    return TreeNode(p_path[i])
    
    def recurse(self, curr_tree: TreeNode, val: int) -> list[int]:
        # print_tree(curr_tree)

        if curr_tree.val == val:
            return [val]

        if curr_tree.left == None:
            if curr_tree.right == None: # Handle if is leaf
                return None
        
            if curr_tree.right.val == val:
                return [val, curr_tree.val]
        
            right = self.recurse(curr_tree.right, val)
            if right == None:
                return None    
            right.append(curr_tree.val)
            return right

        if curr_tree.right == None:
            if curr_tree.left.val == val:
                return [val, curr_tree.val]
            
            left = self.recurse(curr_tree.left, val)
            if left == None:
                return None
            left.append(curr_tree.val)
            return left

        if curr_tree.left.val == val or curr_tree.right.val == val:
            return [val, curr_tree.val]
        
        left = self.recurse(curr_tree.left, val)
        right = self.recurse(curr_tree.right, val)

        if left == None:
            if right == None:
                return None
            right.append(curr_tree.val)
            return right
        left.append(curr_tree.val)
        return left
    
    # def traceback(self, start_index: int):
    #     out_path = []
    #     # for i in range(start_index // 2, 0, :
        
    #     i = start_index
    #     while i >= 0:

    #         out_path.append(self.tree[i])
    #         i = (i - 1) // 2
    #     return out_path




# Helper function to create a TreeNode from a list (for testing)
def create_tree_from_list(data):
    if not data:
        return None
    root = TreeNode(data[0])
    queue = [root]
    i = 1
    while queue and i < len(data):
        node = queue.pop(0)
        if data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1
    return root


# def flatten_tree_to_list(root: TreeNode) -> list:
#     """
#     Flattens a binary tree into a list representation using level-order traversal,
#     ensuring all levels are represented with None for missing nodes.

#     Args:
#         root: The root of the binary tree (TreeNode).

#     Returns:
#         A list representing the level-order traversal of the tree, with None
#         values filling in missing nodes at all levels.
#     """
#     if not root:
#         return []

#     result = []
#     queue = [root]


#     # for level in 



#     while queue:
#         node = queue.pop(0)
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#             if len(queue) > 0:
#                 queue.append(None)
#                 queue.append(None)
#     return result

def print_tree(tree):
    """
    Returns a string representation of the binary tree, formatted to
    resemble a tree structure.
    """
    if not tree:
        return "Empty Tree"

    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    def get_width(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return get_width(node.left) + get_width(node.right)

    def build_string(node, curr_height, height, curr_width, total_width, string_list):
        if not node:
            return
        # Calculate the position for the current node
        left_width = get_width(node.left)
        node_position = curr_width + left_width
        # Add the node value to the string list at the correct position
        string_list[curr_height][node_position] = str(node.val)

        # Recursively build the string for the left and right children
        build_string(node.left, curr_height + 1, height, curr_width, total_width, string_list)
        build_string(node.right, curr_height + 1, height, node_position + 1, total_width, string_list)
    height = get_height(tree)
    total_width = 2**(height-1) # Maximum possible width, adjusted.
    string_list = [[" " for _ in range(total_width)] for _ in range(height)]

    build_string(tree, 0, height, 0, total_width, string_list)
    result = "\n".join(["".join(row) for row in string_list])
    print("Printing Tree-----------------")
    print(result)


# Example 2 test case
# tree2_data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
# root2 = create_tree_from_list(tree2_data)
# # print(root2)
# p2 = TreeNode(5)
# q2 = TreeNode(4)
# # find_nodes(root2, 5, 4)

# solution = Solution()
# lca2 = solution.lowestCommonAncestor(root2, p2, q2)
# print(f"LCA of nodes with values 5 and 4 in Example 2: {lca2.val if lca2 else None}")


# Example 3 test case
tree3_data = [37,-34,-48,None,-100,-101,48,None,None,None,None,-54,None,-71,-22,None,None,None,8]
root3 = create_tree_from_list(tree3_data)
# print(root2)
p3 = TreeNode(-71)
q3 = TreeNode(8)
# find_nodes(root2, 5, 4)

solution3 = Solution()
lca3 = solution3.lowestCommonAncestor(root3, p3, q3)
print(f"LCA of nodes with values 5 and 4 in Example 2: {lca3.val if lca3 else None}")