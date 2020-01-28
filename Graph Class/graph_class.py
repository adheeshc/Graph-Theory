import numpy as np

class Graph(object):
	def __init__(self,size):
		self.adj_matrix=[]
		for i in range(size):
			self.adj_matrix=np.zeros((size,size))
		self.size=size

	def add_edge(self,v1,v2,d):
		if v1==v2:
			print("already added")
		self.adj_matrix[v1][v2]=d
		self.adj_matrix[v2][v1]=d

	def remove_edge(self,v1,v2,d):
		if self.adj_matrix[v1][v2] == 0:
			print("no edge found")
			return
		self.adj_matrix[v1][v2]=0
		self.adj_matrix[v2][v1]=0

	def contains_edge(self,v1,v2,d):
		if self.adj_matrix[v1][v2]==d: 
			return True 
		else:
			return False

	def __len__(self):
		return self.size

	def toString(self):
		print(self.adj_matrix)

def main():
	g=Graph(5)
	g.toString()


if __name__=="__main__":
	main()
