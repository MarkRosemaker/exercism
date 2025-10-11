from typing import Iterable


class EmptyListException(Exception):
    """Raised when accessing elements of an empty linked list."""

    pass


class Node:
    """Node in a singly linked list."""

    def __init__(self, value: int, next: "Node | None" = None):
        """Create node with given value."""
        self._value = value
        self._next = next

    def value(self) -> int:
        """Get value of node."""
        return self._value

    def next(self) -> "Node | None":
        """Get next node or None."""
        return self._next


class LinkedList:
    """Singly linked list supporting push, pop, and reverse."""

    def __init__(self, values: Iterable[int] = []) -> None:
        """Initialize list with optional values."""
        self._head: Node | None = None
        for value in values:
            self.push(value)

    def __iter__(self):
        """Iterate over node values from head to tail."""
        n = self._head
        while n:
            yield n.value()
            n = n.next()

    def __len__(self) -> int:
        """Return number of nodes in list."""
        return sum(1 for _ in self)

    def head(self) -> Node:
        """Return head node; raise if empty."""
        if not self._head:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: int):
        """Insert value at head."""
        self._head = Node(value, self._head)

    def pop(self) -> int:
        """Remove and return head value; raise if empty."""
        if not self._head:
            raise EmptyListException("The list is empty.")
        val = self._head.value()
        self._head = self._head.next()
        return val

    def reversed(self) -> "LinkedList":
        """Return a reversed list."""
        prev, cur = None, self._head
        while cur:
            prev, cur = Node(cur.value(), prev), cur.next()
        self._head = prev  # New head is previous tail
        return self
