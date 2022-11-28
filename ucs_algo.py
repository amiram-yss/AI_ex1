from ways import load_map_from_csv
from queue import PriorityQueue


def ucs(src: int, dst: int):
    # If same junction
    if src == dst:
        return [dst]

    dst_cpy = dst

    # Dataset initialization
    dataset = load_map_from_csv()
    found = False
    # Opened nodes: (min dist from src to point, point index)
    opened = []

    # Just index of CLOSED points
    closed = set()

    fathers = dict()

    opened.append((0, src))

    while len(opened):
        # print(opened)
        (node_dist, node_idx) = opened.pop()
        # If FOUND the target:
        # print("POPPED: ", (node_dist, node_idx))
        if node_idx == dst:
            # print("GACHA!")
            found = True
            break

        # If in CLOSED LIST:
        if node_idx in closed:
            # print(node_idx, " already in closed set.")
            continue
        children = dataset[node_idx].links
        # print(children)
        for itr in children:
            if itr.target not in closed:
                opened.append(((node_dist + itr.distance), itr.target))
                fathers[itr.target] = node_idx
            # opened.append((node_dist + itr.distance, itr.target))
            # print(opened)
        opened.sort(reverse=True)
        closed.add(node_idx)
    pass
    if not found:
        return None
    # print("found")
    atr = []
    ptr = fathers[dst]
    # print(ptr, " ", fathers[ptr])
    # print(fathers)
    ptr = dst
    # print("ptr: ", ptr, ". src: ", src)
    while ptr != src:
        # print(ptr, " -> ", fathers[ptr])
        atr.append(ptr)
        ptr = fathers[ptr]
    atr.append(src)
    atr.reverse()
    # print(atr)
    return atr


'''
        starting_junction = self.dataset[self]

        queue = []
        visited = {}

        queue.append(self)

        while len(queue) != 0:
            current_node = dataset[queue.pop()]
            if current_node.source == dst:
                queue.append(dst)
                break

            for child in current_node.links:
                print(child)
                queue.append(child.target)
'''
