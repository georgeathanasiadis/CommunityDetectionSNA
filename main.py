import os
import pickle
from os import listdir
from os.path import isfile, join
from GirvanNewman import girvan_newman
from LabelPropogation import label_propagation
from Walktrap import walktrap
from Louvain import fast_greedy


mypath = os.getcwd() + '\\twitter_data_SNA\\day_graphs'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

H = pickle.load(open('twitter_data_SNA/node_attributes', 'rb'))

all_graphs = []
mydir = 'twitter_data_SNA/day_graphs/'
for i in onlyfiles:
    G1 = pickle.load(open(mydir + i, 'rb'))
    all_graphs.append(G1)

G_example = pickle.load(open('twitter_data_SNA/day_graphs/Graph_59', 'rb')) #indicative example

print("Walktrap:")
result = walktrap(G_example, steps = 700)
print(result)
print("No. of communities: ", len(result))

print("Girvan-Newman:")
result = girvan_newman(G_example)
print(result)
print("No. of communities: ", len(result))

print("Label Propogation:")
result = label_propagation(G_example)
print(result)
print("No. of communities: ", len(result))
