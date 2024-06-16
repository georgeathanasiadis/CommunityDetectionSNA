def label_propagation(G):
    for i, node in enumerate(G.nodes()):
        G.nodes[node]['label'] = i

    G_previous = G.copy()

    #repeat until convergence between G & G_previous
    while True:
        #loop: update its label to the mode of its neighbor's labels
        for node in G.nodes():
            labels = [G.nodes[neighbor]['label'] for neighbor in G.neighbors(node)]
            G.nodes[node]['label'] = max(set(labels), key=labels.count)

        #check if the labels have changed from G_previous; if they haven't, the algorithm is done
        if G_previous.nodes(data='label') == G.nodes(data='label'):
            break

        G_previous = G.copy()

    #group nodes into communities based on their labels
    communities = {}
    for node, label in G.nodes(data='label'):
        if label not in communities:
            communities[label] = [] #new label appearance; add new community
        communities[label].append(node)

    return communities




