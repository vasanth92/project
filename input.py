import sys
sys.path.append('/usr/lib/graphviz/python/')    # 32-bits
sys.path.append('/usr/lib64/graphviz/python/')
sys.path.append('/usr/lib/pyshared/python2.7')
import gv

# Import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.readwrite.dot import write

import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
print "Enter the total number of regions"
tot = int(raw_input())
print "Enter name of each room"
i = 0

room=[]
for i in range(0,tot):
	a=raw_input()
	room.append(a)
#print room
print "Regions are..."
i=0
for i in range(0,tot):
	print i+1,':',room[i]
total_edge=tot*(tot-1)

i=0
edges=[[0 for col in range(2)] for row in range(total_edge)]
finaledge=[]
for row in range(total_edge):
	print "press [y/n] "
	input = raw_input()		
	if input=='n':
		break
	elif input=='y':
		print "edges"
		for col in range(2):
			edges[row][col]=raw_input()

# Graph creation
gr = graph()
G.add_edges_from(edges)
print "Nodes of graph: "
print G.nodes()
print "Edges of graph: "
print G.edges()
nx.draw(G)
plt.savefig("simple_path.png") # save as png

	
