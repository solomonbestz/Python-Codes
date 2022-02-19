class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.l_child = None
        self.r_child = None

    def insert(self, data):
        if self.key == data:
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert(data)
            else:
                self.l_child = BinarySearchTree(data)
        else:
            if self.r_child:
                self.r_child.insert(data)
            else:
                self.r_child = BinarySearchTree(data)

    def search_node(self, node):
        if node == self.key:
            return "Found The Node"
        # Checking if value might be in left sub tree
        if node < self.key:
            if self.l_child:
                return self.l_child.search_node(node), " found the node"
            else:
                return "Node Not Found"
        # Checking if value might be in right sub tree
        if node > self.key:
            if self.r_child:
                return self.r_child.search_node(node), " found the node"
            else:
                return "Node Not Found"

    def in_order_traversal(self):
        element = []

        # Arranging the left child tree in the first
        if self.l_child:
          element += self.l_child.in_order_traversal()

        element.append(self.key)
        # Arranging the right child tree at the end
        if self.r_child:
            element += self.r_child.in_order_traversal()
        return element

def build_tree(my_list):
    tree = BinarySearchTree(my_list[0])

    for n in range(1, len(my_list)):
        tree.insert(my_list[n])
    return tree


if __name__=='__main__':
    my_list = [9, 5, 3, 18, 2, 30, 18, 9, 4]

    tree_nodes = build_tree(my_list)
    print(tree_nodes.in_order_traversal())
  
  