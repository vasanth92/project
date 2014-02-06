print "Enter the total number of regions"
tot = int(raw_input())
print "Enter name of each room"
i = 0

room=[]
for i in range(0,tot):
	a=raw_input()
	room.append(a)
#print room
i=0
for i in range(0,tot):
	print 'assume',i+1,'for',room[i]
edge=tot*(tot-1)
i=0
origin=[]
destination=[]
region=[[None]*3]*3
finaledge=[]
for i in range(0,edge):
	print 'enter edge', i+1
	e=i+1
	orig=int(raw_input())
	dest=int(raw_input())
	if (orig==0) and (dest==0) :
		print "no more edges"
		break
	if orig>tot or dest>tot or orig<=0 or dest<=0 :
		print "invalid edge"
		i=i-1
		e=i-1
	origin.append(orig)
	destination.append(dest)
	finaledge.append(e)
	print 'edge starting from',origin[i],'to',destination[i]
	#else:
		#region[orig][dest]=1
print 'total no of edges', i
print 'edge list=',finaledge
print 'origin list=',origin
print 'destination list=',destination
for i in range(0,len(origin)):
	print 'edge starting from', origin[i],'to',destination[i]
