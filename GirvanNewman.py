import networkx as nx

def girvan_newman(G):  #initialize the communities list
    communities = list(nx.connected_components(G))
    while True:
        #get the edge betweenness of all edges in the graph
        edge_betweenness = nx.edge_betweenness_centrality(G)
        #get the edge with the highest betweenness
        max_edge = max(edge_betweenness, key=edge_betweenness.get)
        #remove the edge from the graph
        G.remove_edge(*max_edge)
        #get the connected components of the graph
        subgraphs = list(nx.connected_components(G))
        if len(subgraphs) != len(communities):
            communities = subgraphs
        else:
            #convergence clause
            break
    return communities


