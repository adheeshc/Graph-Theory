import numpy as np
import random

def graph(num):
	return np.zeros((num,num))
num=6
graph=graph(num)

graph[0,1]=1
graph[0,5]=1

graph[1,0]=1
graph[1,2]=1

graph[2,1]=1
graph[2,3]=1
graph[2,4]=1
graph[2,5]=1

graph[3,2]=1
graph[3,4]=1

graph[4,2]=1
graph[4,3]=1

graph[5,0]=1
graph[5,2]=1

#print(graph)


def check_euler_path(graph,num):
	odd=[]
	#check vertices with odd degree
	for i in range(0,num):
		if (np.sum(graph[i,:]))%2!=0:
			odd.append(i) 
	if len(odd)==0:
		print('Euler circuit possible')
	elif len(odd)==2:
		print('Euler path possible')
	else:
		print('No euler path or circuit exists!')
	return odd

def find_path(graph,num,odd):
	open_list=[]
	for i in range(0,graph.shape[0]):
		for j in range(0,graph.shape[1]):
			if graph[i][j]!=0:
				open_list.append([i,j])	
	
	open_list=np.array(open_list)
	#print(open_list)

	#print(temp)
	#print(open_list)
	u = np.sort(open_list, axis=1)
	_,idx=np.unique(u,axis=0,return_index=True)
	print(open_list[idx])

	
#	print(open_list)


	close_list=[]
	
	#print(start)



odd=check_euler_path(graph,num)
path=find_path(graph,num,odd)