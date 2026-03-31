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
