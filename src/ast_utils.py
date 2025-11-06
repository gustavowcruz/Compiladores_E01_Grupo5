from dataclasses import is_dataclass, asdict
from typing import Any


def ast_to_dict(node: Any):
    """Convert AST dataclass nodes (and lists) to plain Python dicts/lists for JSON serialization."""
    if node is None:
        return None
    if is_dataclass(node):
        return asdict(node)
    if isinstance(node, list):
        return [ast_to_dict(n) for n in node]
    # primitive (str, int, float, etc.)
    return node
