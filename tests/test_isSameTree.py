from python.isSameTree import Solution, TreeNode

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

def test_same_tree_identical():
	p = build_tree([1,2,3])
	q = build_tree([1,2,3])
	assert Solution().isSameTree(p, q) is True

def test_same_tree_different_structure():
    p = build_tree([1,2])
    q = build_tree([1,None,2])
    assert Solution().isSameTree(p, q) is False

def test_same_tree_different_values():
    p = build_tree([1,2,1])
    q = build_tree([1,1,2])
    assert Solution().isSameTree(p, q) is False

def test_same_tree_both_empty():
    assert Solution().isSameTree(None, None) is True

def test_same_tree_one_empty():
    p = build_tree([1])
    q = None
    assert Solution().isSameTree(p, q) is False
