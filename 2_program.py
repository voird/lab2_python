#В генеалогическом древе определите для двух элементов их наименьшего общего предка (Lowest Common Ancestor). Наименьшим общим
предком элементов A и B является такой элемент C, что С является предком A,
#C является предком B, при этом глубина C является наибольшей из возможных.
#При этом элемент считается своим собственным предком.

def find_ancestors(node, parent_tree):
    result = []
    result.append(node)
    while node in parent_tree:
        node = parent_tree[node]
        result.append(node)
    return result

parent_tree = dict()
num_nodes = int(input(""))
for i in range(num_nodes - 1):
    child_node, parent_node = input("").split()
    parent_tree[child_node] = parent_node
    
num_queries = int(input(""))
for i in range(num_queries):
    query_node_1, query_node_2 = input("").split()
    ancestors_set_1 = set(find_ancestors(query_node_1, parent_tree))
    for common_ancestor in find_ancestors(query_node_2, parent_tree):
        if common_ancestor in ancestors_set_1:
            print("Общий предок:", common_ancestor)
            break
