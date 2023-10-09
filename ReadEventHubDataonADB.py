Insatall package at cluster = com.microsoft.azure:azure-eventhubs-spark_2.12:2.3.21

import pyspark
from pyspark.sql.functions import *
from pyspark.sql import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

##connect with evethub
ehConf = {}
ehConf['eventhubs.connectionString'] = sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt("Endpoint=sb://ehubnamespace2023.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=0/GgIU/SzR6GpRKl/Y/ao9hgF5OUC/LbM+AEhG1hTsM=;EntityPath=ehub")


##read stream data

df_read_stream = (spark.readStream
                 .format("eventhubs")
                 .options(**ehConf)
                 .load())
				 
				 
##preview stream data
%python
bodyDF = df_read_stream.select(col("body").cast("STRING"))

%python
display(bodyDF, streamName= "bodyDF")