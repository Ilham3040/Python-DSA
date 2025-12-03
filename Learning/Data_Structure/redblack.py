from collections import deque

class Node:
    def __init__(self,value,color="red"):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None
        self.color = color
        self.parent: Node | None = None
        
    def grandparent(self) -> 'Node | None' :
        if self.parent is None:
            return None
        
        return self.parent.parent
    
    def sibling(self) -> 'Node | None' :
        if self.parent is None:
            return None
        
        if self == self.parent.left:
            return self.parent.right
        
        return self.parent.left
    
    def uncle(self) -> 'Node | None' :
        if self.parent is None:
            return None
        
        return self.parent.sibling()
    
   
        
class RedBlack:
    
    def __init__(self):
        self.root = None
        self.NIL = Node(value=None)
        self.NIL.color = "black"
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL

        
    def search(self,value):
        
        current = self.root
        
        while current is not self.NIL:
            
            if value == current.value:
                return current
            
            elif value < current.value:
                current = current.left
                
            elif value > current.value:
                current = current.right
                
        return None
        
        
    def insertion(self,value):
        
        newNode = Node(value)
        newNode.left = self.NIL
        newNode.right = self.NIL
        
        if self.root == None:
            self.root = newNode
            
        else:
            current = self.root
            
            while current is not self.NIL:
                
                if newNode.value < current.value:
                    
                    if current.left is self.NIL:
                        current.left = newNode
                        newNode.parent = current
                        break
                    
                    else:
                        current = current.left
                        
                if newNode.value > current.value:
                    
                    if current.right is self.NIL:
                        current.right = newNode
                        newNode.parent = current
                        break
                    
                    else:
                        current = current.right
                        
                if newNode.value == current.value:
                    print("Value is already here")
                    return current
        
        self.fixInsertion(newNode)
                        
    def fixInsertion(self, node: Node):
        
        while node.parent and node.parent.color == "red":
            
            if node.parent == node.grandparent().left:
                
                uncle = node.uncle()
                
                if uncle and uncle.color == "red":
                    
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.grandparent().color = "red"
                    node = node.grandparent()
                    
                else :
                    
                    if node == node.parent.right:
                        node = node.parent
                        self.rotateLeft(node)
                        
                    node.parent.color = "black"
                    node.grandparent().color = "red"
                    self.rotateRight(node.grandparent())
            
            if node.parent == node.grandparent().right:
                
                uncle = node.uncle()
                
                if uncle and uncle.color == "red":
                    
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.grandparent().color = "red"
                    node = node.grandparent()
                    
                else :
                    if node == node.parent.left:
                        
                        node = node.parent
                        self.rotateRight(node)
                        
                    node.parent.color = "black"
                    node.grandparent().color = "red"
                    self.rotateLeft(node.grandparent())
                    
        self.root.color = "black"
        
    
    def delete(self, value):
        node_to_remove = self.search(value)
        if node_to_remove is None:
            return

        removed_color = node_to_remove.color

        if node_to_remove.left is self.NIL or node_to_remove.right is self.NIL:
            x = node_to_remove.left if node_to_remove.left is not self.NIL else node_to_remove.right
            self._replace_node(node_to_remove, x)
            
        else:
            successor = self._find_min(node_to_remove.right)
            node_to_remove.value = successor.value
            removed_color = successor.color        
            x = successor.right                    
            self._replace_node(successor, successor.right)

        if removed_color == "black":
            self.fix_delete(x)


            
    def fix_delete(self,node: Node):
        
        while node != self.root and node.color == "black":

            if node == node.parent.left:
            
                sibling = node.sibling()
                
                if sibling.color == "red":
                    
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotateLeft(node.parent)
                    sibling = node.sibling()
                
                if (sibling.left is None or sibling.left.color == "black") and (sibling.right is None or sibling.right.color == "black"):
                           
                    sibling.color = "red"
                    node = node.parent
                    
                else:
                    
                    if sibling.right is None or sibling.right.color == "black":
                        
                        sibling.left.color = "black"
                        sibling.color = "red"
                        
                        self.rotateRight(sibling)
                        sibling = node.sibling()
                        
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    
                    if sibling.right:
                        sibling.right.color = "black"
                        
                    self.rotateLeft(node.parent)
                    node = self.root
                    
            else:

                sibling = node.sibling()
                
                if sibling.color == "red":
                    
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotateRight(node.parent)
                    sibling = node.sibling()
                
                if (sibling.left is None or sibling.left.color == "black") and (sibling.right is None or sibling.right.color == "black"):
                           
                    sibling.color = "red"
                    node = node.parent
                    
                else:
                    
                    if sibling.left is None or sibling.left.color == "black":
                        
                        sibling.right.color = "black"
                        sibling.color = "red"
                        
                        self.rotateLeft(sibling)
                        sibling = node.sibling()
                        
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    
                    if sibling.left:
                        sibling.left.color = "black"
                        
                    self.rotateRight(node.parent)
                    node = self.root
                    
        node.color = "black"
        
    def _find_min(self, node: Node):
        
        while node.left is not self.NIL:
            node = node.left
            
        return node
    
    def _replace_node(self,old_node: Node,new_node: Node):
        
        if old_node.parent is None:
            self.root = new_node
            
        else:
            
            if old_node == old_node.parent.left:
                old_node.parent.left = new_node
            
            elif old_node == old_node.parent.right:
                old_node.parent.right = new_node
                
        new_node.parent = old_node.parent 
        
                        
    
    def rotateLeft(self,node: Node):
        
        right_child = node.right
        node.right = right_child.left
        
        if right_child.left is not self.NIL:
            right_child.left.parent = node
            
        right_child.parent = node.parent
        
        if node.parent is None:
            self.root = right_child
            
        elif node == node.parent.left:
            node.parent.left = right_child
            
        elif node == node.parent.right:
            node.parent.right = right_child
            
        right_child.left = node
        node.parent = right_child
        
        
    def rotateRight(self,node: Node):
        
        left_child = node.left
        node.left = left_child.right
        
        if left_child.right is not self.NIL:
            left_child.right.parent = node
            
        left_child.parent = node.parent
        
        if node.parent is None:
            self.root = left_child
            
        elif node == node.parent.right:
            node.parent.right = left_child   
            
        elif node == node.parent.left:
            node.parent.left = left_child
            
        left_child.right = node
        node.parent = left_child
        
        
    def printing(self):
        
        queue = deque()
        queue.append([self.root,1])
        
        while queue:
            
            current = queue.popleft()
            print(current[0].value, current[0].color,current[1])
            if current[0].left is not self.NIL:
                queue.append([current[0].left,current[1]+1])
            if current[0].right is not self.NIL:
                queue.append([current[0].right,current[1]+1])
        
        
if __name__ == "__main__":
    
    tree = RedBlack()
    
    for i in range(1,11):
        tree.insertion(i)
    
    tree.printing()
    
    tree.delete(2)
    tree.printing()
    
    tree.delete(4)
    tree.printing()
    
    

    
    
    