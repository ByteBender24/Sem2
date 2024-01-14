from abc import ABC, abstractmethod
# from LinkedQueue import LinkedQueue

class AbstractTree(ABC):
    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self, pos):
        pass

    @abstractmethod
    def numChildren(self, pos):
        pass

    @abstractmethod
    def children(self, pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def isRoot(self, pos):
        return (pos == self.root())

    def isLeaf(self, pos):
        return (self.numChildren(pos) == 0)

    def isEmpty(self):
        return (len(self) == 0)

    def depthN(self, pos):
        if self.isRoot(pos):
            return 0
        return 1 + self.depth(self.parent(pos))

    def _heightN(self, pos):
        if self.isLeaf(pos):
            return 0
        return 1 + max(self._heightN(child) for child in self.children(pos))

    def height(self, pos=None):
        if pos is None:
            if self.isEmpty():
                return -1
            pos = self.root()
        return self._heightN(pos)

    def __iter__(self):
        for pos in self.positions():
            yield pos.getItem()

    def positions(self):
        return self.preorder()

    def preorder(self):
        if not self.isEmpty():
            for pos in self._preorderSubTree(self.root()):
                yield pos

    def _preorderSubTree(self, pos):
        yield pos
        for child in self.children(pos):
            for p in self._preorderSubTree(child):
                yield p

    def postorder(self):
        if not self.isEmpty():
            for pos in self._postorderSubTree(self.root()):
                yield pos

    def _postorderSubTree(self, pos):
        for child in self.children(pos):
            for p in self._preorderSubTree(child):
                yield p
        yield pos

    # def breadthFirst(self):
    #     if not self.isEmpty():
    #         fringe = LinkedQueue()
    #         fringe.enqueue(self.root())
    #         while not fringe.isEmpty():
    #             pos = fringe.dequeue()
    #             yield pos
    #             for child in self.children(pos):
    #                 fringe.enqueue(child)

class AbsBinaryTree(AbstractTree):
    @abstractmethod
    def left(self, pos):
        if self.left(pos) is not None:
            yield self.left(pos)

    @abstractmethod
    def right(self, pos):
        if self.right(pos) is not None:
            yield self.right(pos)

    def children(self, pos):
        if self.left(pos) is not None:
            yield self.left(pos)
        if self.right(pos) is not None:
            yield self.right(pos)

    def sibling(self, pos):
        parent = self.parent(pos)
        if parent is None:
            return None
        if pos == self.left(parent):
            return self.right(parent)
        return self.left(parent)
