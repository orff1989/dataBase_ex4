from pyspark.python.pyspark.shell import sc
from pyspark.sql import SQLContext
from pyspark.sql import Row

# 209163054 - Or Finberg

sqlContext = SQLContext(sc)

########### A #########

df = sqlContext.read.option("multiline","true") \
      .json("books.json").drop(*('country', 'imageLink','language','link','pages'))

t=df.rdd.filter(lambda r: r[0][0]=="F").map(lambda r: Row(r[0],r[1],2022-int(r[2]))).distinct()

columns = ['author','title','past years']
a=sqlContext.createDataFrame(t,columns)

a.printSchema()
a.show()

################ B ############
df2 = sqlContext.read.option("multiline","true") \
      .json("books.json").drop(*('country', 'imageLink','link','title','year'))

t2=df2.rdd.filter(lambda r: r[1]=="English").map(lambda r: (r[0],int(r[2]))).reduceByKey(lambda a,b: a+b).collect()
# t2=df2.rdd.filter(lambda r: r[1]=="English").collect()
a2=sqlContext.createDataFrame(t2,['author', 'pages of english books'])

a2.printSchema()
a2.show(50)
