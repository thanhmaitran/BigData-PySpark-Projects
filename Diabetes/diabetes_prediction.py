#=====IMPORT LIBRARIES=====
from pyspark.sql.functions import col,when,count
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import DecisionTreeClassifier, RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
import logging
logging.basicConfig(level=logging.INFO)
import matplotlib
matplotlib.use('Agg')
import sys
try:
	data_path=sys.argv[1]
except IndexError:
	print("No input path provided. using defaults dataset")
	data_path= "hdfs://m1:9000/data/diabetes.csv"
print(f"Data Path:{data_path}")
#=====SPARK SESSION=====
spark = SparkSession.builder.appName("DiabetesMLib").getOrCreate()
#=====LOAD DATA FROM HDFS=====
data = spark.read.csv(data_path,header=True,inferSchema=True)
data.show(5)
data.printSchema()
#=====CHECK MISSING VALUES=====
data.select([count(when(col(c).isNull(),c)).alias(c) for c in data.columns]).show()
#=====DATA CLEANING=====
cols_with_invalid_zero=["Glucose","BloodPressure","BMI"]
for c in cols_with_invalid_zero:
	data = data.withColumn(c,when(col(c)==0,None).otherwise(col(c)))
for c in cols_with_invalid_zero:
	mean_val=data.selectExpr(f"avg({c})").first()[0]
	data=data.na.fill({c:mean_val})
#=====FEATURE=====
feature_cols=[c for c in data.columns if c!='Outcome']
#=====LABEL=======
data = data.withColumn("label",col("Outcome").cast("double"))
data.show(5)
#=====FEATURE VECTOR=====
feature_cols =[c for c in data.columns if c!= 'Output']
#=====TRAIN AND TEST SPLIT=====
train_data,test_data=data.randomSplit([0.7,0.3],seed=42)
#=====PIPELINE=====
assembler =VectorAssembler(inputCols=feature_cols,outputCol="features_raw")
scaler =StandardScaler(inputCol="features_raw",outputCol="features")
#=====DECISION TREE CLASSIFIER=====
dt = DecisionTreeClassifier(labelCol="label",featuresCol="features",maxDepth=5)
pipeline_dt=Pipeline(stages=[assembler,scaler,dt])
dt_model=pipeline_dt.fit(train_data)
dt_pred=dt_model.transform(test_data)
#=====RANDOM FOREST CLASSIFIER=====
rf=RandomForestClassifier(labelCol="label",featuresCol="features",numTrees=50,maxDepth=5)
pipeline_rf=Pipeline(stages=[assembler,scaler,rf])
rf_model = pipeline_rf.fit(train_data)
rf_pred = rf_model.transform(test_data)
#=====EVALUATION=====
evaluator = MulticlassClassificationEvaluator(labelCol="label",predictionCol="prediction",metricName="accuracy")
dt_acc = evaluator.evaluate(dt_pred)
rf_acc = evaluator.evaluate(rf_pred)
results=pd.DataFrame({
	"Model":["Decision Tree","Random Forest"],
	"Accuracy":[dt_acc,rf_acc]})
print(results)
#=====FEATURE IMPORTANCE=====
rf_stage=rf_model.stages[-1]
importance= pd.DataFrame({ 
	'Feature': feature_cols,
	'Importance': list(rf_stage.featureImportances.toArray())})
importance=importance.sort_values(by='Importance',ascending=False)
print("\nFeature importance (random forest):")
print(importance)
#=====VISUALIZATION=====
os.makedirs("output/diabetes",exist_ok=True)
pdf =data.sample(0.2).toPandas()
#histogram
pdf['Glucose'].hist()
plt.title("Glucose Distribution")
plt.savefig("output/diabetes/glucose_hist.png")
plt.clf()
#correlation heatmap
sns.heatmap(pdf.corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("output/diabetes/heatmap.png")
plt.clf()
#feature importance plot
importance.plot(kind='bar',x='Feature',y='Importance')
plt.title("Feature Importance")
plt.savefig("output/diabetes/feature_importance.png")
plt.clf()
logging.info("DONE")
