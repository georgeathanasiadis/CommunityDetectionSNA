import random

def walktrap(G, steps=500):
    H = G.copy()
    communities = []
    proximity_profiles = {}
    visited = []
    for node in H.nodes():
        #set the current node as the starting point of the random walk
        walk = [node]
        #perform the random walk for the specified number of steps
        for i in range(steps):
            walk.append(random.choice(list(H.neighbors(walk[-1]))))
        walk_nodes = set(walk)
        #add the set of nodes visited during the random walk to the proximity profile
        proximity_profiles[node] = walk_nodes
    for node in H.nodes():
        #check if the node is already assigned to a community
        if node not in visited:
            community = set([node])
            visited.append(node)
            #iterate over the nodes of the graph
            for other_node in H.nodes():
                if other_node in proximity_profiles[node]:
                    community.add(other_node)
                    visited.append(other_node)
            #check if the community of the current node is already in the communities list
            if any(community.issubset(c) for c in communities):
                #if yes, add the current node to the existing community
                for idx,c in enumerate(communities):
                    if community.issubset(c):
                        communities[idx] = c.union(community)
            else:
                #if not, add the community of the current node to the communities list
                communities.append(community)
    return communities

