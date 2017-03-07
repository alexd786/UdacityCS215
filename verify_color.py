def verify(G, cert, k):
    current = 0
    neighbor = 0
    for i in G.keys():
        current = cert[i]
        for l in G[i]:
            neighbor = cert[l]
            if neighbor == current:
                return False
    return True
            
    