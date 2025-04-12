

class TreeNode():

    def __init__(self, key, data):
        self.key = key
        self.data  = data
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = None

    def search_recursive(self, key, node):
        if key is node.key:
            return node.data
        elif key > node.key:
            return self.search_recursive(key, node.right)
        elif key < node.key:
            return self.search_recursive(key, node.left)
        return None


    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.search_recursive(key, self.root)
        
    def insert_recursive(self, key, data, node):
        if node is None:
            return TreeNode(key, data)
        elif node.key is key:
            node.data = data
            return node
        elif key < node.key:
            node.left = self.insert_recursive(key, data, node.left)
            return node
        elif key > node.key:
            node.right = self.insert_recursive(key, data, node.right)
            return node
        
    def insert(self, key, data):
        self.root = self.insert_recursive(key, data, self.root)
        
    def delete_recursive(self, key, node):
        if key < node.key:
            node.left = self.delete_recursive(key, node.left)
            return node
        elif key > node.key:
            node.right = self.delete_recursive(key, node.right)
            return node
        elif key is node.key:
            if node.right is None and node.left is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_node = self.__find_min_node(node.right)
            node.key = min_node.key
            node.data = min_node.data
            node.right = self.__delete_rec(node.right, min_node.key)

        return node

    def delete(self, key):
        self.root = self.delete_recursive(key, self.root)
        

    def print_recursive(self, node):
        if node.left is not None:
            self.print_recursive(node.left)
        print(f" {node.key}:{node.data} ", end = ",")
        if node.right is not None:
            self.print_recursive(node.right)
        
    def print(self):
        if self.root is None:
            return None
        else:
            self.print_recursive(self.root)


    def height_count(self, node):
        if node is None:
            return 0
        else:
            leftHeight = self.height_count(node.left)
            rightHeight = self.height_count(node.right)

            if rightHeight > leftHeight:
                return rightHeight + 1
            else:
                return leftHeight + 1

    def height(self):
        return self.height_count(self.root)




    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self.__print_tree(node.left, lvl+5)


def main():  
    bst = BST()
    elements = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for key in elements:
        bst.insert(key, elements[key])
    bst.print_tree()
    bst.print()
    print()
    print(bst.search(24))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height())
    bst.print()
    print()
    bst.print_tree()

main()