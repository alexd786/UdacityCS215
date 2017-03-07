def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked
    
def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Component containing", node, ": ", mark_component(G, node, marked)
    
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
    
edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h')]
             
G = {}
for x, y in edges:
    make_link(G, x, y)
    
list_component_sizes(G)

def check_connection(G, v1, v2):
    # Return True if v1 is connected to v2 in G
    # or False if otherwise
    marked = {}
    for node in G.keys():
        if node not in marked:
            mark_component(G, node, marked)
        if v1 and v2 in marked:
            return True
        else:
            return False
            
def path(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0 :
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2: distance_from_start[v2}
                open_list.append(neighbor)
    return False
    
# mark_component w/o recursion attempt
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    open_list = [node]
    while len(open_list) > 0 :
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in marked:
                 marked[neighbor] = True
                 total_marked = total_marked + 1 # does this really work?
                 open_list.append(neighbor)
    return total_marked
    
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0] 
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return (sum(distance_from_start.values())+0.0)/len(distance_from_start)
    
def max_distiance(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
   for



