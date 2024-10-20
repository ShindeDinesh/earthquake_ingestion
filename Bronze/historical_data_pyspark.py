from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.master('local[*]').appName('asd').getOrCreate()

    file=spark.read.csv(r'C:\Users\Win10\Downloads\salespeoples.csv')

    file.show()