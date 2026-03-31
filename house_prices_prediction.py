#=====IMPORT LIBRARIES=====
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,when,count
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression, DecisionTreeRegressor, RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
	data_path= "hdfs://m1:9000/data/house_prices_dataset.csv"
print(f"Data Path:{data_path}")
#=====LOAD DATA FROM HDFS=====
spark = SparkSession.builder.appName("HousePriceML").getOrCreate()
data = spark.read.csv(data_path,header=True,inferSchema=True)
data.show(5)
data.printSchema()
#=====CHECK MISSING VALUES=====
data.select([count(when(col(c).isNull(),c)).alias(c) for c in data.columns]).show()
#=====DATA CLEANING=====
data = data.fillna(0)
#=====FEATURE=====
feature_cols=[c for c in data.columns if c!='Price']
#=====LABEL=======
data = data.withColumn("label",col("Price").cast("double"))
data.show(5)
#=====TRAIN AND TEST SPLIT=====
train_data,test_data=data.randomSplit([0.7,0.3],seed=42)
#=====PIPELINE=====
assembler =VectorAssembler(inputCols=feature_cols,outputCol="features_raw")
scaler =StandardScaler(inputCol="features_raw",outputCol="features")
#=====MODELS======
lr=LinearRegression(featuresCol="features",labelCol="label")
dt = DecisionTreeRegressor(featuresCol="features_raw",labelCol="label",maxDepth=5)
rf=RandomForestRegressor(featuresCol="features_raw",labelCol="label",numTrees=50,maxDepth=5)
#pipelines
pipeline_lr=Pipeline(stages=[assembler,scaler,lr])
pipeline_dt=Pipeline(stages=[assembler,scaler,dt])
pipeline_rf=Pipeline(stages=[assembler,scaler,rf])
#train
model_lr=pipeline_lr.fit(train_data)
model_dt=pipeline_dt.fit(train_data)
model_rf=pipeline_rf.fit(train_data)
#predict
pred_lr=model_lr.transform(test_data)
pred_dt=model_dt.transform(test_data)
pred_rf=model_rf.transform(test_data)
#=====EVALUATION=====
evaluator = RegressionEvaluator(
	labelCol="label",
	predictionCol="prediction",
	metricName="rmse")
rmse_lr = evaluator.evaluate(pred_lr)
rmse_dt = evaluator.evaluate(pred_dt)
rmse_rf = evaluator.evaluate(pred_rf)
print("Linear Regression RMSE:",rmse_lr)
print("Deciosion Tree RMSE:",rmse_dt)
print("Random Forest RMSE:",rmse_rf)
#=====SAVE MODEL=====
model_rf.write().overwrite().save("output/house_rf_model")
#=====FEATURE IMPORTANCE=====
rf_stage= model_rf.stages[-1]
importance= pd.DataFrame({ 
	'Feature': feature_cols,
	'Importance': list(rf_stage.featureImportances.toArray())})
importance=importance.sort_values(by='Importance',ascending=False)
print("\nFeature importance:")
print(importance)
#=====VISUALISATION=====
os.makedirs("output/house",exist_ok=True)
try:
	#heatmap	
	pdf =data.select(feature_cols).limit(100).toPandas()
	plt.figure(figsize=(10,8))
	sns.heatmap(pdf.corr(),cmap="coolwarm")
	plt.title("Correlation Heatmap")
	plt.savefig("output/house/heatmap.png")
	plt.close()
	#prediction and actual
	pred_pd=pred_rf.select("label","prediction").limit(200).toPandas()
	plt.figure()
	plt.scatter(pred_pd["label"],pred_pd["prediction"])
	plt.xlabel("Actual")
	plt.ylabel("Predicted")
	plt.title("Prediction and Actual")
	plt.savefig("output/house/pred_and_actual.png")
	plt.close()
	#feature importance plot
	plt.figure()
	plt.bar(importance['Feature'],importance['Importance'])
	plt.xticks(rotation=90)
	plt.title("Feature Importance")
	plt.tight_layout()
	plt.savefig("output/house/feature_importance.png")
	plt.close()
	print("Visualisation done")
except Exception as e:
	print("Visualisation error:",e)
logging.info("DONE")

