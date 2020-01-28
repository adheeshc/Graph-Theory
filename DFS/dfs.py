import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
np.set_printoptions(suppress=True)

from graph_class import Graph

def euclid_dist(x1,y1,x2,y2):
	dist=sqrt((x1-x2)**2+(y1-y2)**2)
	return round(dist,3)

def edge_list(nodelist,n):
	nodes=[]
	weights=[]
	for i in range(0,len(nodelist)-1):
		for j in range(i+1,len(nodelist)):
			(x1,y1)=nodelist[i]
			(x2,y2)=nodelist[j]
			nodes.append((int(i),int(j)))
			weights.append(euclid_dist(x1,y1,x2,y2))
	nodes=np.array(nodes)
	weights=np.array(weights).reshape(-1,1)
	final=np.concatenate((nodes,weights),axis=1)	
	return final

def plot_graph(nodelist,start_node):
	for i,txt in enumerate(nodelist):
		plt.scatter(nodelist[i][0],nodelist[i][1])
		#plt.annotate(txt,(nodelist[i][0],nodelist[i][1]))
	plt.annotate(start_node,(nodelist[i][0],nodelist[i][1]))
	plt.show()

def dfs(at):
	if visited[at]: 
		return
	visited[at] = True

	neighbours = g[at]
	for next in neighbours:
		dfs(next)

def main():
	nodelist=[(8,2),(5,9),(4,3),(2,6),(1,7),(9,2),(5,5),(8,3),(11,8),(6,14)]
	n = len(nodelist)
	edges=edge_list(nodelist,n)
	g=Graph(n)
	for i in range(0,edges.shape[0]):
		g.add_edge(int(edges[i][0]),int(edges[i][1]),edges[i][2])
		
	g.toString()	
	start_node=0
	global visited
	visited = [False]*n
	plot_graph(nodelist,start_node)
	#dfs(start_node,g)
	
if __name__=="__main__":
	main()