"""
memo:
ハッシュテーブル
データに対して一定のルールに基づく整数値（ハッシュ値）を割り当て、配列形式で保管する方法。
特定のデータにアクセスする際はハッシュ値からデータの存在するアドレスを割り出せるため、O(1)でアクセス可能。

チェイン法
ハッシュテーブルにおいて、ハッシュ値の衝突に対応する方法のひとつ。
ハッシュ値に対応するデータを連結リストにしておき、衝突した時は連結リストに付け加える。
"""

import unittest
from dataclasses import dataclass
from typing import Any, List, Optional


class MyHashTable:
    def __init__(self, size=10):
        self._nodes: List[Optional["MyHashNodeTree"]] = [None for _ in range(size)]

    def __setitem__(self, key, value):
        h = self._get_hash(key)
        node = MyHashTableNode(key=key, value=value)

        if self._nodes[h] is None:
            self._nodes[h] = MyHashNodeTree(head=node)
        else:
            self._nodes[h].add(node)

    def __getitem__(self, key):
        tree = self._nodes[self._get_hash(key)]
        if tree is None:
            raise KeyError()
        return tree.get(key).value

    def delete(self, key):
        h = self._get_hash(key)
        target = self._nodes[h]
        target.delete(key)

    @staticmethod
    def _get_hash(origin: str):
        """
        ハッシュ値を求める。
        ハッシュ値はoriginの各文字のUnicodeポイントを合計した数の下一桁。
        """
        v = sum([ord(char) for char in origin])
        return int(str(v)[-1])


class MyHashNodeTree:
    def __init__(self, head: "MyHashTableNode"):
        self.head = head
        self.tail = head

    def add(self, node: "MyHashTableNode"):
        self.tail.next = node

    def get(self, key):
        pointer = self.head

        while pointer:
            if pointer.key == key:
                return pointer
            else:
                pointer = pointer.next

        raise KeyError()

    def delete(self, key):
        target = self.get(key)

        # 削除対象が先頭の場合
        if self.head == target:
            if self.tail == target:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        # 削除対象が最後尾の場合
        elif self.tail == target:
            self.tail.before = None
        # 削除対象が中間の場合
        elif all([target.before, target.next]):
            target.before.next = target.next
        else:
            # ここにはこないはずなのでエラーを出す
            raise ValueError()


@dataclass()
class MyHashTableNode:
    key: str
    value: Any
    before: "MyHashTableNode" = None
    next: "MyHashTableNode" = None


class TestMyHashTable(unittest.TestCase):
    def test_set(self):
        ht = MyHashTable()
        ht["hoge"] = "fuga"
        assert ht["hoge"] == "fuga"

    def test_key_err(self):
        ht = MyHashTable()
        with self.assertRaises(KeyError):
            assert ht["hoge"]

    def test_delete(self):
        ht = MyHashTable()
        ht["hoge"] = "fuga"
        ht.delete("hoge")
        with self.assertRaises(KeyError):
            assert ht["hoge"]

    def test_collision(self):
        ht = MyHashTable()
        ht["aa"] = "hoge"  # hash(c) == 194
        ht["bbb"] = "fuga"  # hash(e) == 294

        assert ht["aa"] == "hoge"
        assert ht["bbb"] == "fuga"

        tree = ht._nodes[4]

        aa_node = tree.head
        assert aa_node.key == "aa"
        assert aa_node.value == "hoge"

        bbb_node = aa_node.next
        assert bbb_node.key == "bbb"
        assert bbb_node.value == "fuga"


if __name__ == '__main__':
    unittest.main()
