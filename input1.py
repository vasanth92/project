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
count=0
for row in range(total_edge):
	print "press [y/n] "
	input = raw_input()		
	if input=='n':
		break
	elif input=='y':
		print "edges"
		for col in range(2):
			edges[row][col]=raw_input()
		count=count+1

# Graph creation
gr = graph()
G.add_edges_from(edges)
print "Nodes of graph: "
print G.nodes()
print "Edges of graph: "
print G.edges()
nx.draw(G)
plt.savefig("final.png") # save as png
edges=G.edges()
#path creation
#print "total no of edges"
print len(edges)
listlen=(len(edges)-1)*2
list =[[]for i in range(listlen)]
i=0
print "entering instructions for each path"
for i in range(listlen):
	for j in range(1):
		print "starting point"
		r=raw_input()
		list[i].append(r)
		print "instructions"
        	ins=raw_input()
		list[i].append(ins)
		print "ending point"
        	p=raw_input()
		list[i].append(p)

print "length of list after entering instructions"
print len(list)
#for i in range(len(list)):
	#print list[i]
r = 0 
c=2
list1=list
for i in range(len(list)):
	for row in range(len(list)):
		#print "row",row
		#print "initial edge",edges[r][c]
		sublist=[]
		#print sublist
		for col in range(3): 
		#print "col",col
		#print "each edge",edges[row][col]
			if(col==0):
				if(list[r][c]==list[row][col]):
					sublist.append(list[r][c-1])
					sublist.append(list[row][col+1])
					#print sublist
					if(list[r][c-2]!=list[row][col+2]):
						list1.append([list[r][c-2],sublist,list[row][col+2]])
					#sublist=[]
	row=row+1
	r=r+1
print "length of list after finding various paths"
print len(list1)
for i in range(len(list1)):
	print list1[i]
print "enter the starting region to get the desired path"
start=raw_input()
print "enter the ending region"
end=raw_input()
print "the following is/are the path(s)"
for row in range(len(list1)):
	for col in range(1):
		if (list1[row][col]==start) and (list1[row][col+2]==end):
			print list1[row][col+1]
