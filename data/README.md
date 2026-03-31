# Dataset Folder

This folder contains the datasets used in the **Big Data PySpark project** for machine learning pipelines.

It includes datasets for **classification** (Diabetes prediction) and **regression** (House price prediction).  
These CSV files are meant to be used in a **distributed computing environment** via HDFS.

---

## 1. Diabetes Dataset (`diabetes.csv`)

**Task:** Classification – predict whether a patient has diabetes.

**Columns:**

| Column | Description |
|--------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skinfold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction | Genetic diabetes risk function |
| Age | Age of the patient (years) |
| Outcome | Diabetes outcome (0 = no, 1 = yes) |

**Sample rows:**

**Notes:**  
- This dataset is suitable for classification tasks.  
- Missing values should be handled during preprocessing (e.g., zero values replaced with mean).  

---

## 2. House Price Dataset (`house_prices_dataset.csv`)

**Task:** Regression – predict house prices based on input features.

**Columns:**

| Column | Description |
|--------|-------------|
| size | House size in square meters |
| bedrooms | Number of bedrooms |
| age | Age of the house in years |
| distance_city_km | Distance to city center in kilometers |
| price | House price in thousands (target variable) |

**Sample rows:**

**Notes:**  
- This dataset is suitable for regression tasks.  
- Ensure numeric columns are correctly typed for ML processing.  

---
## Notes
Local CSV files are optional, mainly for reference.
For production or large-scale experiments, always use HDFS as the source.
Keep this README as documentation for dataset structure, column description, and HDFS usage.
# Folder Structure
data/
├── README.md
├── diabetes.csv
└── house_prices_dataset.csv

## How to Use

These datasets can be uploaded to **HDFS** for Big Data processing.

### Step 1: Create HDFS directory

```bash
hdfs dfs -mkdir -p /data
hdfs dfs -put data/diabetes.csv /data/
hdfs dfs -put data/house_prices_dataset.csv /data/
hdfs dfs -ls /data
data_path_diabetes = "hdfs://m1:9000/data/diabetes.csv"
data_path_house = "hdfs://m1:9000/data/house_prices_dataset.csv"
hdfs dfs -get /data/diabetes.csv ./data/
hdfs dfs -get /data/house_prices_dataset.csv ./data/
