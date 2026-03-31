# BigData-PySpark-Projects
Big Data ML pipelines with PySpark – Diabetes prediction &amp; House price regression
# Big Data Machine Learning Pipeline with Apache Spark

## Project Overview

This project implements a **scalable Big Data Machine Learning pipeline** using **Apache Spark (PySpark)** to perform both **classification** and **regression** tasks on datasets stored in **HDFS**.

It demonstrates an end-to-end workflow including data ingestion, preprocessing, model training, evaluation, and visualization in a distributed computing environment.

---

## Key Highlights

* Built scalable machine learning pipelines using **Spark MLlib**
* Processed large datasets directly from **HDFS**
* Implemented both **classification** and **regression** models
* Compared multiple algorithms for performance evaluation
* Performed **feature importance analysis**
* Generated **data visualizations** for insights
* Executed in a **virtual machine (VM) environment** simulating real-world big data systems

---

## Tech Stack

* **Apache Spark (PySpark)**
* **Hadoop Distributed File System (HDFS)**
* **Python**
* **Spark MLlib**
* **Matplotlib & Seaborn**

---

## Use Cases

### 1. Diabetes Prediction (Classification)

* Predict whether a patient has diabetes based on medical features
* Models used:

  * Decision Tree Classifier
  * Random Forest Classifier

### 2. House Price Prediction (Regression)

* Predict house prices based on input features
* Models used:

  * Linear Regression
  * Decision Tree Regressor
  * Random Forest Regressor

---

## Workflow Summary

1. Load data from HDFS
2. Perform data cleaning and preprocessing
3. Create feature vectors and labels
4. Build ML pipelines using Spark
5. Train multiple models
6. Evaluate model performance
7. Extract feature importance
8. Generate and save visualizations
9. Save trained models

---

## Output

* Model performance metrics (Accuracy / RMSE)
* Feature importance tables
* Visualization images:

  * Distribution plots
  * Correlation heatmaps
  * Prediction vs actual plots
* Saved trained models

---

## Purpose

This project showcases how to build a **production-style machine learning pipeline** for big data using distributed computing tools, making it suitable for real-world applications in data engineering and machine learning.
======================================================================================================================================================================
## Dataset Setup & HDFS Usage Guide

This project uses two datasets:

* `diabetes.csv` → for classification
* `house_prices_dataset.csv` → for regression

Below is a step-by-step guide to upload and use these datasets with **HDFS** in a VM environment.

---

## ⚙️ Step 1: Start Hadoop Services

Before interacting with HDFS, start all Hadoop services:

```bash
start-all.sh
```

Check if services are running:

```bash
jps
```

You should see processes like:

* NameNode
* DataNode
* SecondaryNameNode

---

## Step 2: Create HDFS Directory

Create a directory in HDFS to store datasets:

```bash
hdfs dfs -mkdir -p /data
```

Verify:

```bash
hdfs dfs -ls /
```

---

## Step 3: Upload Datasets to HDFS

Assuming your datasets are in your local VM path (e.g. `/home/hdc/Downloads`):

```bash
hdfs dfs -put /home/hdc/Downloads/diabetes.csv /data/
hdfs dfs -put /home/hdc/Downloads/house_prices_dataset.csv /data/
```

---

## Step 4: Verify Upload

List files in HDFS:

```bash
hdfs dfs -ls /data
```

You should see:

```bash
diabetes.csv
house_prices_dataset.csv
```

---

## Step 5: Read Data in Spark

Use HDFS path inside your PySpark scripts:

```python
data_path = "hdfs://m1:9000/data/diabetes.csv"
```

or:

```python
data_path = "hdfs://m1:9000/data/house_prices_dataset.csv"
```

---

## Step 6: Run Your Spark Jobs

Run your scripts with:

```bash
spark-submit diabetes.py
```

or:

```bash
spark-submit house_price.py
```

You can also pass the dataset path manually:

```bash
spark-submit diabetes.py hdfs://m1:9000/data/diabetes.csv
```

---

## Step 7: Download Data from HDFS (Optional)

To copy data from HDFS back to local:

```bash
hdfs dfs -get /data/diabetes.csv /home/hdc/Downloads/
```

---

## Step 8: Remove Files (Optional)

Delete files in HDFS:

```bash
hdfs dfs -rm /data/diabetes.csv
```

Delete entire folder:

```bash
hdfs dfs -rm -r /data
```

---

## Notes

* Ensure Hadoop services are running before any HDFS command
* Always verify file paths using `hdfs dfs -ls`
* Use correct HDFS URI (`hdfs://m1:9000/`) in Spark scripts
* Large datasets should always be processed via HDFS instead of local storage

---

This setup simulates a real-world **Big Data pipeline**, where data is stored in distributed storage (HDFS) and processed using Spark.

