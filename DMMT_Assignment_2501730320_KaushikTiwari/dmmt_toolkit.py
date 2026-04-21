# Data Management Mini Toolkit

# ------- BST IMPLEMENTATION --------
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: No child
            if not node.left and not node.right:
                return None
            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Case 3: Two children
            min_larger = self._min(node.right)
            node.key = min_larger.key
            node.right = self._delete(node.right, min_larger.key)

        return node

    def _min(self, node):
        while node.left:
            node = node.left
        return node


# --------GRAPH IMPLEMENTATION --------
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)

            for neighbor, _ in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []
        self._dfs(start, visited, result)
        return result

    def _dfs(self, node, visited, result):
        visited.add(node)
        result.append(node)

        for neighbor, _ in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, result)


# -------- HASH TABLE IMPLEMENTATION-------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# ----- - MAIN RUNNER --------
def main():
    with open("output.txt", "w") as f:

        def log(text):
            print(text)
            f.write(text + "\n")

        log("===== BST TEST =====")
        bst = BST()

        nums = [50, 30, 70, 20, 40, 60, 80]
        for n in nums:
            bst.insert(n)

        log("Inorder: " + str(bst.inorder()))

        log("Search 20: " + str(bst.search(20)))
        log("Search 90: " + str(bst.search(90)))

        bst.delete(20)
        log("After deleting 20: " + str(bst.inorder()))

        bst.insert(65)
        bst.delete(60)
        log("After deleting 60: " + str(bst.inorder()))

        bst.delete(30)
        log("After deleting 30: " + str(bst.inorder()))

        log("\n===== GRAPH TEST =====")
        g = Graph()

        edges = [
            ('A','B',2), ('A','C',4), ('B','D',7),
            ('B','E',3), ('C','E',1), ('D','F',5),
            ('E','D',2), ('E','F',6), ('C','F',8)
        ]

        for u,v,w in edges:
            g.add_edge(u,v,w)

        log("Adjacency List:")
        for node in g.graph:
            log(f"{node} -> {g.graph[node]}")

        log("BFS from A: " + str(g.bfs('A')))
        log("DFS from A: " + str(g.dfs('A')))

        log("\n===== HASH TABLE TEST =====")
        ht = HashTable(5)

        keys = [10, 15, 20, 7, 12]
        for k in keys:
            ht.insert(k, k*10)

        log("Hash Table:")
        for i, bucket in enumerate(ht.table):
            log(f"{i}: {bucket}")

        log("Get 10: " + str(ht.get(10)))
        log("Get 15: " + str(ht.get(15)))
        log("Get 7: " + str(ht.get(7)))

        ht.delete(15)
        log("After deleting 15:")
        for i, bucket in enumerate(ht.table):
            log(f"{i}: {bucket}")


if __name__ == "__main__":
    main()