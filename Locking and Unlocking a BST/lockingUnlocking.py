'''
# A node can either be locked or unlocked if all of its ancestors or descendents are not locked
class Node:
    def __init__(self, value, parent):
        self.data = value
        self.left = None
        self.right = None
        self.parent = None
        self.isLocked = False
        self.lockedDescendantsCount = 0
        
    def lock_or_unlock(self):
        # to be locked or unlocked, all of its ancestors or descendents must be not locked, 
        # so the count must be 0
        if self.lockedDescendantsCount > 0:
            return False
        
        current = self.parent
        while current:
            if current.isLocked:
                return False
            current = current.parent
        
        return True
    
    # Returns the current status of the isLocked status
    def is_locked(self):
        return self.isLocked
    
    # Attempts to lock the node, if it cannot be locked it will return false.
    # If it can be locked, it will lock it return True
    def lock(self):
        if self.lock_or_unlock():
            # it is not locked and increment the count to all of its ancestors
            self.isLocked = True
            
            current = self.parent
            while current:
                self.lockedDescendantsCount += 1
                current = current.parent
            return True
        else:
            return False
        
    # Attempts to unlock the node, if it cannot be unlocked it will return false. 
    # Otherwise, it will be unlocked, and it will return True
    def unlock(self):
        if self.lock_or_unlock():
            # it is currently locked, we must unlock it, and update the count to all of its ancestors
            self.isLocked = False
            
            current = self.parent
            while current:
                current.lockedDescendentsCount -= 1
                current = current.parent
            return True
        else:
            return False     

a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

print(b.lock())
print(b.is_locked())
print(c.lock())
print(b.unlock())
print(not b.is_locked())
print(d.lock())
print(not g.lock())
print(c.unlock())
print(g.lock())
print(f.lock())
print(e.lock())
print(a.locked_descendants_count)
print(b.locked_descendants_count)
print(c.locked_descendants_count)
'''

def is_parent_locked(node):
    # No parent, there is no parent that is locked
    if not node.parent:
        return False
    # if the parent is locked return true 
    elif node.parent.locked:
        return True
    # if not at the parent, recursively call until we reach the parent
    return is_parent_locked(node.parent)

# Method updates all the parent nodes with appropriate locked descendants counts
def update_parent(node, enable_locks):
    if enable_locks:
        increment = 1
    else: 
        increment = -1
    if node.parent:
        node.parent.locked_descendants += increment
        update_parent(node.parent, enable_locks)


class Node:
    def __init__(self, val, parent):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
        self.locked = False
        self.locked_descendants = 0

    def lock(self):
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = True
            update_parent(node=self, enable_locks=True)
            return True

    def unlock(self):
        if is_parent_locked(self) or self.locked_descendants:
            return False
        else:
            self.locked = False
            update_parent(node=self, enable_locks=False)
            return True

    def is_locked(self):
        return self.locked


a = Node("a", None)
b = Node("b", a)
c = Node("c", a)
d = Node("d", b)
e = Node("e", b)
f = Node("f", c)
g = Node("g", c)

print(b.lock())
print(b.is_locked())
print(c.lock())
print(b.unlock())
print(not b.is_locked())
print(d.lock())
print(not g.lock())
print(c.unlock())
print(g.lock())
print(f.lock())
print(e.lock())
print(a.locked_descendants)
print(b.locked_descendants)
print(c.locked_descendants)


