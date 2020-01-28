# HAMILTONIAN CYCLE SOLUTION
from pprint import pprint

class Graph():

	def __init__(self,vertices):
		self.graph=[[0 for col in range(vertices)] for row in range(vertices)]	
		self.V=vertices

	
	def issafe(self,v,pos,path):

	#Check if vertex is an adjacent vertex of the previously added vertex and is not included in the path earlier
		if self.graph[path[pos-1]][v]==0:
			return False

	#Check if vertex is currently in path
		for vertex in path:
			if vertex==v:
				return False

		return True


	# def hamiltonian_cycle_util(self,path,pos):
	# 	if pos==self.V:

g1=Graph(5)
g1.graph=[[0,1,0,1,0], [1, 0, 1, 1, 1],  
             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],  
             [0, 1, 1, 1, 0] ]
pprint(vars(g1))