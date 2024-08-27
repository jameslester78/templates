#allow Jupyter to find the spark installation

import findspark
findspark.init()
findspark.find()

#create a new spark session

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

#returns a hyperlink to access the spark ui
spark


#fetch a table from a sql server rds and load it into a dataframe
def getSqlTable(server,database,table,user,password):  
    
    df = spark.read.format("jdbc").options(
        url=f"jdbc:sqlserver://{server}:{port};database={database};", 
        driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
        dbtable=f'{table}',
        user=user,
        password=password
    ).load()
    
    return df

#create a working table on the rds
def writeWorkingTableToDb(server,port,database,workingTablePrefix,table,dbUser,dbPassword,df):
    
    df.write.format("jdbc") \
          .mode('overwrite') \
          .option("url", f"jdbc:sqlserver://{server}:{port};database={database};") \
          .option("dbtable", f'{workingTablePrefix}{table}') \
          .option("user", dbUser) \
          .option("password", dbPassword) \
          .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
          .save()
    
    return 

#filter and perform an aggregate on a dataframe
df.filter("field1 is NULL").groupBy("field2").agg(sum("field3").alias("alias"))    

#join two dataframes
df1.join(df2, df1.field1 == df2.field2, 'inner').select(df1.field1,df2.field2)

#output dataframe to screen
df.show()   

#read csv to dataframe
spark.read.format("csv").option("header", "true").load('file_Location')


df.withColumn("field1",to_timestamp(col("field2"), 'dd/MM/yyyy')) #convert string to timestamp
df.drop("field1") #drop column from dataframe
df.withColumn("field1",col("field1").cast("integer")) #cast column

