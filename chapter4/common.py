from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    name: str
    children = []


class Tree:
    root: Node = None


class Graph:
    nodes: List[Node] = []
