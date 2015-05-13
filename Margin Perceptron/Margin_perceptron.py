import math

# T = lambda: map(int, raw_input().split())

def find_max_R(M,n,d):
	l=[]
	for i in range(n):
		temp=0
		for j in range(d):
			temp+=M[i][j]**2
		l.append(math.sqrt(float(temp)))
	return max(l)

def regular_perceptron(M,n,d):
	c=[0 for i in range(d)]
	flag=False
	while not flag:
		# flag=True
		# print 1
		for i in range(n):
			temp=0
			for j in range(d):
				temp+=c[j]*M[i][j]
			if M[i][d]==0 and temp<=0:
				for k in range(d):
					c[k]+=M[i][k]
				flag=False
				break
			elif M[i][d]==1 and temp>=0:
				for k in range(d):
					c[k]-=M[i][k]
				flag=False
				break
			else:
				flag=True
	return c

def distance(c):
	temp=0
	for i in range(len(c)):
		temp+=math.pow(c[i],2.0)
	return math.sqrt(temp)

def margin_of_p(p):
	tmp=0
	for i in range(d):
		tmp+=(p[i]/float(p[d]))**2
	y=1/math.sqrt(tmp)
	return y

def Margin_Perceptron(M,n,d,y,R):
	c=[0 for i in range(d)]
	flag=False
	Flag=False
	threshold=1+12*(math.pow(R,2))/(math.pow(y,2))
	# print threshold
	count=0
	while not flag:
		# flag=True
		if count>threshold:
			Flag=True				#see if this gonna run forever, if so break and return
			break
		for i in range(n):
			temp=0
			for j in range(d):
				temp+=c[j]*M[i][j]
			if M[i][d]==0 and temp<=0 or distance(c)<=y/2.0:
				for k in range(d):
					c[k]+=M[i][k]
				flag=False
				break
			elif M[i][d]==1 and temp>=0 or distance(c)<=y/2.0:
				for k in range(d):
					c[k]-=M[i][k]
				flag=False
				break
			else:
				flag=True
		count+=1

	return c,Flag

def Incremental_Algorithm(M,n,d,R,p):
	y=margin_of_p(p)
	# print R,y
	while True:
		y=4*y
		c,Flag=Margin_Perceptron(M, n, d, y, R)
		# print c
		if Flag:
			return p
		p=c

if __name__ == '__main__':
	f=open('data.txt','r')				#input file name
	n,d=map(int,f.readline().split())
	F=f.readlines()
	f.close()
	M = [[0 for i in range(d+1)]for i in range(n)]
	M_1= [[0 for i in range(d+2)]for i in range(n)]
	for i in range(len(F)):
		M[i]=map(float,F[i].split())
		for j in range(d):
			M_1[i][j]=M[i][j]
		M_1[i][d]=1
		M_1[i][d+1]=M[i][d]

	p=regular_perceptron(M_1,n,d+1)     #x1c1+x2c2+x3c3+.....1*cd+1=0
	R=find_max_R(M_1, n, d+1)
	ans=Incremental_Algorithm(M_1, n, d+1, R, p)
	print ans,margin_of_p(ans)
