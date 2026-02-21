# Task 1: Exploring and Visualizing a Simple Dataset

## Objective:

Learn how to **load**, **inspect**, and **visualize a dataset** to understand data trends and distributions.

## Dataset:

**Iris** Dataset (CSV format, can be loaded via seaborn or downloaded)

## Instructions:

- Load the dataset using pandas.
- Print the shape, column names, and the first few rows using `.head()`.
- Use `.info()` and `.describe()` for summary statistics.

### Visualize the dataset:

- Create a **scatter plot** to show relationships between features.

- Use **histograms** to show value distributions.
- Use **box plots** to identify outliers.
- Use **matplotlib** and **seaborn** for plotting.

### Skills:

- Data loading and inspection using **pandas**
- Descriptive statistics and data exploration
- Basic plotting and visualization with seaborn and matplotlib

## How the Tasks Were Done:

### Data Loading & Inspection

- Loaded the Iris dataset using `seaborn.load_dataset('iris')`
- Inspected dataset structure with `.shape`, `.columns`, and `.head(5)`
- Generated summary statistics using `.info()` and `.describe()` methods

### Data Visualization

- **Scatter Plots**: Created 4 scatter plots showing relationships between features:
  - Sepal length vs Petal length
  - Sepal length vs Petal width
  - Sepal width vs Petal length
  - Sepal width vs Petal width

- **Histogram**: Visualized the distribution of petal_length using 10 bins

- **Box Plot**: Created a box plot showing petal_length distribution across different iris species with color differentiation

### **Problems Faced & Solutions:**

The main challenge was understanding how box plots identify outliers internally:

### **Problem**:

Understanding the statistical computation behind outlier detection in box plots

### **Solution**:

Implemented manual outlier detection using the Interquartile Range (IQR) method which might have slight mismatch with seaborn's internal calcualtion for **outliers**
