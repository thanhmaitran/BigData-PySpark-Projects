# Big Data ML Pipeline with PySpark & HDFS

## Project Overview

This project implements a **scalable Big Data Machine Learning pipeline** using **Apache Spark (PySpark)** to perform both **classification** and **regression** tasks on datasets stored in **HDFS**.

It demonstrates an end-to-end workflow including data ingestion, preprocessing, model training, evaluation, and visualization in a distributed computing environment.

---

## Architecture

HDFS → Spark (PySpark) → Data Processing → ML Pipeline → Evaluation → Visualization → Output

---

## Key Highlights

* Built scalable machine learning pipelines using **Spark MLlib**
* Processed large datasets directly from **HDFS**
* Implemented both **classification** and **regression** models
* Compared multiple algorithms for performance evaluation
* Performed **feature importance analysis**
* Generated **data visualizations** for insights
* Executed in a distributed VM environment simulating real-world big data systems

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

## Project Structure

```
.
├── diabetes.py
├── house_price.py
├── data/
├── output/
│   ├── diabetes/
│   └── house/
└── README.md
```

---

## Dataset Setup & HDFS Usage Guide

This project uses two datasets:

* `diabetes.csv` → for classification
* `house_prices_dataset.csv` → for regression

---

### Step 1: Start Hadoop Services

```bash
start-all.sh
```

Check running services:

```bash
jps
```

---

### Step 2: Create HDFS Directory

```bash
hdfs dfs -mkdir -p /data
hdfs dfs -ls /
```

---

### Step 3: Upload Datasets

```bash
hdfs dfs -put /home/hdc/Downloads/diabetes.csv /data/
hdfs dfs -put /home/hdc/Downloads/house_prices_dataset.csv /data/
```

---

### Step 4: Verify Upload

```bash
hdfs dfs -ls /data
```

---

### Step 5: Use Data in Spark

```python
data_path = "hdfs://m1:9000/data/diabetes.csv"
```

or

```python
data_path = "hdfs://m1:9000/data/house_prices_dataset.csv"
```

---

### Step 6: Run Spark Jobs

```bash
spark-submit diabetes.py
spark-submit house_price.py
```

Optional:

```bash
spark-submit diabetes.py hdfs://m1:9000/data/diabetes.csv
```

---

### Step 7: Download from HDFS (Optional)

```bash
hdfs dfs -get /data/diabetes.csv /home/hdc/Downloads/
```

---

### Step 8: Remove Files (Optional)

```bash
hdfs dfs -rm /data/diabetes.csv
hdfs dfs -rm -r /data
```

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

This project showcases the ability to build **production-style machine learning pipelines** using distributed computing technologies such as Spark and HDFS.

---

## Key Takeaway

This project demonstrates strong understanding of **Big Data processing**, **machine learning pipelines**, and **scalable system design**, making it applicable to real-world data engineering and machine learning tasks.
