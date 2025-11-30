from python.isSubtree import Solution, TreeNode

def build_tree(values):
	"""Helper to build a binary tree from a list (level-order)."""

	if not values:
		return None

	nodes = [TreeNode(val) if val is not None else None for val in values]
	kids = nodes[::-1]
	root = kids.pop()
	for node in nodes:
		if node:
			if kids:
				node.left = kids.pop()
			if kids:
				node.right = kids.pop()
	return root


def test_isSubtree_true_simple():
    s = build_tree([3, 4, 5, 1, 2])
    t = build_tree([4, 1, 2])
    assert Solution().isSubtree(s, t) is True


def test_isSubtree_false_extra_node():
    s = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    t = build_tree([4, 1, 2])
    assert Solution().isSubtree(s, t) is False

def test_isSubtree_same_tree():
    s = build_tree([1, 2, 3])
    t = build_tree([1, 2, 3])
    assert Solution().isSubtree(s, t) is True

def test_isSubtree_t_empty():
    s = build_tree([1, 2, 3])
    t = build_tree([])
    assert Solution().isSubtree(s, t) is True

def test_isSubtree_s_empty():
    s = build_tree([])
    t = build_tree([1])
    assert Solution().isSubtree(s, t) is False

def test_isSubtree_deep_subtree():
    s = build_tree([1, 2, 3, None, None, 4, 5])
    t = build_tree([3, 4, 5])
    assert Solution().isSubtree(s, t) is True