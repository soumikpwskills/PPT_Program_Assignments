class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None



def inOrder(node):
  if (node == None):
		return
        
  inOrder(node.left)
  print(node.data, end=' ')
  inOrder(node.right)


def findIndex(Str, si, ei):
    if (si > ei):
        return -1
        
    s = []
    for i in range(si, ei + 1):
        if (Str[i] == '('):
            s.append(Str[i])
        
        elif (Str[i] == ')'):
            if (s[-1] == '('):
                s.pop(-1)

                if len(s) == 0:
                    return i
    return -1


def treeFromString(Str, si, ei):


    if (si > ei):
	    return None

    root = newNode(ord(Str[si]) - ord('0'))
    index = -1

    if (si + 1 <= ei and Str[si + 1] == '('):
        index = findIndex(Str, si + 1, ei)

    if (index != -1):
        root.left = treeFromString(Str, si + 2, index - 1)
        root.right = treeFromString(Str, index + 2, ei - 1)
    return root


if __name__ == '__main__':
	Str = "4(2(3)(1))(6(5))"
	root = treeFromString(Str, 0, len(Str) - 1)
	inOrder(root)

