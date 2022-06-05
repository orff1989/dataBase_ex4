from pyspark.python.pyspark.shell import sc
from pyspark.sql import SQLContext
from pyspark.sql import Row

sqlContext = SQLContext(sc)

df = sqlContext.read.option("multiline","true") \
      .json("books.json").drop(*('country', 'imageLink','language','link','pages'))


t=df.rdd.filter(lambda r: r[0][0]=="F").map(lambda r: Row(r[0],r[1],2022-int(r[2]))).distinct()

columns = ['author','title','past years']
a=sqlContext.createDataFrame(t,columns)

a.printSchema()
a.show()


