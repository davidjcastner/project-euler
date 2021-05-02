# Minimal network
# Problem 107
# https://projecteuler.net/problem=107

# The following undirected network consists of seven vertices and twelve edges
# with a total weight of 243.
# The same network can be represented by the matrix below.
#    A  B  C  D  E  F  G
# A  - 16 12 21  -  -  -
# B 16  -  - 17 20  -  -
# C 12  -  - 28  - 31  -
# D 21 17 28  - 18 19 23
# E  - 20  - 18  -  - 11
# F  -  - 31 19  -  - 27
# G  -  -  - 23 11 27  -
# However, it is possible to optimise the network by removing some edges and
# still ensure that all points on the network remain connected. The network
# which achieves the maximum saving is shown below. It has a weight of 93,
# representing a saving of 243  93 = 150 from the original network.


# Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
# containing a network with forty vertices, and given in matrix form, find the
# maximum saving which can be achieved by removing redundant edges whilst
# ensuring that the network remains connected.

from src.lib.utility import read_lines

Network = list[list[int]]
# node index, node weight
Node = tuple[int, int]
Stack = list[Node]


def read_network(data_file: str) -> Network:
    data = read_lines(data_file)
    data = [line.split(',') for line in data]
    data = [[0 if val == '-' else int(val) for val in line] for line in data]
    return data


def insert_stack(stack: Stack, node: Node) -> None:
    '''inserts a node into the stack while keeping it sorted,
    lowest weight is top of stack (highest index)'''
    index = 0
    while index < len(stack) and stack[index][1] > node[1]:
        index += 1
    stack.insert(index, node)


def add_node_weights(network: Network, stack: Stack, node_index: int) -> None:
    '''adds all weights of the node to the stack'''
    for index, weight in enumerate(network[node_index]):
        if weight != 0:
            insert_stack(stack, (index, weight))


def solve(data_file: str = 'd_107.txt') -> str:
    '''Problem 107 - Minimal network'''
    network = read_network(data_file)
    visited = set()
    stack = []

    # initialize weight totals
    # divide total weight by 2 since each edge is represented twice in network
    total_weight = sum((sum(node) for node in network)) // 2
    minimal_weight = 0

    # initialize visited and stack
    visited.add(0)
    add_node_weights(network, stack, 0)
    while len(visited) < len(network):
        [node_index, node_weight] = stack.pop()
        if node_index not in visited:
            visited.add(node_index)
            add_node_weights(network, stack, node_index)
            minimal_weight += node_weight

    return str(total_weight - minimal_weight)


def test_simplified_version() -> None:
    answer = solve(data_file='d_107.basic.txt')
    assert type(answer) == str
    assert answer == '150'


def test_answer() -> None:
    answer = solve()
    assert type(answer) == str
    assert answer == '259679'


if __name__ == '__main__':
    print(solve())
