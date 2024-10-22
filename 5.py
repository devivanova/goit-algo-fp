import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, visited=[], current_node=None, traversal_type="BFS"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    labels = {node[0]: node[1].get('label', '')
              for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)

    if current_node:
        plt.title(
            f"{traversal_type} Traversal - Visiting Node {current_node.val}")
        plt.text(
            0, -1.5, f"Visited nodes: {[n.val for n in visited]}", fontsize=12, ha='center')
        plt.text(
            0, -1.8, f"Current traversal: {traversal_type}", fontsize=12, ha='center')

    plt.show()


def generate_color_gradient(steps):
    colors = []
    for i in range(steps):
        color_intensity = hex(16 + int((240 / steps) * i))[2:].zfill(2)
        color = f"#{color_intensity}{color_intensity}{
            color_intensity}"
        colors.append(color)
    return colors


def reset_tree_colors(node):
    if node is None:
        return
    node.color = "#000000"
    reset_tree_colors(node.left)
    reset_tree_colors(node.right)


def bfs(root):
    reset_tree_colors(root)

    queue = deque([root])
    visited = []
    steps = 0

    while queue:
        node = queue.popleft()
        visited.append(node)

        colors = generate_color_gradient(len(visited))
        for i, visited_node in enumerate(visited):
            visited_node.color = colors[i]

        draw_tree(root, visited, current_node=node, traversal_type="BFS")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def dfs(root):
    reset_tree_colors(root)

    stack = [root]
    visited = []
    steps = 0

    while stack:
        node = stack.pop()
        visited.append(node)

        colors = generate_color_gradient(len(visited))
        for i, visited_node in enumerate(visited):
            visited_node.color = colors[i]

        draw_tree(root, visited, current_node=node, traversal_type="DFS")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("Обхід у ширину (BFS):")
bfs(root)

print("Обхід у глибину (DFS):")
dfs(root)
