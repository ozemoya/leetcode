
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = [root]

        while queue:
            # Why? : BFS, Each time we are going one level lower
            childrenCount = len(queue)

            # Why? : To add all the children from current level
            children = []

            for _ in range(childrenCount):
                child = queue.pop(0)
                if child:
                    children.append(child.val)
                    queue.append(child.left)
                    queue.append(child.right)

            # Why? : We might add `None` nodes.
            if children:
                res.append(children)
        return res