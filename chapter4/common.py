from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    name: str
    children: List["Node"]


class Tree:
    root: Node


class Graph:
    nodes: List[Node]
