from AbstractTree import AbsBinaryTree


class LinkedBinaryTree(AbsBinaryTree):

    class _BTNode:
        __slots__ = ['_item', '_parent', '_left', '_right']

        def __init__(self, item, parent=None, left=None, right=None):
            self._item = item
            self._parent = parent
            self._left = left
            self._right = right

        def getItem(self):
            return self._item

        def setItem(self, item):
            self._item = item

    __slots__ = ['_root', '_size']

    def __init__(self, item=None, TLeft=None, TRight=None):
        self._root = None
        self._size = 0

        if item is not None:
            root = self.addRoot(item)

            if TLeft is not None:
                if TLeft._root is not None:
                    TLeft._root._parent = root
                    root._left = TLeft._root
                    self._size += TLeft._size
                TLeft._root = None
                TLeft._size = 0

            if TRight is not None:
                if TRight._root is not None:
                    TRight._root._parent = root
                    root._right = TRight._root
                    self._size += TRight._size
                TRight._root = None
                TRight._size = 0

    def root(self):
        return self._root

    def __len__(self):
        return self._size

    def __str__(self):
        def __preorder(pos):
            res = f"[{pos._item} "
            if pos._left is not None:
                res += __preorder(pos._left)
            if pos._right is not None:
                res += __preorder(pos._right)
            res += ']'
            return res

        if self._root is None:
            return '[]'
        return __preorder(self._root)

    def parent(self, pos):
        if pos is None:
            return None
        return pos._parent

    def numChildren(self, pos):
        count = 0
        if pos is None:
            return count
        if pos._left is not None:
            count += 1
        if pos._right is not None:
            count += 1
        return count

    def left(self, pos):
        if pos is None:
            return None
        return pos._left

    def right(self, pos):
        if pos is None:
            return None
        return pos._right

    def addRoot(self, item):
        if self._root is not None:
            raise ValueError("Root already exists!")
        self._root = self._BTNode(item)
        self._size = 1
        return self._root

    def addLeft(self, item, pos):
        if pos is None:
            raise TypeError("Not a valid position.")
        if pos._left is not None:
            raise ValueError("Left child already exists!")
        pos._left = self._BTNode(item, pos)
        self._size += 1
        return pos._left

    def addRight(self, item, pos):
        if pos is None:
            raise TypeError("Not a valid position.")
        if pos._right is not None:
            raise ValueError("Right child already exists!")
        pos._right = self._BTNode(item, pos)
        self._size += 1
        return pos._right

    def replace(self, item, pos):
        if pos is None:
            raise TypeError("Not a valid position.")
        old = pos._item
        pos.setItem(item)
        return old


# Driver code
lbt1 = LinkedBinaryTree(11)
lbt1.addLeft(22, lbt1.root())
lbt1.addRight(33, lbt1.root())
lbt1.addLeft(44, lbt1.root()._left)
lbt1.addRight(55, lbt1.root()._left)
print(lbt1)
