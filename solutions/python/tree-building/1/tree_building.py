import bisect


class Record:
    """Tree record with ID and parent ID."""

    def __init__(self, record_id: int, parent_id: int) -> None:
        """Create record."""
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Tree node with ID and children."""

    def __init__(self, node_id: int) -> None:
        """Create node."""
        self.node_id: int = node_id
        self.children: list[Node] = []

    def __lt__(self, other: object) -> bool:
        """Sort nodes by ID."""
        if not isinstance(other, Node):
            return NotImplemented
        return self.node_id < other.node_id


def BuildTree(records: list[Record]) -> Node | None:
    """Build tree from records. Return root or None."""
    if not records:
        return None

    num_records = len(records)

    # Pre-create all nodes by their ID for fast lookup
    nodes = [Node(id) for id in range(num_records)]

    for r in records:
        # Parent must have lower ID (except root)
        if r.record_id < r.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        # Root node is its own parent
        if r.record_id == 0:
            continue
        # Only root can have equal record and parent ID
        if r.record_id == r.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        # IDs must be valid
        if r.record_id >= num_records:
            raise ValueError("Record id is invalid or out of order.")
        # Insert child in sorted order
        bisect.insort(nodes[r.parent_id].children, nodes[r.record_id])

    # Return the root node (ID 0) which now has its full tree of children
    return nodes[0]
