import numpy as np

# 209163054 - Or Finberg

################# 1 ################
print("answer of 1:")
data = np.genfromtxt("prices.txt",delimiter=",")
xy=[]

for i in range(len(data)):
    xy.append([(sum(data[i])-data[i][11])/(len(data[i])-1),data[i][11]])
xy.sort()
xy=np.array(xy)

w=0
b=0
alpha=0.1

for i in range(100):
    gradB=np.mean(1*(xy[:,1]-(w*xy[:,0]+b)))
    gradW = np.mean(xy[:,0]*(xy[:,1]-(w*xy[:,0]+b)))
    b+=alpha*float(gradB)
    w+=alpha*float(gradW)

print(3.42218182*w+b)
print(4.4302*w+b)
print(6.8156*w+b)

################# 2 ################

# mean squared-error: 1/28(36.9+7.647604+37.9+9.802118+29.9+1.4900615)=4.415706554

################# 3 ################

print("answer of 3:")
def h(x,w,b):
    return 1/(1+np.exp(-(np.dot(x,w)+b)))

data = np.genfromtxt("prices.txt",delimiter=",")
x=[]
y=[]
for i in range(len(data)):
    x.append([data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8],data[i][9],data[i][11]])
    y.append(data[i][10])

x = np.array(x)
y = np.array(y)

w=np.array([0.,0,0,0,0,0,0,0,0,0,0])
b=0
alpha=0.001

for i in range(100000):
    gradB = np.mean(1*(y-(h(x,w,b))))
    gradW = np.dot((y-h(x,w,b)),x)*1/len(y)
    b+=alpha*gradB
    w+=alpha*gradW

for i in range(23,len(data)):
    print(h(x[i],w,b))

################# 4 ################

# confusion matrix | classified as positive | classified as negative
# -------------------------------------------------------------------
# really positive  |            2           |          0
# really negative  |            0           |          3

# accuracy = (2+3)/5=1
# recall = 2/2=1
# precision = 2/2=1
# F-Measure = (2*1*1)/(1+1)=1