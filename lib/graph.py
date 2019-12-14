from typing import List


class GraphNode:
    def __init__(self, name: str, children: List["GraphNode"] = []):
        self.name = name
        self.children = children


class Graph:
    nodes: List["GraphNode"] = []
