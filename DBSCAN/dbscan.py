from math import sqrt
import Queue

def dis(x,y):
	return sqrt(pow(x[0]-y[0],2)+pow(x[1]-y[1],2))

def bfs(coreset,dist,num):
	tag=[-1 for i in xrange(num)]
	while len(coreset)!=0:
		corepoint=coreset.pop()
		q=Queue.Queue()
		q.put(corepoint)
		while q.empty() is not True:		#start with this point to do bfs
			temppoint=q.get()
			tag[temppoint]=corepoint
			templist=dist[temppoint]
			for item in templist:			#put all points that around this core point
				if tag[item]==-1:
					q.put(item)
					if item in coreset:		#if the current point is alse core point, remove it because we already classify it
						coreset.remove(item)

	return tag

if __name__ == '__main__':
	r,t=1,4				#radius and thredhold
	n=0
	data={}
	with open('data.txt','r') as f:
		key=0
		for line in f:
			data[key]= tuple(map(float,line.split()))
			key+=1
		num=key			#numbers of data pairs
	# print data[0]
	dist={}

	for i in xrange(num):
		dist[i]=[]   		#all data points whose distance between i and themselves smaller than t
		tempi=data[i]		# a tuple with x and y coordinates
		for j in xrange(num):
			if i != j:
				tempj=data[j]
				tempdis=dis(tempi,tempj)
				if tempdis<r:
					dist[i].append(j)

	coreset=set([])			# find out core points
	for i in xrange(num):
		if len(dist[i])>t:
			coreset.add(i)

	print bfs(coreset, dist, num)
