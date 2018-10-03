# BFS
# breadth first search

# Breadth-first search (BFS) is a method for exploring a tree or graph. 
# In a BFS, you first explore all the nodes one step away, 
# then all the nodes two steps away, etc.


tree = (5, (6, (7,None, None,),(1,None,None,),),(2,(4,None,None,),(2,None,None,),),)

# node -> (value, left child, right child)
def print_tree(node):
	queue = []
	queue.append(node)
	while len(queue) > 0:
		first_elem = queue.pop(0)
		value, left, right = first_elem
		print (value)
		if left is not None:
			queue.append(left)
		if right is not None:
			queue.append(right)


print_tree(tree)

def is_balanced(tree_root):
	depths = set() #if there are more than 2 depths, the tree is not balanced
	nodes = [] #store nodes and depth 
	nodes.append(tree_root)
	while len(queue) > 0:
		node, depth = nodes.pop(0)
		#found leaf
		if node.left is None and node.right is None:
			depths.add(depth)
			if (len(depths) > 2) or ((max(depths)-min(depths)) > 1):
				return False

		#not a leaf
		else:
			if node.left in not None:
				nodes.append((node.left, depth + 1))
			if node.left in not None:
				nodes.append((node.right, depth + 1))
	
	return True